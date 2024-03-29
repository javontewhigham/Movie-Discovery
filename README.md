### Description of project:
+ This project is a movie explorer web app. Upon loading, a login/signup page appears so that new/returning users can login/sign up. This method is authenticated by adding the usernames to a database when a user signs up and querying it when a user logs in to see if it already exists. Upon login, the app randomly picks a movie from a hard coded list of &apos;movie ids&apos; and uses an online movie database to search for that movie by it&apos;s id and fetch particular data about it. It pulls the movie&apos;s title, tagline, classified genres, and poster image and displays them onto the web app. The web app also includes a link to the movie&apos;s Wikipedia page. At the bottom of the page, there is a review section so that users may leave ratings and comments about the appeared movie. Review history is also shown, showing all the reviews others have left in the past. Every time you refresh the page, the program randomly picks another movie from the list and displays the new movie&apos;s title, tagline, classified genres, poster image, Wikipedia link, and review history.

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
	+ `pip3 install flask-login`
+ Go to https://developers.themoviedb.org/3/getting-started/authentication to receive an API key from TMDB
+ Create a file named .env in the directory with the other files and inside the .env file, put `API_KEY = "{insert your key here}"`
+ Go to https://signup.heroku.com/ to create a Heroku account. In your terminal, run `heroku login -i` and login to Heroku. Next, run `heroku addons:create heroku-postgresql:hobby-dev -a {your-app-name}` to create a remote database
+ Run `heroku config` and copy value for DATABASE_URL and insert into .env file as `export DB_URL = "{database url}"` and replace `postgres:` with `postgresql:`
+ Also in the .env file, create a secret key (any String you want) as `app.secret_key = "{secret key}"`
+ Run the command `python3 app.py` and follow the link in your terminal to run the web app in your local environment
