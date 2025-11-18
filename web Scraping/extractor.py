import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

BRD_MEET_URL = "https://abespa.alabama.gov/board_meetings.aspx" 

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def data_scrapping():

    print(f"Scraping Program starts ==>> {BRD_MEET_URL}")
    
    try:
        response = requests.get(BRD_MEET_URL, headers=HEADERS, timeout=15)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')

        tbl_title = soup.find('h2')
        filename = tbl_title.get_text()
        xlsheet = f"{filename}_Scrapped Data.xlsx"

        table = soup.find('table', class_='table-striped')

        dataWeScraped = []
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        rows = table.find_all('tr')
        print(f"Found {len(rows)} rows in the table.")

        # for index, row in enumerate(rows):
        #     cells = row.find_all('td')
        #     meet_dates = ' '.join(cell.get_text(strip=True) for cell in cells)

        slno=1
        for row in rows:
            cells=row.find_all('td')
            meet_dates = ''.join(cell.get_text(strip=True)for cell in cells)

            if meet_dates: 
                dataWeScraped.append({
                    'Sl No.': slno,
                    'Board Meeting Dates': meet_dates,
                    'Data Extracted Time': timestamp
                })
                slno+=1

        # the panda dattaframe
        df = pd.DataFrame(dataWeScraped)

        df.to_excel(xlsheet, index=False, engine='openpyxl')
        print(f"Data suceessfully extracted to '{xlsheet}'")

    except requests.exceptions.HTTPError as errh:
        print(f"This HTTP Error: {errh}")
        print("404 / VPN not set to US")
    except Exception as e:
        print(f"This error: {e}")


if __name__ == "__main__":
    data_scrapping()