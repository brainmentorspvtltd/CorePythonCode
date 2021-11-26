import json
import urllib.request as url

response = url.urlopen("https://data.covid19india.org/states_daily.json")
data = json.load(response)
states = data['states_daily']
deceased_cases = []
confirmed_cases = []
recovered_cases = []
for i in range(len(states)):
    if states[i]['status'] == 'Deceased':
        deceased_cases.append(states[i])
    elif states[i]['status'] == 'Confirmed':
        confirmed_cases.append(states[i])
    else:
        recovered_cases.append(states[i])

# stateNames = {"delhi":"dl","rajasthan":"rj","total":"tt"}

print("Confirmed :",confirmed_cases[400]['dl'])
print("Recovered :",recovered_cases[400]['dl'])
print("Deceased :",deceased_cases[400]['dl'])

