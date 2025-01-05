import requests
from bs4 import BeautifulSoup
import json
import os

# Configurații pentru scraping
URL = "https://www.autovit.ro/autoturisme?search%5Bfilter_float_price%3Ato%5D=8000&search%5Border%5D=created_at_first%3Adesc&search%5Badvanced_search_expanded%5D=true"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
MAX_LISTINGS = 100

# Director pentru salvarea imaginilor
IMAGE_DIR = "autovit_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Stocăm datele aici
listings = []

# Funcție pentru a extrage detalii despre anunțuri
def get_listings(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Nu am putut accesa site-ul.")
        print(f"Cod de eroare: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    ads = soup.find_all("article", class_="ooa-1yux8sr")

    for ad in ads:
        try:
            # Găsim link-ul anunțului
            link_tag = ad.find("a", href=True)
            link = link_tag['href'] if link_tag else "N/A"

            # Găsim titlul anunțului
            title_tag = ad.find("h2")
            title = title_tag.text.strip() if title_tag else "N/A"

            # Găsim prețul
            price_tag = ad.find("h3", class_="e6r213i1 ooa-1n2paoq er34gjf0")
            price = price_tag.text.strip() if price_tag else "N/A"

            # Găsim anul, kilometrii și alte detalii
            details_tag = ad.find("p", class_="ewg8vos8")
            details_text = details_tag.text.strip() if details_tag else "N/A"

            # Găsim kilometrajul și anul
            year = "N/A"
            km = "N/A"
            if details_text:
                parts = details_text.split(" • ")
                if len(parts) >= 3:
                    year = parts[-2].strip()
                    km = parts[-3].strip()

            # Găsim locația și data publicării
            location_tag = ad.find("p", class_="ooa-gmxnzj")
            location = location_tag.text.strip() if location_tag else "N/A"

            # Găsim poza anunțului
            image_tag = ad.find("img")
            image_url = image_tag['src'] if image_tag else "N/A"

            # Salvăm imaginea local
            image_path = "N/A"
            if image_url != "N/A":
                image_name = os.path.join(IMAGE_DIR, os.path.basename(image_url.split("?")[0]))
                image_data = requests.get(image_url).content
                with open(image_name, "wb") as img_file:
                    img_file.write(image_data)
                image_path = image_name

            # Adăugăm la listă
            listings.append({
                "Link": link,
                "Sumar": title,
                "Prețul": price,
                "Anul": year,
                "Kilometri": km,
                "Locația": location,
                "Imagine": image_path
            })

            if len(listings) >= MAX_LISTINGS:
                break

        except Exception as e:
            print(f"Eroare la procesarea unui anunț: {e}")
            continue

    return listings

# Extragem datele
print("Extragem anunțurile...")
listings = get_listings(URL)

# Salvăm datele într-un fișier JSON
output_file = "autovit_listings.json"
if listings:
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(listings, f, ensure_ascii=False, indent=4)
    print(f"Am salvat {len(listings)} anunțurile în {output_file}.")
else:
    print("Nu am găsit anunțurile.")
