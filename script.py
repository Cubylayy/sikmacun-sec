
#Download .csv and save it to path C:\Users\PC\Desktop\IOCs\ as week.csv
import requests

url = 'https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/week.csv'
response = requests.get(url)

if response.status_code == 200:
    with open(r'/home/ioc-bot/Desktop/sikmacun-sec/week.csv', 'w') as f:
        f.write(response.text)
else:
    print(f"HTTP error {response.status_code}")


#extract fourth column (IOCs) from .csv file and save it as week-iocs.txt

import csv
import os

with open(r'/home/ioc-bot/Desktop/sikmacun-sec/week.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ioc_clean = []
    for row in csv_reader:
        if len(row) >= 4:
            ioc_clean.append(row[3].strip())

base_path = os.path.dirname(r'/home/ioc-bot/Desktop/sikmacun-sec/week.csv')
file_path = os.path.join(base_path, 'week-iocs.txt')

with open(file_path, 'w') as txtfile:
    for ioc in ioc_clean:
        txtfile.write(ioc + '\n')

