import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/"

# Make an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the page
    html_content = response.text

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the movie entries in the chart
    movie_entries = soup.find_all("td", class_="titleColumn")

    # Open a CSV file for writing
    with open("movies.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["Rank", "Title", "IMDb Rating"])

        # Get the rank of the first movie in the chart
        rank = 1

        # Iterate over the movie entries and write their data to the CSV
        for movie_entry in movie_entries:
            title = movie_entry.find("a").text
            rating_element = movie_entry.find_next("td", class_="ratingColumn").find("strong")
            if rating_element:
                rating = rating_element.text
            else:
                rating = ""
            writer.writerow([rank, title, rating])
            rank += 1

    print("Data saved to movies.csv")
else:
    # The request was not successful, print an error message
    print("Failed to retrieve the page")
