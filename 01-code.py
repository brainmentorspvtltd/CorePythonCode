import bs4
import urllib.request as url
import requests

path = "https://www.flipkart.com/search?q=iphone+12"
# response = url.urlopen(path)
response = requests.get(path, proxies={"http":"proxy_url"})
page = bs4.BeautifulSoup(response,"html.parser")
title = page.find('div', {"class":"_4rR01T"})
price = page.find('div', class_='_30jeq3 _1_WHN1')
print(title.text)
print(price.text)
