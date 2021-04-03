# web-scraping-challenge

This project features a web application that scrapes various websites for data related to the mission to mars and displays the information in a single HTML page.

The initial scraping is done in a Jupyter Notebook in the file ```mission_to_mars.ipynb```, using BeautifulSoup, Pandas and Requests/Splinter. Items being scraped are the latest news title and paragraph text, the current featured Mars image, a table of facts about Mars, and images and names of the four hemispheres of Mars.

The Jupyter notebok is then converted into a Python script called ```scrape_mars.py``` with a function called ```scrape``` that executes all of the scraping code and returns one Python dictionary containing all of the data.

In ```app.py``` a route called ```/scrape``` imports the ```scrape_mars.py``` script and calls the ```scrape``` function. The return value gets stored in Mongo as a Python dictionary.

The root route ```/``` in ```app.py``` queries the Mongo database and passes the Mars data into the template HTML file called ```index.html```. This takes the Mars data dictionary and displays all of the data on the web page.

To use this application, do the following:

1. Clone the repository to your computer.

1. In Visual Studio Code, go to Open Folder and navigate to the root directory of the Repository.

1. Using ```index.html```, open live server.

1. Press the "Scape New Data" button.




