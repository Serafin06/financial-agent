import os
import sys

# Dodanie katalogu src do ścieżek wyszukiwania modułów Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pdf_parser import pdf_to_markdown
from ollama_client import query_qwen
from db import MongoDBHandler

def main():
    # Wyznaczenie ścieżki głównej projektu (parent dir dla src)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    prompt_path = os.path.join(base_dir, "prompts", "pdf_to_json.md")

    if not os.path.exists(prompt_path):
        print(f"BŁĄD: Nie znaleziono pliku promptu pod ścieżką: {prompt_path}")
        return

    db_handler = MongoDBHandler()

    with open(prompt_path, "r", encoding="utf-8") as f:
        system_prompt = f.read()

    pdf_found = False
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".pdf"):
                pdf_found = True
                pdf_path = os.path.join(root, file)
                print(f"\n--- Przetwarzanie: {pdf_path} ---")
                
                print("1. Konwersja PDF do Markdown...")
                md_text = pdf_to_markdown(pdf_path)
                
                print("2. Analiza przez Qwen 2.5 (Ollama)...")
                json_response = query_qwen(system_prompt, md_text)
                
                print("3. Zapis do MongoDB...")
                db_handler.insert_report(json_response)
                print("Zakończono sukcesem!")

    if not pdf_found:
        print(f"\nBrak plików PDF w katalogu {data_dir}. Wrzuć plik raportu do podfolderu w data/ i spróbuj ponownie.")

if __name__ == "__main__":
    main()
