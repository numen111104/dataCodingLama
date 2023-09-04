import requests
url ="https://api-xyz.com/trueid/mobilelegends/?id=960207848&zone=12821"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)