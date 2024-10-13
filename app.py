from flask import Flask, request, jsonify
from flask_cors import CORS
from crew import HalloweenPartyCrew
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/plan-halloween', methods=['POST'])
def plan_halloween():
    # Log input
    input_data = request.json
    log_to_file(input_data, 'input_log.json')
    
    # Process the request
    out_dates = input_data.get('out_dates')
    num_people = input_data.get('num_people')
    interests = input_data.get('interests')
    location = input_data.get('location')
    age = input_data.get('age')
    budget = input_data.get('budget')

    inputs = {
        'out_dates': out_dates,
        'num_people': num_people,
        'interests': interests,
        'location': location,
        'age': age,
        'budget': budget
    }

    crew = HalloweenPartyCrew().crew().kickoff(inputs=inputs)
    crew_output = crew.dict()

    # Log output
    log_to_file(crew_output, 'output_log.json')

    return jsonify(crew_output)

def log_to_file(data, filename):
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    with open(filename, 'a') as f:
        json.dump(log_entry, f, indent=2)
        f.write('\n')  # Add newline for readability between entries

if __name__ == '__main__':
    app.run(debug=True, port=3002)
