import json
import requests
import urllib3



response = requests.get("https://api.covid19india.org/v4/min/data.min.json")
covid_data = json.loads(response.text)

#  data store in covid_data variable

print("State",'\t', "Active Cases")
print("___________")
for i,j in covid_data.items():
  confirm = j["total"]["confirmed"]
  recover = j["total"]["recovered"]
  decease = j["total"]["deceased"]

  # Active cases = confirmed - (recovered+deceased+others)
  
  infected = recover+decease
  active = confirm-infected
  print(i,'\t', active)

