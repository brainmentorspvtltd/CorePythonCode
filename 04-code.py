import bs4
import urllib.request as url

product = input("Enter product name : ")
product = product.replace(" ", "+")

for i in range(1,5):
    print("Fetching Data From Page",i)
    path = f"https://www.flipkart.com/search?q={product}&page={i}"
    response = url.urlopen(path)
    page = bs4.BeautifulSoup(response,"html.parser")
    titleList = page.find_all('div', {"class" : "_4rR01T"})
    priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')
    # print(titleList.text)
    # print(priceList.text)
    for j in range(len(priceList)):
        print(titleList[j].text)
        print(priceList[j].text)
        print("======================")
