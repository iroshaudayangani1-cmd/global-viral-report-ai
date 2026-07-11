import requests

url = "https://news.google.com/rss"

print("Downloading news...")

response = requests.get(url)

print(response.status_code)
print(response.text[:500])
