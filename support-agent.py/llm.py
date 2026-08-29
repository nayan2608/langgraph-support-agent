import os
from functools import lru_cache

from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel


@lru_cache(maxsize=1)
def get_llm() -> BaseChatModel:
    """Create the chat model configured through environment variables.

    MODEL should preferably use LangChain's provider:model format, for example:
    - openai:gpt-4.1-mini
    - anthropic:claude-sonnet-4-6
    - google_genai:gemini-2.5-flash
    - groq:llama-3.3-70b-versatile
    - openrouter:auto

    The selected provider's integration package and credentials must be installed/configured.
    """
    model = os.getenv("MODEL", "google_genai:gemini-3.7-flash")
    temperature = float(os.getenv("TEMPERATURE", "0"))

    return init_chat_model(
        model,
        temperature=temperature,
    )
