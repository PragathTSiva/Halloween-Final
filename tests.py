import requests
import json

# URL of your Flask server
url = 'http://localhost:3001/plan-halloween'

# Sample data to send in the POST request
data = {
    'out_dates': ['2024-10-24', '2024-10-25', '2024-10-26', '2024-10-27'],
    'num_people': 4,
    'interests': ['Basketball', 'Rainbow Six Siege', 'Mcdonalds Food', 'Gambling'],
    'location': 'University of Illinois at Urbana-Champaign',
    'age': 21,
    'budget': 500
}

# Send POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the response JSON
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)

