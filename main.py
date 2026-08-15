import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
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
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

    
    res = client.chat.completions.create(model="openrouter/free", messages=messages)
    if not res.usage:
         raise RuntimeError("No usage information returned from the API.")
    print(f"Prompt tokens: {res.usage.prompt_tokens}")
    print(f"Response tokens: {res.usage.completion_tokens}")
    print(res.choices[0].message.content)

if __name__ == "__main__":
    main()
