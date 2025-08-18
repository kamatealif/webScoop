# Image Scraping Project

This project scrapes book cover images from [Books to Scrape](https://books.toscrape.com/) and saves them locally. It uses Python, BeautifulSoup, and Requests.

## Features
- Scrapes book images from multiple pages
- Saves images with sanitized filenames
- User can specify how many images to download

## Installation


1. **Clone the repository** (if needed):

	```sh
	git clone https://github.com/kamatealif/webScoop/tree/main/image_scraping
	cd image_scraping
	```

2. **Install dependencies using [uv](https://github.com/astral-sh/uv):**

	```sh
	uv pip install -r requirements.txt
	```

	Or, if you prefer to use `pyproject.toml`:

	```sh
	uv sync
	```

## Usage

Run the script and enter the number of book images you want to download:


```sh
uv run main.py
```


You will be prompted to enter the number of books to scrape images for. Images will be saved in the `images` directory.


## Requirements
- Python 3.7+
- [uv](https://github.com/astral-sh/uv)
- beautifulsoup4
- requests
- urllib3

## License
MIT
