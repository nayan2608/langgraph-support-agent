
from .state import SupportState
from langgraph.graph import StateGraph
from .nodes import classify_ticket, draft_response, escalate_ticket, finalize_response

workflow = StateGraph(SupportState)

workflow.add_node("classify_ticket", classify_ticket)
workflow.add_node("draft_response", draft_response)
workflow.add_node("escalate_ticket", escalate_ticket)
workflow.add_node("finalize_response", finalize_response)