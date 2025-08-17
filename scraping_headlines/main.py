import requests
from bs4 import BeautifulSoup


def get_all_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    soup = BeautifulSoup(response.text, "html5lib")
    all_h2s = soup.find_all("h2")
    print(f"Found {len(all_h2s)} <h2> headers.")
    for index,h2 in enumerate(all_h2s):
        if index >= 10:
            break;
        print(f"{index+1}. {h2.get_text(strip=True)}")
       


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    get_all_headers(url)
