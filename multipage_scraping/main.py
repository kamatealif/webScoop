from bs4 import BeautifulSoup
import requests

import json
from urllib.parse import urljoin
import os



def scrape_book(base_url):
    books = []

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching {base_url}: {e}")
        return [],None
       

        
    soup = BeautifulSoup(response.text, 'html5lib')
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        title_tag = article.select_one('h3 > a')
        title = title_tag.get("title", "No title found")
        price = article.find('p', class_='price_color').text
        in_stock = article.find('p', class_='instock availability').text.strip()
        # book_url = urljoin(base_url, article.find('h3 a')['href'])

        books.append({
            'title' : title,
            'price' : price,
            'in_stock' : in_stock
            # 'url' : book_url
        })

        # print(f"Scraped book: {title} - Price: {price} - In Stock: {in_stock}")
    print(f"Scraped {len(books)} books from {base_url}")

    next_link = soup.select_one('li.next > a')
    next_url = urljoin(base_url, next_link.get('href')) if next_link else None;
    return books, next_url
    

        
if __name__ == "__main__":
    BASE_URL = "https://books.toscrape.com/"
    START_PAGE = "catalogue/page-1.html"
    OUTPUT_FILE = "books.json"
    TARGET_COUNT = int(input("Enter the number of books to scrape: "))

    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)
    # SCRAPE FIRST PAGE BOOKS   
    while current_url and len(collected) < TARGET_COUNT:
        # print(f"Scraping {current_url}")
        books, next_url = scrape_book(current_url)
        collected.extend(books)
        current_url = next_url

    collected = collected[:TARGET_COUNT]  # Limit to TARGET_COUNT books
    print(f"Total books collected: {len(collected)}")

    # save to json file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(collected, f, ensure_ascii=False, indent=4)
            
    print(f"Books saved to {OUTPUT_FILE}")