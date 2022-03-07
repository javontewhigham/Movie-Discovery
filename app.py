import flask
import os
import random
from tmdb import get_movie_data
from wiki import get_wiki_data
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    logout_user,
    current_user,
)

app = flask.Flask(__name__)

load_dotenv(find_dotenv())

app.config["SECRET_KEY"] = os.getenv("app.secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def get_username(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    current_username = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(150), nullable=True)


db.create_all()


@app.route("/")  # Displays login page
def index():
    return flask.render_template(
        "login.html",
    )


@app.route("/login", methods=["GET", "POST"])  # Handles user input for login page
def login():
    if flask.request.method == "POST":
        login_input = flask.request.form.get("username")
        user = User.query.filter_by(
            username=login_input
        ).first()  # If username user inputs is already in database
        if user:
            login_user(user)
            return flask.redirect("/main")  # Redirect them to the main page
        else:
            flask.flash("No account found with that username. Please sign up!")
            return flask.redirect(
                "/signup_form"
            )  # If not, redirect them to the sign up page


@app.route("/signup_form")  # Displays sign up page
def signup_form():
    return flask.render_template(
        "signup.html",
    )


@app.route("/signup", methods=["GET", "POST"])  # Handles user input for sign up page
def signup():
    if flask.request.method == "POST":
        signup_input = flask.request.form.get("username")
        if User.query.filter_by(
            username=signup_input
        ).first():  # If username user inputs is already in database
            flask.flash("Account already exists with this username. Please login!")
            return flask.redirect(
                "/"
            )  # Tell user username already exists and redirect them to the login page
        else:
            db.session.add(User(username=signup_input))
            db.session.commit()
            flask.flash("Account created. Please login!")
            return flask.redirect(
                "/"
            )  # If not, add username to database and redirect user to login page so they can log in with new username


@app.route("/main", methods=["GET", "POST"])  # Displays main page
@login_required  # Redirects user to login page if they try to manually access main page
def main():
    movie_id = [557, 558, 559, 1930, 102382, 315635, 429617, 634649]
    random_movie = random.choice(movie_id)
    movie_data = get_movie_data(random_movie)
    title_params = movie_data["title"]
    wiki_data = get_wiki_data(title_params)
    reviews = Review.query.filter_by(
        movie_id=random_movie
    ).all()  # Gathers all rows who has a movie id value the same as random.choice()
    total_reviews = len(reviews)
    return flask.render_template(
        "index.html",
        title=movie_data["title"],
        tagline=movie_data["tagline"],
        genre=movie_data["genre"],
        image=movie_data["image_url"],
        link=wiki_data,
        random_movie=random_movie,
        reviews=reviews,
        total_reviews=total_reviews,
    )


@app.route("/logout", methods=["GET", "POST"])  # Adds a logout function to main page
@login_required
def logout():
    logout_user()
    return flask.redirect("/")  # Redirects user to login page once they have logged out


@app.route(
    "/review_form", methods=["GET", "POST"]
)  # Handles user input for review section on main page
def review_form():
    if flask.request.method == "POST":
        current_movie = flask.request.form.get("movie_id")
        current_person = current_user.username
        rating_input = flask.request.form.get("rating")
        comment_input = flask.request.form.get("comment")
        db.session.add(
            Review(
                movie_id=current_movie,
                current_username=current_person,
                rating=rating_input,
                comment=comment_input,
            )
        )  # Takes user input from review section and add to database accordingly
        db.session.commit()
        return flask.redirect("/main")  # And redirect user back to main page


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
