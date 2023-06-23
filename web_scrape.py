import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SERVICE_NAME = "youtube"
API_VERSION = os.getenv("API_VERSION")


def get_channels(api_key, query, max_results):
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)
    channels = []
    next_page_token = None

    while len(channels) < max_results:
        search_response = youtube.search().list(
            q=query,
            type="channel",
            pageToken=next_page_token,
            part="id,snippet",
            maxResults=min(max_results - len(channels), 50)
        ).execute()

        for search_result in search_response.get("items", []):
            channel_id = search_result["id"]["channelId"]
            channel_title = search_result["snippet"]["title"]
            channel_description = search_result["snippet"]["description"]
            channel_url = f"https://www.youtube.com/channel/{channel_id}"
            channels.append({
                "ChannelName": channel_title,
                "ChannelLink": channel_url
            })

        next_page_token = search_response.get("nextPageToken")
        if not next_page_token:
            break

    return channels

try:
    query = "site:youtube.com openinapp.co"
    max_results = 10000
    channels = get_channels(API_KEY, query, max_results)
except HttpError as e:
    print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
    channels = []

if channels:
    with open("channels.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ChannelName", "ChannelLink"])
        writer.writeheader()
        writer.writerows(channels)
    print(f"Found {len(channels)} channels and saved to channels.csv")
else:
    print("No channels found")