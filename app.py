import flask
import os
from tmdb import get_movie_data
from wiki import get_wiki_data

app = flask.Flask(__name__)

@app.route("/")
def index():
    movie_id = [557, 558, 559, 1930, 102382, 315635, 429617, 634649]
    
    movie_data = get_movie_data(movie_id)
    title_params = movie_data['title']
    wiki_data = get_wiki_data(title_params)
    
    return flask.render_template(
        "index.html",
        title = movie_data['title'],
        tagline = movie_data['tagline'], 
        genre = movie_data['genre'],
        image = movie_data['image_url'],
        link = wiki_data
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    )