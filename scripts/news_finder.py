import datetime

print("=" * 50)
print("GLOBAL VIRAL REPORT AI")
print("=" * 50)

today = datetime.date.today()

countries = [
    "Australia",
    "USA",
    "Canada",
    "UK",
    "Germany"
]

for country in countries:
    print(f"Checking {country}...")

print()
print("News Finder Finished")
print("Date:", today)
