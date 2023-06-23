# import requests
# import bs4
# import csv
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import json

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



# via Selenium

# driver_path = r'C:\Users\User\OneDrive\Documents\chromedriver_win32 (1)\chromedriver'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.maximize_window()
# # Open Google search
# driver.get('https://www.google.com')


# # Find the search input element and enter the query
# search_input = driver.find_element(By.NAME,'q')

# search_input.send_keys('youtube.com openinapp.co')
# time.sleep(4)
# search_input.send_keys(Keys.RETURN)
# time.sleep(15)
# driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
# time.sleep(4)

# # Collect the YouTube links
# links = []
# channel = []
# count = 10000


# while len(links) <=10000: 
#     try:
#         urls = driver.find_elements(By.XPATH,"//div[@class='DhN8Cf']//a")
#         for url in urls:
#             href = url.get_attribute("href")
#             if href.startswith("https://www.youtube.com/"):
#                     links.append(href)  
#     except:
#         continue
        
#     try:
#         next_page = driver.find_element(By.ID,'pnnext')
#         next_page.click()
#     except:
#         print("No more pages left")
#         break

        
# for j in links:
#     driver.get(j)
#     time.sleep(5)
#     try:
#         cha = driver.find_element(By.XPATH,'//*[@id="text"]/a')
#         channel.append(cha.get_attribute("href"))
#     except:
#         channel.append("NA")
        
# # Close the driver

# driver.quit()

# # Save the links in JSON format
# data = {'links': links, 'channel links' : channel}
# with open('youtube_links.json', 'w') as f:
#     json.dump(data, f)
        
# #csv format
# youtube_df =  pd.DataFrame(list(zip(links,channel)))
# youtube_df.columns =['LINKS','CHANNEL LINKS']
# youtube_df.to_csv(r"C:\Users\User\OneDrive\Desktop\New folder\youtube_csv.csv")


