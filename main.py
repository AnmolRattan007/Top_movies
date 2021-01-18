import requests
from bs4 import BeautifulSoup


movies_data = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

content = movies_data.text


soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movies = [movie.string for movie in titles ]
movies.reverse()
with open("movies.text","w") as file:
    for movie in movies:
        data = f"{movie}\n"
        file.write(data)


