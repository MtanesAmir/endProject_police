"""Unit tests for police_llm_bluff_generator feature."""

import pytest
from src.infra.llm_provider import (
    TokenBudgetTracker,
    TemplateProvider,
    OllamaProvider,
    ClaudeAPIProvider,
    ClaudeCLIProvider,
    LLMProvider,
)
from src.domain.bluff import BluffGenerator, generate_bluff


class ErrorProvider(LLMProvider):
    """Failing LLM provider for testing error fallback."""

    def generate(self, prompt: str) -> str:
        raise ConnectionError("LLM API service unreachable")

    def get_token_cost(self, prompt: str, response: str) -> int:
        return 100


class ExorbitantTokenProvider(LLMProvider):
    """Provider requiring high token count."""

    def generate(self, prompt: str) -> str:
        return "Very long response line that consumes a lot of tokens"

    def get_token_cost(self, prompt: str, response: str) -> int:
        return 500000


def test_token_budget_tracker():
    tracker = TokenBudgetTracker(budget=100)
    assert tracker.can_spend(50)
    tracker.consume(50)
    assert tracker.used_tokens == 50
    assert not tracker.is_exceeded()

    tracker.consume(50)
    assert tracker.is_exceeded()
    assert not tracker.can_spend(1)

    with pytest.raises(ValueError):
        tracker.consume(1)


def test_template_provider_zero_tokens():
    provider = TemplateProvider()
    response = provider.generate("Test prompt")
    assert isinstance(response, str)
    assert len(response) > 0
    assert provider.get_token_cost("Test prompt", response) == 0


def test_ollama_and_claude_providers():
    ollama = OllamaProvider()
    res_ollama = ollama.generate("Test prompt")
    assert "Ollama" in res_ollama
    assert ollama.get_token_cost("Test prompt", res_ollama) > 0

    claude_api = ClaudeAPIProvider()
    res_api = claude_api.generate("Test prompt")
    assert "ClaudeAPI" in res_api
    assert claude_api.get_token_cost("Test prompt", res_api) > 0

    claude_cli = ClaudeCLIProvider()
    res_cli = claude_cli.generate("Test prompt")
    assert "ClaudeCLI" in res_cli
    assert claude_cli.get_token_cost("Test prompt", res_cli) > 0


def test_bluff_generator_default_template():
    gen = BluffGenerator(provider_type="template")
    bluff = gen.generate_bluff({"police_pos": (2, 3)})
    assert isinstance(bluff, str)
    assert len(bluff.split()) <= 15


def test_bluff_generator_fallback_on_network_error():
    failing_gen = BluffGenerator(provider=ErrorProvider())
    bluff = failing_gen.generate_bluff({"police_pos": (1, 1)})
    # Should fall back to TemplateProvider text without crashing
    assert isinstance(bluff, str)
    assert len(bluff) > 0
    assert "LLM API service unreachable" not in bluff


def test_bluff_generator_budget_exhaustion_fallback():
    greedy_gen = BluffGenerator(token_budget=100, provider=ExorbitantTokenProvider())
    bluff = greedy_gen.generate_bluff({"police_pos": (0, 0)})
    # High cost causes fallback to template
    assert isinstance(bluff, str)
    assert len(bluff) > 0


def test_word_limit_truncation():
    class LongTextProvider(LLMProvider):
        def generate(self, prompt: str) -> str:
            return "word " * 30

        def get_token_cost(self, prompt: str, response: str) -> int:
            return 10

    long_gen = BluffGenerator(hint_max_words=10, provider=LongTextProvider())
    bluff = long_gen.generate_bluff()
    assert len(bluff.split()) <= 10


def test_standalone_generate_bluff_function():
    bluff = generate_bluff({"turn": 1})
    assert isinstance(bluff, str)
    assert len(bluff) > 0
