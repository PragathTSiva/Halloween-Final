import requests
import json
import datetime

# URL of your Flask server
url = 'http://localhost:3002/plan-halloween'

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

# Generate a timestamp for the log file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_name = f"api_response_{timestamp}.log"

# Write the raw response text to a log file
with open(log_file_name, 'w', encoding='utf-8') as log_file:
    log_file.write(response.text)

print(f"API response has been written to {log_file_name}")
