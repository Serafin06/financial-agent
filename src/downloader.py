import os
import sys
from datetime import datetime, timedelta

def create_directory(ticker):
    directory = f"data/{ticker}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def download_reports(ticker, years=None):
    # Placeholder dla funkcji pobierającej raporty PDF
    print(f"Pobieranie raportów dla {ticker}...")
    
    if years:
        start_year, end_year = map(int, years.split('-'))
        for year in range(start_year, end_year + 1):
            print(f"Pobieranie raportu za rok {year}...")
            # Tutaj powinien być kod pobierający raporty z odpowiednich stron
    else:
        print("Pobieranie najnowszego dostępnego raportu...")
        # Tutaj powinien być kod pobierający najnowszy dostępny raport

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
        print("Użycie: python downloader.py <ticker> [years]")
        print("Przykład: python downloader.py CDR 2024-2025")
        return

    ticker = sys.argv[1]
    years = sys.argv[2] if len(sys.argv) > 2 else None

    directory = create_directory(ticker)
    download_reports(ticker, years)

if __name__ == "__main__":
    main()
