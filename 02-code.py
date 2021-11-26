import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=iphone+12"
response = url.urlopen(path)
page = bs4.BeautifulSoup(response,"html.parser")
titleList = page.find_all('div', {"class" : "_4rR01T"})
priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')
# print(titleList.text)
# print(priceList.text)
for i in range(len(priceList)):
    print(titleList[i].text)
    print(priceList[i].text)
    print("======================")
