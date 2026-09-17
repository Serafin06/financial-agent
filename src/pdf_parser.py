import pymupdf4llm

def pdf_to_markdown(pdf_path: str) -> str:
    """Konwertuje plik PDF do formatu Markdown z zachowaniem struktur tabel."""
    try:
        md_text = pymupdf4llm.to_markdown(pdf_path)
        return md_text
    except Exception as e:
        print(f"Błąd podczas parsowania PDF {pdf_path}: {e}")
        return ""
