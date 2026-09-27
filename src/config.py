"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations


import os

def load_config() -> dict:
    return {
        "LLM_PROVIDER": os.getenv("LLM_PROVIDER", "mock"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", ""),
    }
