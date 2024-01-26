import httpx
from parsel import Selector
from pprint import pprint


MAIN_URL = "https://www.mashina.kg/search/all/"
ORGINAL_URL = "https://www.mashina.kg"

def get_page():
    response = httpx.get(MAIN_URL)
    print("Response", response.status_code, response.url)
    html = Selector(text=response.text)
    return html

def get_title(html: Selector):
    title = html.css("title::text").get()
    print(title)

def get_cars_data(html: Selector):
    cars_links = html.css("div.list-item a::attr(href)").getall()
    # pprint(cars)
    # cars = [f"{ORGINAL_URL}{car}" for car in cars]
    cars = list(map(lambda car: f"{ORGINAL_URL}{car}", cars_links))
    pprint(cars[:3])


if __name__ == "__main__":
    html = get_page()
    get_title(html)
    get_cars_data(html)