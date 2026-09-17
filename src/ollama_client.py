import ollama

def query_qwen(system_prompt: str, user_content: str) -> dict:
    """Wysyła zapytanie do lokalnej Ollamy z wymuszeniem struktury JSON."""
    response = ollama.generate(
        model='qwen2.5-coder:14b',
        prompt=f"{system_prompt}\n\nTekst raportu:\n{user_content[:12000]}", # Ograniczenie kontekstu na start
        format='json'
    )
    return response['response']
