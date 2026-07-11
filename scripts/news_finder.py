import urllib.request
import xml.etree.ElementTree as ET

RSS_URL = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"

print("=" * 60)
print("GLOBAL VIRAL REPORT")
print("Today's Top Headlines")
print("=" * 60)

response = urllib.request.urlopen(RSS_URL)
xml_data = response.read()

root = ET.fromstring(xml_data)

count = 1

for item in root.findall("./channel/item")[:10]:
    title = item.find("title").text
    print(f"{count}. {title}")
    count += 1
