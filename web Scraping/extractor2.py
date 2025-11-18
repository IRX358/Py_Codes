import requests
from bs4 import BeautifulSoup
import pandas as pd

INFO_URL = "https://abespa.alabama.gov/consumer.aspx" 

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def data_scrapping2():
    print(f"Scraping Program starts ==>> {INFO_URL}")
    
    try:
        response = requests.get(INFO_URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        container = soup.find('div', class_='content-container-margins')
        pg_title = container.find('h2')   
        filename = pg_title.get_text()
        xlsheet = f"{filename}_Scrapped Data.xlsx"


        ul = container.find('ul')
        scraped_data = []
        for li in ul.find_all('li'):
            anchor = li.find('a')
            if anchor:
                href_link = anchor.get('href', 'N/A')
                link_text = anchor.get_text(strip=True)
                
                list_text = anchor.next_sibling.strip() if anchor.next_sibling else 'N/A'
                
                scraped_data.append({
                    'Link in the page': href_link,
                    'Text for the LINK': link_text,
                    'Text in the LIST': list_text
                })


        df = pd.DataFrame(scraped_data)
        
        df.insert(0, 'Sl No.', range(1, 1 + len(df)))
        
        df.to_excel(xlsheet, index=False, engine='openpyxl')
        print(f"Data suceessfully extracted to '{xlsheet}'")

    except requests.exceptions.HTTPError as errh:
        print(f"This HTTP Error: {errh}")
        print("404 / VPN not set to US")
    except Exception as e:
        print(f"This error: {e}")


if __name__ == "__main__":
    data_scrapping2()