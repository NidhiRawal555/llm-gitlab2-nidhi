"""Optional OpenAI provider implementation for Lab 02."""

from __future__ import annotations

from src.models import LLMResponse
from src.provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """Provider implementation backed by the OpenAI Python SDK."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the OpenAI SDK."""
        # TODO: implement this method.
        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)
            completion = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            text = completion.choices[0].message.content or ""
        except Exception:
            raise RuntimeError("OpenAI provider request failed.") from None

        return LLMResponse(
            text=text,
            provider="openai",
            model=self.model,
        )
