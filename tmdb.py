import requests
import os
from dotenv import find_dotenv, load_dotenv
import random

load_dotenv(find_dotenv())

MOVIE_BASE_URL = "https://api.themoviedb.org/3/movie/"
IMAGE_BASE_URL = "https://api.themoviedb.org/3/configuration"
movie_dict = {}

def get_movie_data(movie_id):
    query_params = {
        "api_key": os.getenv("API_KEY")
    }

    movie_response = requests.get(
        MOVIE_BASE_URL + str(random.choice(movie_id)),
        params= query_params
    )

    image_response = requests.get(
        IMAGE_BASE_URL,
        params= query_params
    )

    movie_dict["title"] = movie_response.json()["original_title"]
    movie_dict["tagline"] = movie_response.json()["tagline"]

    genre_base = movie_response.json()["genres"]
    genre = []
    for i in range(len(genre_base)):
        genre.append(genre_base[i]["name"])
    movie_dict["genre"] = ", ".join(genre)

    image = image_response.json()["images"]["base_url"]
    poster_path = movie_response.json()["poster_path"]
    movie_dict["image_url"] = image + "original" + poster_path
    
    return movie_dict