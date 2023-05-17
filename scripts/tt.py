import requests

# Make a GET request to the OpenSky API
response = requests.get('https://opensky-network.org/network/explorer?icao24=40087c&callsign=BAW469&time=1684256755000')

# Check if the request was successful
if response.status_code == 200:
    # Access the response data
    data = response.json()
    # Print the response data
    print(data)
else:
    print('Error:', response.status_code)
