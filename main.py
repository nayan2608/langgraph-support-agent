import os

from dotenv import load_dotenv


def main() -> None:
    # Load provider/model configuration before importing the graph.
    load_dotenv()

    model = os.getenv("MODEL")
    if not model:
        raise RuntimeError(
            "MODEL is missing. Add it to .env, for example MODEL=google_genai:gemini-3.7-flash"
        )

if __name__ == "__main__":
    main()
