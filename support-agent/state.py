from typing import Literal, TypedDict


class SupportState(TypedDict, total=False):
    ticket: str
    category: Literal["billing", "technical", "account", "general"]
    priority: Literal["low", "medium", "high"]
    sentiment: Literal["positive", "neutral", "negative"]
    draft_response: str
    final_response: str
    route: str
