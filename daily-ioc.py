
#Download .csv and save it to path X
import requests

url = 'https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/today.csv'
response = requests.get(url)

if response.status_code == 200:
    with open(r'/home/ioc-bot/Desktop/sikmacun-sec/day.csv', 'w') as f:
        f.write(response.text)
else:
    print(f"HTTP error {response.status_code}")

#extract fourth column (IOCs) from .csv file and save it as day-iocs.txt

import csv
import os

with open(r'/home/ioc-bot/Desktop/sikmacun-sec/day.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ioc_clean = []
    for row in csv_reader:
        if len(row) >= 4:
            ioc_clean.append(row[3].strip())

base_path = os.path.dirname(r'/home/ioc-bot/Desktop/sikmacun-sec/day.csv')
file_path = os.path.join(base_path, 'day-iocs.txt')

with open(file_path, 'w') as txtfile:
    for ioc in ioc_clean:
        txtfile.write(ioc + '\n')

