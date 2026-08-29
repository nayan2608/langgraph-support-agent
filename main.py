import os

from dotenv import load_dotenv
from support_agent.graph import graph


def main() -> None:
    # Load provider/model configuration before importing the graph.
    load_dotenv()

    model = os.getenv("MODEL")
    if not model:
        raise RuntimeError(
            "MODEL is missing. Add it to .env, for example MODEL=google_genai:gemini-3.7-flash"
        )
    
    ticket = input("Enter a customer support ticket:\n> ").strip()
    if not ticket:
        print("Ticket cannot be empty.")
        return

    result = graph.invoke({"ticket": ticket})

    print("\n--- RESULT ---")
    print(f"Model    : {model}")
    print(f"Category : {result['category']}")
    print(f"Priority : {result['priority']}")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Route    : {result['route']}")
    print("\nResponse:")
    print(result["final_response"])

if __name__ == "__main__":
    main()
