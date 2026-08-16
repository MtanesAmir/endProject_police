"""Police Trash Talk Profiler module."""

import re
from typing import List, Optional
from src.infra.llm_provider import LLMProvider, TemplateProvider

class TrashTalkProfiler:
    """Psychological profiler classifier evaluating Thief's hints."""
    
    def __init__(self, provider: Optional[LLMProvider] = None):
        self.provider = provider or TemplateProvider()
        
    def evaluate_truthfulness(self, thief_text: str, scent_map: List[List[float]]) -> float:
        """Evaluate if the Thief is telling the truth. Returns reliability weighting 0.0 to 1.0."""
        prompt = (
            f"Thief says: '{thief_text}'.\n"
            f"Current scent map: {scent_map}\n"
            "Is the thief telling the truth? Output a single float reliability score between 0.0 and 1.0."
        )
        try:
            response = self.provider.generate(prompt)
            # Find the first float in the response
            match = re.search(r"(0\.\d+|1\.0)", response)
            if match:
                return float(match.group(1))
        except Exception:
            pass
            
        # Fallback neutral reliability if LLM parsing fails
        return 0.5
