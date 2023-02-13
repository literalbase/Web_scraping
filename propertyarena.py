import requests as rq
from bs4 import *
import os
import re
from csv import writer 


get_request = rq.get('https://www.propertypro.ng/property/3-bedroom-house-for-sale-1004-victoria-island-lagos-6HHMC')

soup = BeautifulSoup(get_request.text  , 'lxml')

with open('propertyarena/first.csv', 'w',encoding='utf8',newline='') as fprop:
    propwriter= writer(fprop) 
    header = ['Title' , 'Location' , 'Price' , 'Description' ,'Contact' ]
    propwriter.writerow(header)

    lists = soup.find_all("div" , class_ = 'duplex-text')
    for list in lists:
        title = list.find('h1').text
        location = list.find('h6').text

    price = soup.find_all("div",  class_ = 'duplex-view-text') 
    for item in price: 
        prop_price = item.find_all('strong')[1].text

    desc = soup.find_all("div",  class_ = 'description-text')  
    for descs in desc:
        prop_desc= descs.find('p').text


    contact = soup.findAll('a' , class_ = 'call-show')
    for con in contact:
        if con.has_attr('href'):
            agent_con = con['href']

    info = [title,location,prop_price,prop_desc,agent_con]

    propwriter.writerow(info)
    # print(info)

## Scraping images from the provided url 
links = []

images = soup.findAll('img' , class_ = "slider-nav-img")
for item in images:
     links.append(item['data-lazy'])

os.mkdir('propertyarena')
i = 1 
for index, img_link in enumerate(links):
    if i <= 10:
        img_data = rq.get(img_link)
        with open('propertyarena/' + str(index + 1)+ '.jpg', 'wb') as  f:
            f.write(img_data.content)   

print('Done')            
    

