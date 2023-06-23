#Search_Scraper
Scraping n Google searches using the googleapi client and Youtube Data Api as part of a Listed assessment

## To Use
1. Modify the environment variable (.env) using your own API Key and version
2. Run the pip install -r requirements.txt file to install the required libraries
3. You're golden to run the web_scrape.py file in Python

### Current Functionality
1. Searches for a Query as provided in the ```query``` variable.
2. Since the solution is specific to searching Youtube data, it runs the search results via the Youtube Data Api to get info regarding the video.
3. Saves the scraped information to a CSV file (Channels.csv specifically here, as I'm scraping the channels of the videos and its youtube links).

Note#1: This was made using the Youtube Data API. Custom Searches could be made via the Custom Search JSON API or other GData APIs provided by google.
Note#2: The try.py has alternate trials of the code executed via bs4 and selenium as well. Results may not be optimum

