import os
import sys
import argparse
from unittest.mock import patch, mock_open
import pytest

# Dodanie katalogu src do ścieżek wyszukiwania modułów Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.downloader import create_directory, check_local_reports, download_reports

def test_downloader_missing_range():
    with pytest.raises(SystemExit) as excinfo:
        sys.argv = ["downloader.py", "--ticker", "CDR"]
        from src.downloader import main
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 2

@patch('os.makedirs')
@patch('os.walk')
def test_auditor(mock_walk, mock_makedirs, capsys):
    # Mockowanie struktury folderów
    mock_walk.return_value = [
        ("data/CDR", [], ["Q1_2024.pdf", "Q2_2024.pdf"])
    ]
    
    # Tworzenie katalogu
    create_directory("CDR")
    
    # Sprawdzenie lokalnych raportów
    check_local_reports("CDR", 2024, 2024)
    
    # Oczekiwany output
    expected_output = [
        "Dostępne kwartały: ['Q1_2024', 'Q2_2024']",
        "Brakujące kwartały: ['Q3_2024', 'Q4_2024']"
    ]
    
    # Sprawdzenie czy funkcja wypisała oczekiwane informacje
    captured = capsys.readouterr()
    assert all(output in captured.out for output in expected_output)
