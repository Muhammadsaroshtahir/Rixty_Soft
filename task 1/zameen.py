import requests
from bs4 import BeautifulSoup

def scrape_rentals(base_url, num_pages=5):
    # Loop through each page and collect data
    for page in range(1, num_pages + 1):
        # Update URL for the current page
        url = f"{base_url}-{page}.html"
        response = requests.get(url)
        
        # Check if the page was retrieved successfully
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.find(id="body-wrapper")

            # Extract data
            # Page Titles
            page_titles = result.find_all(class_="_76809701")
            for title in page_titles:
                print(title.get_text())

            # Links
            for link in soup.find_all("a"):
                print(link.get("href"))
            print(link.get_text() if link else "No link text available")

            # Images
            for img in soup.find_all("img"):
                print(img.get("src"))
            print(img.get("alt") if img else "No image alt text available")

            # Details
            details = result.find_all(class_="_5b98ebdf")
            for detail in details:
                print(detail.get_text())

            # Prices
            a_prices = result.find_all(class_="dc381b54")
            for price in a_prices:
                print(price.get_text())

            # Additional Information
            info = result.find_all(class_="d3b6a76b _43afd188")
            for data in info:
                print(data.get_text())
            
            print(f"\n--- End of page {page} ---\n")

        else:
            print(f"Failed to retrieve page {page}")

# Usage example
base_url = "https://www.zameen.com/Rentals/Lahore_Johar_Town-93"
scrape_rentals(base_url, num_pages=5)
