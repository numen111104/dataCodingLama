import http.client

conn = http.client.HTTPSConnection("api-xyz.com")
payload = ''
headers = {}
conn.request("GET", "/trueid/mobilelegends/?id=366409793&zone=9707", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))