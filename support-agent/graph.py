
from typing import Literal
from .state import SupportState
from langgraph.graph import StateGraph, START, END
from .nodes import classify_ticket, draft_response, escalate_ticket, finalize_response

def choose_route(state: SupportState) -> Literal["escalate", "respond"]:
    if state["priority"] == "high" or state["sentiment"] == "negative":
        return "escalate"
    return "respond"


workflow = StateGraph(SupportState)

workflow.add_node("classify_ticket", classify_ticket)
workflow.add_node("draft_response", draft_response)
workflow.add_node("escalate_ticket", escalate_ticket)
workflow.add_node("finalize_response", finalize_response)

workflow.add_edge(START, "classify_ticket")
workflow.add_conditional_edges(
    "classify_ticket",
    choose_route,
    {
        "escalate": "escalate_ticket",
        "respond": "draft_response",
    },
)
workflow.add_edge("draft_response", "finalize_response")
workflow.add_edge("escalate_ticket", END)
workflow.add_edge("finalize_response", END)

graph = workflow.compile()
