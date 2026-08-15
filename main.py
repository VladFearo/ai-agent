import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not found in environment variables.")
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    messages = [
    {
        "role": "user",
        "content": args.user_prompt
    }
]

    
    res = client.chat.completions.create(model="openrouter/free", messages=messages)
    if not res.usage:
         raise RuntimeError("No usage information returned from the API.")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {res.usage.prompt_tokens}")
        print(f"Response tokens: {res.usage.completion_tokens}")
    print(res.choices[0].message.content)

if __name__ == "__main__":
    main()
