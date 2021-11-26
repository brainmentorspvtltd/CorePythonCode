import json
import urllib.request as url

city = input("Enter city name : ")

api_key = "83e01e3dce5d28839bb5a177cb51af12"
path = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = url.urlopen(path)
data = json.load(response)
print(data)
