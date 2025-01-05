# Autovit Scraper

This Python project scrapes car listing details from [Autovit.ro](https://www.autovit.ro) and saves them in a structured format. The scraper is designed to extract important metadata from car ads, including images, and store them locally for further analysis or use.

## Features

### 🔍 **Scrapes Car Listings**
- Extracts key details:
  - **Title**: Name of the car listing.
  - **Price**: Extracted directly from the ad.
  - **Year**: Year of manufacture.
  - **Mileage**: Total kilometers driven.
  - **Location**: Where the car is listed.
  - **Image URL**: Downloads the car's image locally.

### 📂 **Data Storage**
- Stores the scraped data in a structured JSON file (`autovit_listings.json`).
- Saves images locally in a directory (`autovit_images`).

### ⚙️ **Configurable**
- Customize:
  - Filters (e.g., price limit).
  - Maximum number of listings to scrape (`MAX_LISTINGS`).

### 🛠 **HTML Structure for Extraction**
The scraper works by targeting specific HTML elements on the [Autovit.ro](https://www.autovit.ro) website. Key elements include:
- **Listing Container**: Each car ad is wrapped in an `<article>` tag with the class `ooa-1yux8sr`.
- **Title**: Found within an `<h2>` tag.
- **Price**: Located inside an `<h3>` tag with the class `e6r213i1 ooa-1n2paoq er34gjf0`.
- **Details**: Mileage and year are stored in a `<p>` tag with the class `ewg8vos8`.
- **Location**: Found in a `<p>` tag with the class `ooa-gmxnzj`.
- **Image**: URL of the car's image is in an `<img>` tag.

## Getting Started

### 🧰 **Requirements**
- Python 3.7 or higher
- Required libraries:
  - `requests`
  - `beautifulsoup4`

### 📥 **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/autovit_scraper.git
   cd autovit_scraper
   ```
2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

### 🚀 **Usage**
1. Run the scraper script:
   ```bash
   python scraper.py
   ```
   - This will fetch car listings, save images to the `autovit_images` directory, and generate the JSON file `autovit_listings.json`.

2. Access the results:
   - View the structured JSON file containing all extracted details.
   - Use the images saved in the `autovit_images` directory.

### ⚠️ **Notes**
- Ensure the website [Autovit.ro](https://www.autovit.ro) is accessible from your network.
- If the website's HTML structure changes, update the selectors in the script to match the new structure.
- The scraper is intended for educational purposes and must comply with the website's terms of service.

## Example JSON Output
Here’s an example of the generated JSON file:

```json
[
    {
        "Link": "https://www.autovit.ro/autoturisme/anunt/peugeot-5008-ID7HuVH7.html",
        "Summary": "Peugeot 5008",
        "Price": "6,999 EUR",
        "Year": "2015",
        "Mileage": "215,000 km",
        "Location": "Timișoara (Timiș)",
        "Image": "autovit_images/image_1.jpg"
    }
]
```

## Contribution
Feel free to fork this repository, submit issues, or create pull requests to improve functionality or add new features.

---
