# import requests
# import bs4
# import csv


# text = "site:youtube.com+openinapp.co"
# num_page_results = 200
# url = f'https://google.com/search?q={text}&num={num_page_results}'
# request_result=requests.get(url)

# soup = bs4.BeautifulSoup(request_result.text,"html.parser")
# heading_object=soup.find_all( 'h3' )

# data = []
# for heading in heading_object:
#     title = heading.getText()
#     link = heading.find_parent('a')['href']
#     data.append({'Title': title, 'Link': link})

# for info in heading_object[:2]:
#     print(info.getText())
#     print("------")

# print (len(data))


import requests
import bs4
import csv

search_query = "bleh"
results_per_page = 100
total_results = 300
num_pages = (total_results + results_per_page - 1) // results_per_page

channels = [] 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

for page in range(num_pages):
    start = page * results_per_page
    url = f'https://www.google.com/search?q={search_query}&num={results_per_page}&start={start}&filter=0'
    request_result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    heading_objects = soup.find_all('h3')
    for heading in heading_objects:
        # link = heading.find_parent('a')['href']
        # channels.append(link)  # Append each link to the list
        channel_div = heading.find_next('div', class_='BNeawe UPmit AP7Wnd')
        channel_name = channel_div.text
        channel_link = channel_div.find_next('a')['href']
        channels.append({'Channel Name': channel_name, 'Channel Link': channel_link})  # Append channel info to the list

# Save the channels to a CSV file
filename = 'channels.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Channel Name', 'Channel Link'])
    writer.writeheader()
    writer.writerows(channels)

print(f"Channels saved to {filename}")

# Print the length of the links list
print("Total links:", len(channels))



