import requests
from bs4 import BeautifulSoup
import json
import os

# Dizionario delle aziende con i loro ticker e nomi per Macrotrends
COMPANIES = {
    "AMZN": "amazon",
    "META": "meta-platforms",
    "IBM": "ibm",
    "MSFT": "microsoft",
    "TSLA": "tesla",
    "GOOGL": "alphabet",
    "AAPL": "apple",
    "NFLX": "netflix",
    "NVDA": "nvidia",
    "CRM": "salesforce",
    "INTC": "intel",
    "CSCO": "cisco",
    "ORCL": "oracle",
    "ADBE": "adobe",
    "PYPL": "paypal",
    "UBER": "uber-technologies",
    "SNAP": "snap",
    "SQ": "square"
}


def scrape_employee_data(company_ticker):
    if company_ticker not in COMPANIES:
        print(f"Ticker {company_ticker} non trovato nel dizionario.")
        return None

    company_name = COMPANIES[company_ticker]
    print(f"Tentativo di scraping da Macrotrends per {company_name}...")

    url = f"https://www.macrotrends.net/stocks/charts/{company_ticker}/{company_name}/number-of-employees"
    print(f"Tentativo con URL: {url}")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        table = soup.find('table', class_='historical_data_table')

        if table:
            employee_data = []
            rows = table.find('tbody').find_all('tr')

            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    year = columns[0].text.strip()
                    employee_count_str = columns[1].text.strip().replace(',', '')

                    # Se il campo è vuoto, aggiungi None
                    employee_count = int(employee_count_str) if employee_count_str else None

                    employee_data.append({
                        "year": year,
                        "employee_count": employee_count
                    })

            result = {
                "company": company_name,
                "ticker": company_ticker,
                "data": employee_data
            }

            return result
        else:
            print(f"Tabella dei dati non trovata per {company_name}")
            return None

    except requests.RequestException as e:
        print(f"Errore nella richiesta per {company_name}: {e}")
        return None


def scrape_all_companies():
    results = {}
    for ticker, company_name in COMPANIES.items():
        print(f"\nElaborazione: {company_name} ({ticker})")
        result = scrape_employee_data(ticker)
        if result:
            results[ticker] = result
        else:
            print(f"Impossibile recuperare dati per {company_name}")

    # Salva i risultati in un file JSON
    os.makedirs('output', exist_ok=True)
    output_file = 'output/employee_data.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"\nDati salvati in {output_file}")
    return results


# Esegui lo scraping per tutte le aziende
if __name__ == "__main__":
    scrape_all_companies()