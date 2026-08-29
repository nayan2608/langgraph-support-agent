import json
from typing import Any

from .llm import get_llm
from .state import SupportState


def _content(response: Any) -> str:
    content = response.content
    if isinstance(content, str):
        return content
    return str(content)


def classify_ticket(state: SupportState) -> dict:
    prompt = f"""
        You are a customer-support triage assistant.
        Analyze the ticket below and return ONLY valid JSON with these keys:
        category: one of billing, technical, account, general
        priority: one of low, medium, high
        sentiment: one of positive, neutral, negative

        Ticket:
        {state['ticket']}
    """
    raw = _content(get_llm().invoke(prompt)).strip()
    raw = raw.removeprefix("```json").removesuffix("```").strip()
    data = json.loads(raw)
    return {
        "category": data["category"],
        "priority": data["priority"],
        "sentiment": data["sentiment"],
    }


def draft_response(state: SupportState) -> dict:
    prompt = f"""
        You are a helpful customer-support agent.
        Write a concise, professional response to this ticket.

        Category: {state['category']}
        Priority: {state['priority']}
        Sentiment: {state['sentiment']}
        Ticket: {state['ticket']}

        Do not invent refunds, credits, account changes, or actions that have not happened.
    """
    response = _content(get_llm().invoke(prompt)).strip()
    return {"draft_response": response}


def escalate_ticket(state: SupportState) -> dict:
    message = (
        "This ticket should be escalated to a human support specialist. "
        f"Reason: priority={state['priority']}, sentiment={state['sentiment']}, "
        f"category={state['category']}."
    )
    return {
        "route": "human_escalation",
        "final_response": message,
    }


def finalize_response(state: SupportState) -> dict:
    return {
        "route": "auto_response",
        "final_response": state["draft_response"],
    }
