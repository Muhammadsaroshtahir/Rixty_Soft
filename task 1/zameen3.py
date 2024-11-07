import requests
from bs4 import BeautifulSoup
import csv

def scrape_rentals(base_url, num_pages=5):
    # Open the CSV file in write mode
    with open("rentals_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Page", "Title", "Link", "Link Text", "Image Source", "Image Alt Text", "Detail", "Price", "Additional Info"])
        
        for page in range(1, num_pages + 1):
            url = f"{base_url}-{page}.html"
            response = requests.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                result = soup.find(id="body-wrapper")

                # Initialize lists to store data from each section
                page_titles = [title.get_text() for title in result.find_all(class_="_76809701")]
                links = [link.get("href") for link in soup.find_all("a")]
                link_texts = [link.get_text() if link else "No link text available" for link in soup.find_all("a")]
                images_src = [img.get("src") for img in soup.find_all("img")]
                images_alt = [img.get("alt") if img else "No image alt text available" for img in soup.find_all("img")]
                details = [detail.get_text() for detail in result.find_all(class_="_5b98ebdf")]
                prices = [price.get_text() for price in result.find_all(class_="dc381b54")]
                infos = [info.get_text() for info in result.find_all(class_="d3b6a76b _43afd188")]

                # Adjust the length of lists for uniformity in CSV rows
                max_len = max(len(page_titles), len(links), len(link_texts), len(images_src), len(images_alt), len(details), len(prices), len(infos))
                page_titles += [""] * (max_len - len(page_titles))
                links += [""] * (max_len - len(links))
                link_texts += [""] * (max_len - len(link_texts))
                images_src += [""] * (max_len - len(images_src))
                images_alt += [""] * (max_len - len(images_alt))
                details += [""] * (max_len - len(details))
                prices += [""] * (max_len - len(prices))
                infos += [""] * (max_len - len(infos))

                # Write each row of data to the CSV file
                for i in range(max_len):
                    writer.writerow([page, page_titles[i], links[i], link_texts[i], images_src[i], images_alt[i], details[i], prices[i], infos[i]])

                print(f"--- End of page {page} ---\n")
            else:
                print(f"Failed to retrieve page {page}")

# Define the base URL
base_url = "https://www.zameen.com/Rentals/Lahore_Johar_Town-93"
scrape_rentals(base_url, num_pages=5)
