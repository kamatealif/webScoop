import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re




def sanitized_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '', filename).replace(' ', '_')

def download_image(image_url, filename):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()

        with open(filename, 'ab') as file:
            for chunk in response.iter_content(chunk_size = 1024):
                file.write(chunk)

    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

def scrape_and_download_images(base_url, image_dir, target_count=20, count=0):
    url = base_url;
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('article.product_pod')

    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    for book in books:
        title = book.h3.a['title']
        relative_image_url = book.find('img')['src']
        image_url = urljoin(base_url, relative_image_url)
        print(f"url: {image_url}")

        filename = sanitized_filename(title) + ".jpg"
        filepath = os.path.join(image_dir, filename)

        print(f"Filepath: {filepath}")
        print(f"Downloading image for book: {title} from {image_url}")
        download_image(image_url, filename=filepath)
        print()

        count += 1
        print(f"Downloaded {count} books so far...")
        if count >= target_count:
            break

    print(f"Downloaded {count} images to {image_dir}")
    next_link = soup.select_one('li.next > a')
    next_url = urljoin(base_url, next_link.get('href')) if next_link else None

    if next_url and count < target_count:
        print(f"Next page URL: {next_url}")
        scrape_and_download_images(next_url, image_dir, target_count, count)
    else:
        print("No more pages to scrape or target count reached.")

    print("Image scraping completed.")
    current_url = next_url

if __name__ == "__main__":
    BASE_URL = "https://books.toscrape.com/"
    IMAGE_DIR = 'images'
    TARGET_COUNT = int(input("Enter the number of books to scrape images for: "))

    scrape_and_download_images(BASE_URL, IMAGE_DIR, TARGET_COUNT)