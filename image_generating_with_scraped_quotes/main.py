import requests
from bs4 import BeautifulSoup
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont


def fetch_quotes(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return


    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.select('div.quote')

    quote_data = []

    for quote in quotes[:5]:
        quote_text = quote.find('span', class_='text').text.strip("“”")
        author = quote.find('small', class_='author').text.strip("“”")
        quote_data.append((quote_text, author))

    return quote_data

def create_image(text, author, index,output_dir):
    width, height = 800, 400
    background_color = "#dc5555"
    text_color = "#ffffff"

    image_frame = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image_frame)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=50)
    author_text = f"- {author}"

    y_text = 60
    x_text = 50
    draw.text((x_text, y_text), wrapped_text, fill=text_color, font=font)
    y_text += wrapped_text.count('\n')*16 + 40
    draw.text((500, y_text), author_text, fill=text_color, font=author_font)

    # save image
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    filename = os.path.join(output_dir, f"quote_{index + 1}.png")
    image_frame.save(filename)

    print(f"✅ Image saved: {filename}")
def main():
    BASE_URL = "https://quotes.toscrape.com/"
    OUTPUT_DIR = 'quotes'

    qauotes =fetch_quotes(BASE_URL)

    for index, (text, author) in enumerate(qauotes):
        create_image(text, author, index, OUTPUT_DIR)

    print("All images created successfully!")




if __name__ == "__main__":
    main()
