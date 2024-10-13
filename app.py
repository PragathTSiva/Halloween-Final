import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from main import HalloweenPlannerCrew
import logging
from logging.handlers import RotatingFileHandler
import os
import json

app = Flask(__name__)
CORS(app)

# Set up logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

# File Handler
file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=10)
file_handler.setFormatter(log_formatter)

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/plan-halloween', methods=['POST'])
def plan_halloween():
    data = request.json
    out_dates = data.get('out_dates')
    num_people = data.get('num_people')
    interests = data.get('interests')
    location = data.get('location')
    age = data.get('age')
    budget = data.get('budget')

    inputs = {}
    inputs['out_dates'] = out_dates
    inputs['num_people'] = num_people
    inputs['interests'] = interests
    inputs['location'] = location
    inputs['age'] = age
    inputs['budget'] = budget

    halloween_planner = HalloweenPlannerCrew()
    costume_crew_output = halloween_planner.costume_crew().kickoff(inputs=inputs)
    party_crew_output = halloween_planner.party_crew().kickoff(inputs=inputs)

    # Log the original outputs
    logging.info(f"Original costume_crew_output: {costume_crew_output}")
    logging.info(f"Original party_crew_output: {party_crew_output}")

    costume_results = costume_crew_output.to_dict()
    party_results = party_crew_output.to_dict()

    # Log the dict conversions
    logging.info(f"Costume results dict: {json.dumps(costume_results, indent=2)}")
    logging.info(f"Party results dict: {json.dumps(party_results, indent=2)}")

    response = jsonify({'costume_results': costume_results, 'party_results': party_results})

    # Log the final jsonified response
    logging.info(f"Final jsonified response: {response.get_data(as_text=True)}")

    return response

if __name__ == '__main__':
    app.run(debug=True, port=3001)
