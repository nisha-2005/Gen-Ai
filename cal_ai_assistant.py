import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Cohere API Key
COHERE_API_KEY = os.getenv("MroDIYVmCxafasShCdLjXvEuNcTXUSemNca5MXDU")

if not COHERE_API_KEY:
    print("❌ Error: COHERE_API_KEY not found in .env file.")
    exit(1)

# Initialize Cohere Client
co = cohere.Client(COHERE_API_KEY)

def get_ai_response(prompt):
    try:
        response = co.chat(
            message=prompt,
            model="command-r-plus",
            temperature=0.4,
        )
        return response.text
    except cohere.error.UnauthorizedError:
        return "❌ Invalid Cohere API key. Please check your .env file."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# --- Assistant Loop ---
print("📅 Cal AI Assistant — Powered by Cohere")
print("Ask about your schedule or say 'book a call'. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    response_text = get_ai_response(user_input)
    print("🤖 AI:", response_text, "\n")
