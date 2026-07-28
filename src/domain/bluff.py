"""Domain bluff module for Police agent."""

from typing import Any, Dict, Optional
from src.infra.llm_provider import (
    LLMProvider,
    TokenBudgetTracker,
    TemplateProvider,
    OllamaProvider,
    ClaudeAPIProvider,
    ClaudeCLIProvider,
)


class BluffGenerator:
    """Generates verbal hints and bluffs using LLM providers with token budgeting and fallback isolation."""

    def __init__(
        self,
        provider_type: str = "template",
        token_budget: int = 200000,
        hint_max_words: int = 15,
        provider: Optional[LLMProvider] = None,
    ):
        self.provider_type = provider_type
        self.token_budget = token_budget
        self.hint_max_words = hint_max_words
        self.token_tracker = TokenBudgetTracker(budget=token_budget)

        if provider is not None:
            self.provider = provider
        else:
            self.provider = self._create_provider(provider_type)

        self.fallback_provider = TemplateProvider()

    def _create_provider(self, provider_type: str) -> LLMProvider:
        p_type = provider_type.lower()
        if p_type == "template":
            return TemplateProvider()
        elif p_type == "ollama":
            return OllamaProvider()
        elif p_type == "claude_api":
            return ClaudeAPIProvider()
        elif p_type == "claude_cli":
            return ClaudeCLIProvider()
        else:
            return TemplateProvider()

    def generate_bluff(self, state: Optional[Dict[str, Any]] = None) -> str:
        """Generate a bluff/hint string given the current game state."""
        prompt = f"State: {state}" if state else "Generate tactical bluff for Police agent."

        # Check if tracker is already exceeded or cannot spend minimum tokens
        if self.token_tracker.is_exceeded():
            text = self.fallback_provider.generate(prompt)
            return self._truncate_words(text)

        try:
            raw_text = self.provider.generate(prompt)
            cost = self.provider.get_token_cost(prompt, raw_text)
            if self.token_tracker.can_spend(cost):
                self.token_tracker.consume(cost)
                text = raw_text
            else:
                # Token budget threshold reached, fallback to TemplateProvider
                text = self.fallback_provider.generate(prompt)
        except Exception:
            # Failure isolation: fallback to TemplateProvider on network or execution error
            text = self.fallback_provider.generate(prompt)

        return self._truncate_words(text)

    def _truncate_words(self, text: str) -> str:
        words = text.split()
        if len(words) > self.hint_max_words:
            return " ".join(words[: self.hint_max_words])
        return text


def generate_bluff(state: Optional[Dict[str, Any]] = None, generator: Optional[BluffGenerator] = None) -> str:
    """Standalone module-level function to generate bluff given state."""
    if generator is None:
        generator = BluffGenerator()
    return generator.generate_bluff(state)
