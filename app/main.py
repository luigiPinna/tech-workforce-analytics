import requests
from bs4 import BeautifulSoup
import json
import os
import time
from typing import Dict, List, Optional, Any
import sys

sys.path.append('./config')
from config.env_manager import EnvManager

from constants.companies import COMPANIES


class EmployeeScraper:
    """Classe per lo scraping dei dati dei dipendenti dalle aziende su Macrotrends."""

    def __init__(self):
        # Inizializza il gestore delle variabili d'ambiente
        self.env = EnvManager()

        # Carica le configurazioni dalle variabili d'ambiente
        self.headers = {
            "User-Agent": self.env.get("USER_AGENT")
        }
        self.base_url = self.env.get("BASE_URL")
        self.timeout = self.env.get_int("REQUEST_TIMEOUT", 30)
        self.retry_attempts = self.env.get_int("RETRY_ATTEMPTS", 3)
        self.retry_delay = self.env.get_int("RETRY_DELAY", 2)

        # Percorsi per il salvataggio dei risultati
        self.output_dir = self.env.get("OUTPUT_DIR", "../output")
        self.output_file = self.env.get("OUTPUT_FILE", "employee_data.json")

    def scrape_employee_data(self, company_ticker: str) -> Optional[Dict[str, Any]]:
        """Scraping dei dati dei dipendenti per una specifica azienda."""
        if company_ticker not in COMPANIES:
            print(f"Ticker {company_ticker} non trovato nel dizionario.")
            return None

        company_name = COMPANIES[company_ticker]
        print(f"Tentativo di scraping da Macrotrends per {company_name}...")

        url = f"{self.base_url}{company_ticker}/{company_name}/number-of-employees"
        print(f"Tentativo con URL: {url}")

        # Implementa sistema di retry
        for attempt in range(self.retry_attempts):
            try:
                response = requests.get(
                    url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                response.raise_for_status()

                # Se la richiesta va a buon fine, procedi con il parsing
                return self._parse_employee_data(response.text, company_name, company_ticker)

            except requests.RequestException as e:
                print(f"Tentativo {attempt + 1} fallito per {company_name}: {e}")
                if attempt < self.retry_attempts - 1:
                    print(f"Nuovo tentativo tra {self.retry_delay} secondi...")
                    time.sleep(self.retry_delay)
                else:
                    print(f"Tutti i tentativi falliti per {company_name}")
                    return None

    def _parse_employee_data(self, html_content: str, company_name: str, company_ticker: str) -> Optional[
        Dict[str, Any]]:
        """Analizza il contenuto HTML per estrarre i dati dei dipendenti."""
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table', class_='historical_data_table')

        if not table:
            print(f"Tabella dei dati non trovata per {company_name}")
            return None

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

    def scrape_all_companies(self) -> Dict[str, Any]:
        """Scraping dei dati dei dipendenti per tutte le aziende nel dizionario COMPANIES."""
        results = {}
        for ticker, company_name in COMPANIES.items():
            print(f"\nElaborazione: {company_name} ({ticker})")
            result = self.scrape_employee_data(ticker)
            if result:
                results[ticker] = result
            else:
                print(f"Impossibile recuperare dati per {company_name}")

        # Salva i risultati in un file JSON
        self._save_results(results)
        return results

    def _save_results(self, results: Dict[str, Any]) -> None:
        """Salva i risultati in un file JSON."""
        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, self.output_file)

        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)

        print(f"\nDati salvati in {output_path}")


# Esegui lo scraping per tutte le aziende
if __name__ == "__main__":
    scraper = EmployeeScraper()
    scraper.scrape_all_companies()