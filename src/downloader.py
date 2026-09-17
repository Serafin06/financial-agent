import os
import sys
import argparse
from datetime import datetime

def create_directory(ticker):
    directory = f"data/{ticker}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def check_local_reports(ticker, start_year, end_year):
    directory = f"data/{ticker}/"
    if not os.path.exists(directory):
        print(f"Brak katalogu {directory}.")
        return

    available_years = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                year = int(file.split('_')[0])
                available_years.add(year)

    missing_years = [year for year in range(start_year, end_year + 1) if year not in available_years]

    print(f"Dostępne lata: {sorted(available_years)}")
    print(f"Brakujące lata: {sorted(missing_years)}")

def download_reports(ticker, start_year, end_year):
    # Placeholder dla funkcji pobierającej raporty PDF
    print(f"Pobieranie raportów dla {ticker} z lat {start_year} do {end_year}...")
    
    for year in range(start_year, end_year + 1):
        if not os.path.exists(f"data/{ticker}/{year}.pdf"):
            print(f"Pobieranie raportu za rok {year}...")
            # Tutaj powinien być kod pobierający raporty z odpowiednich stron
        else:
            print(f"Raport za rok {year} już istnieje.")

def main():
    parser = argparse.ArgumentParser(description="Downloader for financial reports.")
    parser.add_argument("--ticker", required=True, help="Ticker of the company (e.g., CDR)")
    parser.add_argument("--range", required=True, help="Range of years to download (e.g., 2023-2025)")

    args = parser.parse_args()

    ticker = args.ticker
    start_year, end_year = map(int, args.range.split('-'))

    directory = create_directory(ticker)
    check_local_reports(ticker, start_year, end_year)
    download_reports(ticker, start_year, end_year)

if __name__ == "__main__":
    main()
