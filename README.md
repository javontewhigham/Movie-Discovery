### Description of project:
+ This project is a movie explorer web app. It randomly picks a movie from a hard coded list of &apos;movie ids&apos; and uses an online movie database to search for that movie by it&apos;s id and fetch particular data about it (the only movies used for this project are the 8 live action Spider Man movies). It  pulls data for a movie&apos;s title, tagline, classified genres, and poster image and displays them on the web app. The web app also includes a link to that movie&apos;s Wikipedia page. For every time you refresh the page, the program randomly picks a movie from the list of movie ids and displays that movie&apos;s title, tagline, classified genres, poster image, and Wikipedia link.

### Technologies used:
+ Python (via VSCode)
+ HTML
+ CSS
+ TMDB API (The Movie Database)
+ WikiMedia API (Wikipedia)
+ Heroku (for deployment)
+ Flask (framework)

### How to run program locally:
+ Clone repository to local environment
+ Install WSL
+ Run the following commands in terminal to install Python and  frameworks used for project:
	+ `sudo apt-get update`
	+ `sudo apt install python3-pip`
	+ `pip3 install flask`
	+ `pip3 install requests`
	+ `pip3 install python-dotenv`
+ Go to https://developers.themoviedb.org/3/getting-started/authentication to receive an API key from TMDB
+ Create a file named .env in the directory with  the other files
+ Inside the .env file, put `API_KEY = "{insert your key here}"` and save the file
+ Run the command `python3 app.py` and follow the link in your terminal to run the web app in your local environment

### Known problems that still exist:
+ Certain Wikipedia links will take you to the Wikipedia page for a character/comic book of the same name instead of the movie&apos;s Wikipedia page because the WikiMedia API only searches for pages by a movie&apos;s title and nothing else. For example for the movie &apos;Spider Man&apos;, the Wikipedia link takes you to the Wikipedia page for &apos;the character Spider Man&apos;.
	+ I would address this by trying to use some sort of filter/parameter so that when the WikiMedia API searches for a movie by its title, it only will retrun a link for that movie instead of characters, comic books, etc. with the same name.
+ Sometimes when you refresh the page, the same movie could load twice. This is because there are only 8 movies for the program to choose from, so there is always a 1/8 chance the same movie can be picked randomly again.
	+ I would fix this by just simply increasing the number of movies the program can choose from.

### Technical issues I encountered:
+ One issue I had was trying to display all the genres of a movie on my web app instead of only one of it&apos;s genres.
	+ How I solved the issue: I had to loop through every json response I received for &apos;genre&apos; from the TMDB API call and join them within a list to pass to my web app so it could display all the genres a movie has.
+ Another issue I had was trying to use the TMDB API call to fetch a movie&apos;s poster image instead of hard coding it into my code.
	+ How I solved the issue: I had to make an API call to TMDB to receive a json response that contained the poster path for a particular movie. I also had to make another API call to TMDB to receive the base url for the poster path. Once I received both of those, I concatenated them to receive the full poster image to pass to my web app.

### Heroku app link
+ [Javonte&apos;s Movie Explorer Web App](https://desolate-island-05503.herokuapp.com/)