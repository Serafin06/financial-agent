# 📈 Financial Agent GPW — Architecture & Roadmap

Autonomiczny agent lokalny oparty na modelu **Qwen 2.5 (14B)** do ekstrakcji, analizy, walidacji i wizualizacji sprawozdań finansowych spółek z GPW.

---

## 🏗️ Architektura Systemu i Poliglotyzm
- 🐍 **Python**: Core Engine (Ollama API, Downloader, Audytor katalogów, PyMuPDF, MongoDB).
- 🦀 **Rust**: Engine obliczeniowy do szybkiego przeliczania wskaźników (ROE, DCF, Altman Z-Score).
- 🪟 **Kotlin**: REST API pod interfejs użytkownika (Spring Boot / Ktor).

---

## 📌 Status Projektu i Roadmapa

### 🟢 Etap 1: Lokalny Fundament & Parser PDF (ZROBIONE)
- [x] Docker z MongoDB + Mongo Express (`http://localhost:8081`).
- [x] Środowisko Python (`venv`) i integracja z Ollamą (`qwen2.5-coder:14b`).
- [x] Podstawowy pipeline przetwarzania w `src/main.py`.
- [x] Konfiguracja Aidera do automatycznego kodowania.

---

### 🟡 Etap 2: Downloader, Audytor Folderów & Walidacja (W TRAKCIE)
- [ ] **Moduł Pobierania Raportów (`src/downloader.py`):**
  - Obowiązkowe parametry CLI: `--ticker` oraz `--range` (obowiązkowy zakres lat, np. `2023-2025`).
  - Tworzenie dedykowanej struktury folderów `data/<TICKER>/`.
  - Pobieranie brakujących raportów okresowych (PDF) z oficjalnych źródeł (PAP/ESPI/Biznesradar).
- [ ] **Audytor i Sprawdzanie Aktualności (`src/auditor.py`):**
  - Skanowanie istniejących podfolderów w `data/` pod kątem posiadanych raportów.
  - Raportowanie brakujących kwartałów (np. `CDR: Posiadane [Q1 2024, Q2 2024], Brakujące: [Q3 2024, Q4 2024]`).
- [ ] **Walidacja danych z Biznesradar (`src/biznesradar_checker.py`).**

---

### 🔴 Etap 3: Silnik Obliczeniowy (RUST / PYTHON)
- [ ] Implementacja modeli predykcyjnych i wyliczanie wskaźników finansowych.

---

### 🔵 Etap 4: Backend Kotlin & Dashboard WWW
- [ ] REST API w Kotlinie oraz interfejs graficzny.
