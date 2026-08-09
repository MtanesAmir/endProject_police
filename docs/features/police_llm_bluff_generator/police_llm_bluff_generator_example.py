"""Example demonstrating LLM verbal bluff generator with fallback templates."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.bluff import BluffGenerator

def main():
    generator = BluffGenerator(provider_type="template", hint_max_words=15)
    hint = generator.generate_bluff(state={"my_pos": (0, 0), "target_pos": (3, 3), "intent": "truth"})
    print(f"Generated hint: '{hint}' (word count: {len(hint.split())})")

if __name__ == "__main__":
    main()
