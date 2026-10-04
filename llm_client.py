from openai import OpenAI
import os

# We define all providers. If a key is missing, the code skips it automatically.
PROVIDERS = [
    {"name": "gemini", "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "model": "gemini-2.5-flash-lite", "key_env": "GEMINI_API_KEY"},
    {"name": "groq", "base_url": "https://api.groq.com/openai/v1", "model": "llama-3.3-70b-versatile", "key_env": "GROQ_API_KEY"},
    {"name": "openrouter", "base_url": "https://openrouter.ai/api/v1", "model": "openrouter/free", "key_env": "OPENROUTER_API_KEY"},
    {"name": "mistral", "base_url": "https://api.mistral.ai/v1", "model": "mistral-small-latest", "key_env": "MISTRAL_API_KEY"},
    {"name": "sambanova", "base_url": "https://api.sambanova.ai/v1", "model": "Meta-Llama-3.3-70B-Instruct", "key_env": "SAMBANOVA_API_KEY"},
 {"name": "nvidia", "base_url": "https://integrate.api.nvidia.com/v1", "model": "nvidia/nemotron-3-super-120b-a12b", "key_env": "NVIDIA_API_KEY"},
]

def chat(messages: list, temperature: float = 0.3) -> str:
    for p in PROVIDERS:
        api_key = os.getenv(p["key_env"])
        if not api_key:
            continue  # Skip if you haven't added this key to your .env yet
        try:
            client = OpenAI(base_url=p["base_url"], api_key=api_key)
            resp = client.chat.completions.create(
                model=p["model"], messages=messages, temperature=temperature
            )
            return resp.choices[0].message.content
        except Exception as e:
            print(f"[{p['name']}] failed: {e}, trying next...")
    raise RuntimeError("All LLM providers failed. Do you have at least one valid API key in your .env?")