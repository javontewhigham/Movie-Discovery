### Description of project:
+ This project is a movie explorer web app. Upon loading, a login/signup page appears so that returning/new users can login/create an account. This method is authenticated by adding usernames to a database when a user signs up and querying it to when a user logs in to see if the database contains that username. Upon login, the app randomly picks a movie from a hard coded list of &apos;movie ids&apos; and uses an online movie database to search for that movie by it&apos;s id and fetch particular data about it (the only movies used for this project are the 8 live action Spider Man movies). It  pulls data for a movie&apos;s title, tagline, classified genres, and poster image and displays them on the web app. The web app also includes a link to that movie&apos;s Wikipedia page. At the bottom of the page is a review section so that users may leave ratings and comments about the appeared movie and review history showing all reviews posted in the past by other users. For every time you refresh the page, the program randomly picks a movie from the list of movie ids and displays that movie&apos;s title, tagline, classified genres, poster image, Wikipedia link, and review history.

### Technologies used:
+ Python (via VSCode)
+ HTML
+ CSS
+ TMDB API (The Movie Database)
+ WikiMedia API (Wikipedia)
+ Heroku (for deployment)
+ Flask
+ PostgreSQL
+ Flask-SQLAlchemy
+ HTML Forms
+ Flask-Login

### How to run program locally:
+ Clone repository to local environment
+ Install WSL
+ Run the following commands in terminal to install Python and  frameworks used for project:
	+ `sudo apt-get update`
	+ `sudo apt install python3-pip`
	+ `pip3 install flask`
	+ `pip3 install requests`
	+ `pip3 install python-dotenv`
	+ `sudo apt install postgresql`
	+ `sudo service postgresql start`
	+ `sudo -u postgres psql`
	+ `pip3 install psycopg2-binary`
	+ `pip3 install Flask-SQLAlchemy==2.1`
+ Go to https://developers.themoviedb.org/3/getting-started/authentication to receive an API key from TMDB
+ Create a file named .env in the directory with the other files and inside the .env file, put `API_KEY = "{insert your key here}"`
+ Go to https://signup.heroku.com/ to create a Heroku account. In your terminal, run `heroku login -i` and login to Heroku. Next, run `heroku addons:create heroku-postgresql:hobby-dev -a {your-app-name}` to create a remote database
+ Run `heroku config` and copy value for DATABASE_URL and insert into .env file as `export DB_URL = "{database url}"` and replace `postgres:` with `postgresql:`
+ Also in the .env file, create a secret key (any String you want) as `app.secret_key = "{secret key}"`
+ Run the command `python3 app.py` and follow the link in your terminal to run the web app in your local environment

### Known problems that still exist:
+ Certain Wikipedia links will take you to the Wikipedia page for a character/comic book of the same name instead of the movie&apos;s Wikipedia page because the WikiMedia API only searches for pages by a movie&apos;s title and nothing else. For example for the movie &apos;Spider Man&apos;, the Wikipedia link takes you to the Wikipedia page for &apos;the character Spider Man&apos;.
	+ I would address this by trying to use some sort of filter/parameter so that when the WikiMedia API searches for a movie by its title, it only will retrun a link for that movie instead of characters, comic books, etc. with the same name.
+ Sometimes when you refresh the page, the same movie could load twice. This is because there are only 8 movies for the program to choose from, so there is always a 1/8 chance the same movie can be picked randomly again.
	+ I would fix this by just simply increasing the number of movies the program can choose from.

### Technical issues I encountered:
+ One issue I had was trying to display all the genres of a movie on my web app instead of only one of it&apos;s genres.
	+ How I solved the issue: I had to loop through every json response I received for &apos;genre&apos; from the TMDB API call and join them within a list to pass to my web app so it could display all the genres a movie has.
+ Another issue I encountered was trying to use the TMDB API call to fetch a movie&apos;s poster image instead of hard coding it into a list.
	+ How I solved the issue: I had to make an API call to TMDB to receive a json response that contained the poster path for a particular movie. I also had to make another API call to TMDB to receive the base url for the poster path. Once I received both of those, I concatenated them to receive the full poster image to pass to my web app.
+ The next issue I had was trying to have the app keep track of what user was logged in so that it could be displayed if that user left a review.
	+ I solved this issue by simply implementing the Flask login functionality since it has built in methods to keep track and grab the name of the user that&apos;s logged in upon request.
+ I also had to deal with how to let the system know what review is associated with which movie.
	+ I solved this by passing the random movie choice id into the html form and grabbing that same value and adding it to a databse along with the current user, rating, and comment.

### Heroku app link
+ [Javonte&apos;s Movie Explorer Web App](https://desolate-island-05503.herokuapp.com/)