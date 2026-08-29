# LangGraph Customer Support Routing Agent

A small LangGraph project that classifies customer-support tickets, routes urgent/negative tickets to human escalation, and drafts automatic responses for normal tickets.

## Graph

```text
START
  ↓
classify_ticket
  ↓
  ├── high priority / negative → escalate_ticket → END
  └── normal                  → draft_response → finalize_response → END
```

## Model-agnostic LLM configuration

The LangGraph workflow is not tied to Gemini, OpenAI, or any single provider. It uses LangChain's `init_chat_model()` factory.

Set the desired model in `.env` using `provider:model` format:

```env
MODEL=openai:gpt-4.1-mini
TEMPERATURE=0
OPENAI_API_KEY=your_key
```

Change only environment configuration to switch models:

```env
MODEL=anthropic:claude-sonnet-4-6
ANTHROPIC_API_KEY=your_key
```

```env
MODEL=google_genai:gemini-2.5-flash
GOOGLE_API_KEY=your_key
```

```env
MODEL=groq:llama-3.3-70b-versatile
GROQ_API_KEY=your_key
```

Other LangChain-supported providers can also be used. Install the provider integration package required by that provider, then set its credentials and `MODEL` value.

## Project structure

```text
langgraph-support-agent/
├── support_agent/
│   ├── __init__.py
│   ├── graph.py
│   ├── llm.py
│   ├── nodes.py
│   └── state.py
├── .env.example
├── .gitignore
├── langgraph.json
├── main.py
├── README.md
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and configure one provider/model.

Run:

```bash
python main.py
```

## Adding another provider

If the provider is not already included in `requirements.txt`, install its LangChain integration package and add it to your dependencies. The graph and node code do not need to change.
