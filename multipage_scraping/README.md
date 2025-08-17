# Book Scraper

This project is a simple web scraper for collecting a specified number of books from [Books to Scrape](https://books.toscrape.com/). It scrapes books across pages until the target count is reached and saves the results to a JSON file.

## Features
- Scrapes book title, price, and stock status
- Handles pagination automatically
- Saves results to `books.json`
- Configurable target book count

## Requirements
- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [html5lib](https://pypi.org/project/html5lib/)

## Installation

Install dependencies using [uv](https://github.com/astral-sh/uv) or pip:

```sh
uv sync
# or
pip install -r requirements.txt
```

## Usage
Run the scraper:

```sh
uv run main.py
# or
python main.py
```

The scraped data will be saved in `books.json`.

## Configuration
You can change the number of books to scrape by editing the `TARGET_COUNT` variable in `main.py`.

## Project Structure
- `main.py` - Main scraping script
- `books.json` - Output file with scraped data
- `pyproject.toml`, `uv.lock` - Dependency management files
- `README.md` - Project documentation

## License
This project is for educational purposes only.
