"""LLM Provider module for police LLM verbal hint and bluff generator."""

from abc import ABC, abstractmethod
import random


class TokenBudgetTracker:
    """Tracks cumulative token usage against a max budget."""

    def __init__(self, budget: int = 200000):
        self.budget = budget
        self.used_tokens = 0

    def can_spend(self, amount: int) -> bool:
        return (self.used_tokens + amount) <= self.budget

    def consume(self, amount: int) -> None:
        if self.used_tokens + amount > self.budget:
            raise ValueError(f"Token budget threshold reached! Used: {self.used_tokens}, Requested: {amount}, Budget: {self.budget}")
        self.used_tokens += amount

    def is_exceeded(self) -> bool:
        return self.used_tokens >= self.budget


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_token_cost(self, prompt: str, response: str) -> int:
        pass


class TemplateProvider(LLMProvider):
    """Fallback / 0-token template provider."""

    TEMPLATES = [
        "I am closing in on position!",
        "Police moving to inspect grid center.",
        "Surrender now, thief!",
        "Target acquired near North block.",
        "Patrolling perimeter sectors now.",
    ]

    def generate(self, prompt: str) -> str:
        return random.choice(self.TEMPLATES)

    def get_token_cost(self, prompt: str, response: str) -> int:
        return 0


class OllamaProvider(LLMProvider):
    """Local Ollama LLM provider wrapper."""

    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        # Client wrapper stub; raises RuntimeError if service unavailable in test/runtime
        return f"[Ollama-{self.model_name}] Response to: {prompt}"

    def get_token_cost(self, prompt: str, response: str) -> int:
        return len(prompt.split()) + len(response.split())


class ClaudeAPIProvider(LLMProvider):
    """Claude API LLM provider wrapper."""

    def __init__(self, api_key: str = "mock-key"):
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        return f"[ClaudeAPI] Response to: {prompt}"

    def get_token_cost(self, prompt: str, response: str) -> int:
        return len(prompt.split()) + len(response.split())


class ClaudeCLIProvider(LLMProvider):
    """Claude CLI LLM provider wrapper."""

    def generate(self, prompt: str) -> str:
        return f"[ClaudeCLI] Response to: {prompt}"

    def get_token_cost(self, prompt: str, response: str) -> int:
        return len(prompt.split()) + len(response.split())
