"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import load_config
from src.mock_provider import MockProvider
from src.openai_provider import OpenAIProvider

MAX_PROMPT_LENGTH = 4000


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    # TODO: implement this function.
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    normalized_prompt = prompt.strip()
    if not normalized_prompt:
        raise ValueError("Prompt cannot be empty.")
    if len(normalized_prompt) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt must not exceed {MAX_PROMPT_LENGTH} characters.")

    return normalized_prompt


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    # TODO: implement this function.
    provider_name = config.get("LLM_PROVIDER", "mock")
    if not isinstance(provider_name, str):
        raise TypeError("LLM_PROVIDER must be a string.")

    provider_name = provider_name.strip().lower()
    if provider_name == "mock":
        return MockProvider()
    if provider_name == "openai":
        api_key = config.get("OPENAI_API_KEY", "")
        model = config.get("OPENAI_MODEL", "")
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError("OPENAI_API_KEY is required for the openai provider.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("OPENAI_MODEL is required for the openai provider.")
        return OpenAIProvider(api_key=api_key.strip(), model=model.strip())

    raise ValueError("Unsupported LLM_PROVIDER. Choose 'mock' or 'openai'.")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    # TODO: implement this function.
    validated_prompt = validate_prompt(prompt)
    provider = create_provider(load_config())
    response = provider.generate(validated_prompt)
    return {
        "text": response.text,
        "provider": response.provider,
        "model": response.model,
    }


def main() -> None:
    """Simplified CLI entry point for the lab."""
    print("LLMOps Lab 02")

    try:
        config = load_config()
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("Provider:", config.get("LLM_PROVIDER", "mock"))

    prompt = input("\nEnter prompt:\n> ")

    try:
        response = generate_response(prompt)
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("\nResponse:")
    print(response["text"])


if __name__ == "__main__":
    main()
