import requests
from bs4 import BeautifulSoup
import csv

url = "https://fatmongoose.staging.g2.com/categories/payment-gateways"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

contents = soup.find_all("div", class_="product-card__info")

# Open the CSV file in write mode and write the header row
with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Stars', 'Rating', 'Ranking'])

    # Write each product's information to a new row in the CSV file
    for i in contents:
        name=i.find("a").text
        star_element = i.find("span", class_="px-4th")
        if star_element is not None:
            stars = star_element.text.strip()
        rating_element = i.find("span", class_="fw-semibold")
        if rating_element is not None:
            rating = rating_element.text.strip()
        rank = i.find("div", class_="pl-4th text-sm fw-semibold")
        if rank is not None:
            rnk=rank.text.strip()
        writer.writerow([name, stars, rating, rnk])
