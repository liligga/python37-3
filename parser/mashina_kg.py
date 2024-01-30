import httpx
from parsel import Selector
from pprint import pprint


MAIN_URL = "https://www.mashina.kg/search/all/"
ORGINAL_URL = "https://www.mashina.kg"

def get_page(url):
    response = httpx.get(url)
    print("Response", response.status_code, response.url)
    html = Selector(text=response.text)
    return html

def get_title(html: Selector):
    title = html.css("title::text").get()
    print(title)

def get_cars_links(html: Selector):
    cars_links = html.css("div.list-item a::attr(href)").getall()
    # pprint(cars)
    # cars = [f"{ORGINAL_URL}{car}" for car in cars]
    cars = list(map(lambda car: f"{ORGINAL_URL}{car}", cars_links))
    pprint(cars[:3])

# "www fdfdf rrrr"
def clean_text(text: str|None):
    if text is None:
        return ""
    text = " ".join(text.split())
    return text.strip().replace("\t", "").replace("\n", "")

def get_cars_data(html: Selector):
    cars = html.css("div.list-item a")
    cars_list = []
    for car in cars:
        car_data = {}
        car_data["title"] = clean_text(car.css("h2.name::text").get())
        car_data["price"] = clean_text(car.css("div.price strong::text").get())
        car_data["som_price"] = clean_text(car.css("div.price p::text").getall()[1])
        # car_data["car_description"] = car.css("p.year-miles::text").getall()
        cars_list.append(car_data)
    
    # pprint(cars_list)
    return cars_list

def get_cars():
    cars = []
    for page in range(1, 3):
        url = f"{MAIN_URL}?page={page}"
        html = get_page(url)
        cars.extend(get_cars_data(html))
    # return get_cars_links(html)
    pprint(cars)
    print("Lenght", len(cars))


if __name__ == "__main__":
    # html = get_page(MAIN_URL)
    # get_title(html)
    # get_cars_data(html)
    # get_cars_data(html)
    get_cars()