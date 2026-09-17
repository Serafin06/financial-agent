# 📈 Financial Agent GPW — Architecture & Roadmap

Autonomiczny agent lokalny oparty na modelu **Qwen 2.5 (14B)** do ekstrakcji, analizy, walidacji i wizualizacji sprawozdań finansowych spółek z Giełdy Papierów Wartościowych w Warszawie (GPW).

---

## 🏗️ Architektura Systemu i Poliglotyzm

System wykorzystuje podejście **mikroserwisowe / hybrydowe**, łącząc zalety trzech języków programowania:

1. **Python (Core Engine & AI RAG)** 🐍
   - Pobieranie surowych raportów PDF (ESPI/EBI/Strony Spółek).
   - Konwersja PDF $\rightarrow$ Markdown (`pymupdf4llm` / `Docling`).
   - Orkiestracja promptów i komunikacja z Ollamą (`qwen2.5-coder:14b`).
   - Ekstrakcja surowych struktur JSON i zapis do MongoDB.
   - Scraping / Walidacja krzyżowa z Biznesradar.

2. **Rust (High-Performance Engine)** 🦀 *(Opcjonalny moduł obliczeniowy)*
   - Błyskawiczne, deterministyczne przeliczanie skomplikowanych wskaźników finansowych (ROE, ROIC, Altman Z-Score, DCF, Piotroski F-Score).
   - Wykorzystywany jako natywne rozszerzenie Pythona (przez `PyO3`) lub ultra-szybki mikroserwis CLI do przetwarzania masowego setek sprawozdań.

3. **Kotlin (Backend API & Cloud Bridge)** 🪟
   - Rest API (Spring Boot / Ktor) pośredniczące między MongoDB a aplikacją frontendową.
   - Obsługa autoryzacji, powiadomień i zarządzania kolejkami analiz na serwerze produkcyjnym / cloudzie.

---

## 🔄 Schemat Działania Pipeline'u (Data Flow)

```text
[ 1. Input PDF ]
       │
       ▼
[ Python: pdf_parser ] ──► (Konwersja PDF -> Markdown z tabelami)
       │
       ▼
[ Python: ollama_client ] ──► (Ollama + Qwen 2.5 14B z promptem w /prompts)
       │
       ▼
[ 2. Raw JSON Data ]
       │
       ├──────────────────────────────┐
       ▼                              ▼
[ Python: biznesradar_checker ]  [ Rust Math Engine ]
(Walidacja i flaga uderzeń)     (Obliczanie wskaźników & modeli)
       │                              │
       └──────────────┬───────────────┘
                      ▼
            [ Local MongoDB ]
                      │
                      ▼
           [ Kotlin Backend API ]
                      │
                      ▼
       [ Frontend Web / Dashboard ]
