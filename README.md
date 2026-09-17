Autonomiczny agent lokalny oparty na modelu **Qwen 2.5 (14B)** do ekstrakcji, analizy, walidacji i wizualizacji sprawozdań finansowych spółek z GPW.

## 🏗️ Architektura Systemu (Multi-Language)
- 🐍 **Python**: Korpus aplikacji, konwersja PDF (pymupdf4llm), Ollama API, połączenie z MongoDB, skrobanie Biznesradar.
- 🦀 **Rust**: Przyszły silnik obliczeniowy do szybkiego liczenia wskaźników finansowych (ROE, DCF, Altman Z-Score).
- 🪟 **Kotlin**: Przyszły serwer REST API pod aplikację webową.

## 📌 Obecny Stan Projektu (Status)
- [x] Docker z bazą MongoDB oraz Mongo Express (`http://localhost:8081`).
- [x] Środowisko Python (`venv`) i skrypt `src/main.py`.
- [x] Klient Ollama łączący się z `qwen2.5-coder:14b`.
- [x] Zewnętrzny prompt w `prompts/pdf_to_json.md`.
- [ ] **NASTĘPNY KROK:** Pierwszy test na surowym pliku PDF w `data/` i sprawdzenie zapisu w MongoDB.
- [ ] Walidacja danych z serwisem Biznesradar (`src/biznesradar_checker.py`).

## 🚀 Uruchomienie lokalne
```bash
docker compose up -d
source venv/bin/activate
python src/main.py
```

Autonomiczny agent lokalny wykorzystujący model **Qwen 2.5 (14B)** do ekstrakcji, analizy, walidacji i wizualizacji sprawozdań finansowych spółek z GPW.

## 🚀 Przykłady Użycia z Basha

1. **Sprawdzenie aktualności pobranych raportów (Audyt):**
   ```bash
   python src/auditor.py
2. Pobranie brakujących raportów (wymagany ticker i zakres dat):

```bash
python src/downloader.py --ticker CDR --range 2023-2025
```
3. Uruchomienie analizy AI na wczytanych plikach PDF:

```bash
python src/main.py
```
📁 Podgląd Bazy Danych
Dostępny w przeglądarce pod adresem: http://localhost:8081 (Login: admin / pass).
EOF
