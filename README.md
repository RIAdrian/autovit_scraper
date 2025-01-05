# autovit_scraper
This project is a Python-based scraper designed to extract car listing details from Autovit.ro. It collects structured data about car ads, including metadata, and saves it for further analysis or use.

Features:
Scrapes Car Listings:

Extracts important details such as:
Car title
Price
Year of manufacture
Mileage
Location
Image URLs
Downloads car images locally and ensures unique naming.
Customizable:

The scraper allows configurations for:
Filtering ads (e.g., price limits).
Maximum number of ads to scrape (MAX_LISTINGS).
Data Storage:

Saves the extracted data in a structured JSON file (autovit_listings.json).
Image Handling:

Downloads images locally into a designated directory (autovit_images).
HTML Structure:
The scraper relies on the structure of Autovit.ro's HTML. Key elements:

Each car listing is wrapped in an <article> tag with the class ooa-1yux8sr.
Key attributes extracted:
Title: Found in an <h2> tag within the listing.
Price: Extracted from an <h3> tag with the class e6r213i1 ooa-1n2paoq er34gjf0.
Details: Found in a <p> tag with the class ewg8vos8, containing mileage, year, etc.
Location and Date: Extracted from a <p> tag with the class ooa-gmxnzj.
Image URL: Located in an <img> tag within the listing.
File Overview:
scraper.py: The main script for scraping car listings and saving the data to a JSON file.
How to Use:
Clone the repository.
Install the required Python libraries:
bash
Copiază codul
pip install requests beautifulsoup4
Run the scraper script to fetch car listings:
bash
Copiază codul
python scraper.py
This will:
Generate a JSON file (autovit_listings.json) containing the extracted data.
Save car images in the autovit_images directory.
Requirements:
Python 3.7 or higher
Required libraries:
requests
beautifulsoup4
Usage Notes:
Ensure the target website (Autovit.ro) is accessible from your network.
Update the HEADERS field if needed to avoid being blocked by the website.
The scraper depends on the current HTML structure of Autovit.ro. If the structure changes, the selectors in the code will need to be updated.
Contribution:
Feel free to fork this repository, submit issues, or create pull requests to improve functionality or add new features.
