import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
request = requests.get(URL,verify=False)

web_site_text = request.text
soup = BeautifulSoup(web_site_text,'html.parser')


movies = [movie_name.text for movie_name in soup.find_all(name="h3", class_="title")]
#print(movies)
movies.reverse()
#print(movies)

with open("list_of_movies.txt","w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(movie + "\n")