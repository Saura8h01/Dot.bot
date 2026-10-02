from llm_client import chat

async def process_message(text: str) -> str:
    lower = text.lower()
    
    if lower == "/status":
        return "🟢 Dot is online. Brain is working."
        
    # Default: Use the LLM
    return chat([
        {"role": "system", "content": "You are Dot, an always-on AI agent. Be concise and helpful."},
        {"role": "user", "content": text}
    ])