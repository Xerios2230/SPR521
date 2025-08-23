import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.ua/uk/transport/legkovye-avtomobili/"
HOST = "https://www.olx.ua"
CSV = "cars.csv"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

def get_html(url, params=""):
    return requests.get(url, headers=HEADERS, params=params)

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="css-1r93q13")
    cards = []
    for item in items:
        title_item = item.find('h4', class_="css-1g61gc2")
        title = title_item.get_text(strip=True) if title_item else "N/A"

        price_item = item.find('p', class_="css-uj7mm0")
        price = price_item.get_text(strip=True) if price_item else "N/A"

        link_item = item.find('a', class_="css-1tqlkj0")
        link = HOST + link_item.get('href') if link_item else "N/A"

        img_item = item.find('img')
        image = img_item.get('src') if img_item else "N/A"

        details_block = item.find_all('span', class_="css-1l1r91c")

        details = [d.get_text(strip=True) for d in details_block]

        mileage, fuel, transmission = "N/A", "N/A", "N/A"
        for d in details:
            if "км" in d:
                mileage = d
            elif d in ["Бензин", "Дизель", "Газ", "Електро"]:
                fuel = d
            elif d in ["Механічна", "Автомат", "Типтронік", "Робот"]:
                transmission = d

        cards.append({
            "title": title,
            "price": price,
            "link": link,
            "mileage": mileage,
            "fuel": fuel,
            "transmission": transmission,
            "image": image
        })
    return cards


def save_to_csv(cards, path):
    with open(path, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(['Title', 'Price', 'Link', 'Mileage', 'Fuel', 'Transmission', 'Image'])
        for card in cards:
            writer.writerow([
                card['title'],
                card['price'],
                card['link'],
                card['mileage'],
                card['fuel'],
                card['transmission'],
                card['image']
            ])


def parser():
    pagination = int(input("Enter number of pages you want to parse: "))
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, pagination + 1):
            print(f"Parsing page {page}")
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
        save_to_csv(cards, CSV)
        print(f"Done! Saved {len(cards)} cars to {CSV}")
    else:
        print("Error")


parser()