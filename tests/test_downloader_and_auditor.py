import os
import sys
import argparse
from unittest.mock import patch, mock_open
import pytest

# Dodanie katalogu src do ścieżek wyszukiwania modułów Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.downloader import create_directory, check_local_reports, download_reports

def test_downloader_missing_range():
    with pytest.raises(argparse.ArgumentError) as excinfo:
        sys.argv = ["downloader.py", "--ticker", "CDR"]
        from src.downloader import main
        main()
    assert "argument --range is required" in str(excinfo.value)

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
        "Dostępne lata: [2024]",
        "Brakujące lata: [2024]"
    ]
    
    # Sprawdzenie czy funkcja wypisała oczekiwane informacje
    captured = capsys.readouterr()
    assert all(output in captured.out for output in expected_output)
