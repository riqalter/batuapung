import requests as req

url = "https://data.riq.my.id/data"

response = req.get(url).json()

# sanitized to just technologies keys
tech_res = response['techologies']

print()
print(tech_res)

# sanitized to just languages keys
lang_res = response['languages']

print()
print(lang_res)