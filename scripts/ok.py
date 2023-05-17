import requests

url = "https://aircraftscatter.p.rapidapi.com/lat/51.533/lon/-0.0926/"

headers = {
	"X-RapidAPI-Key": "dc9610a994msh74a0267f2436692p193bc2jsnfd301ab70d9d",
	"X-RapidAPI-Host": "aircraftscatter.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
