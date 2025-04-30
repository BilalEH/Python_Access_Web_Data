import urllib.request
import json

url = input("Enter location: ")

print("Retrieving", url)
response = urllib.request.urlopen(url)
data = response.read().decode()
print("Retrieved", len(data), "characters")

info = json.loads(data)

counts = [item['count'] for item in info['comments']]
print("Count:", len(counts))
print("Sum:", sum(counts))
