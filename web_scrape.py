import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError 
from dotenv import load_dotenv
import os

load_dotenv() # Loading the environment variables

API_KEY = os.getenv("API_KEY")
API_SERVICE_NAME = "youtube"
API_VERSION = os.getenv("API_VERSION")


def get_channels(query, max_results): # Function to get the Channels
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY) # Initialising the service
    channels = [] # The channels are stored in this array
    next_page_token = None

    while len(channels) < max_results: # Directly checks youtube for the query
        search_response = youtube.search().list(
            q=query,
            type="channel",
            pageToken=next_page_token,
            part="id,snippet",
            maxResults=min(max_results - len(channels), 50)
        ).execute()

        for search_result in search_response.get("items", []): # Stores the result values in variables
            channel_id = search_result["id"]["channelId"]
            channel_title = search_result["snippet"]["title"]
            channel_description = search_result["snippet"]["description"]
            channel_url = f"https://www.youtube.com/channel/{channel_id}"
            channels.append({
                "ChannelName": channel_title,
                "ChannelLink": channel_url
            })

        next_page_token = search_response.get("nextPageToken") #Checks if a next page exists or not
        if not next_page_token:
            break

    return channels

try: # Main stub of the code
    query = "site:youtube.com openinapp.co"
    max_results = 10000
    channels = get_channels(query, max_results) # Function call for channel scraping
except HttpError as e: #Error Handling
    print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
    channels = []

if channels: # Write the channels into a CSV file
    with open("channels.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ChannelName", "ChannelLink"])
        writer.writeheader()
        writer.writerows(channels)
    print(f"Found {len(channels)} channels and saved to channels.csv")
else:
    print("No channels found")
