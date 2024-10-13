# Halloween Party Planner
![image](https://github.com/user-attachments/assets/dee9554e-f48c-42fb-8b4a-9cf8fd74e974)
![image](https://github.com/user-attachments/assets/91d1131f-b7af-412e-8048-bc2928c0e835)
A comprehensive tool to plan Halloween group costumes and find parties based on user preferences.

## Features

- Generate creative group costume ideas
- Find and link to purchase costume items
- Locate suitable Halloween parties based on specific dates and interests
- Research ticket prices and purchasing information for parties
- Compile all information into a cohesive Halloween plan with a day-by-day itinerary

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/halloween-party-planner.git
cd halloween-party-planner
text

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
text

3. Install required packages:

pip install -r requirements.txt
text

4. Set up your .env file:
Create a `.env` file in the root directory and add your API keys:

SERPER_API_KEY=your_serper_api_key_here

OPENAI_API_KEY=your_open_api_key_here
text

## Usage

1. Run the Flask application:

python app.py

2. Access the application at `http://localhost:3001`

3. Use the API endpoint `/plan-halloween` with a POST request containing the following JSON structure:
``json
{
  "num_people": 4,
  "out_dates": {"Thursday": "2024-10-10", "Friday": "2024-10-11"},
  "interests": ["horror movies", "video games", "superheroes"],
  "location": "New York City",
  "age": 21,
  "budget": 500
}

4. The application will return a comprehensive Halloween plan including costume ideas, party suggestions, and a day-by-day itinerary.

##Project Structure:

1. main.py: Contains the main logic for the Halloween Planner Crew

2. agents.py: Defines the AI agents used in the planning process

3. tasks.py: Specifies the tasks performed by each agent

4. models.py: Defines the data models used in the application

5. app.py: Flask application for API access

6. config/: Contains configuration files

7. agents.yaml: Configuration for AI agents

8. tasks.yaml: Configuration for tasks

##Configuration

1. The project uses YAML files for configuration. You can modify the behavior of agents and tasks by editing the files in the config/ directory.
agents.yaml

2. This file defines the roles, goals, and backstories for each AI agent used in the planning process.
tasks.yaml

3. This file specifies the descriptions and expected outputs for each task in the planning process.
API Reference

POST /plan-halloween
Plan a Halloween party and get costume ideas.
Request Body:
json
{
  "num_people": integer,
  "out_dates": object,
  "interests": array,
  "location": string,
  "age": integer,
  "budget": integer
}

Response:
json
{
  "parties": object,
  "costumes": object
}

##Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


This README is now formatted for easy copying and pasting into a GitHub repository. It includes all the necessary sections typically found in a comprehensive README file, including installation instructions, usage guide, project structure, configuration details, API reference, contribution guidelines, and license information.

Remember to replace "yourusername" in the clone URL with your actual GitHub username or the correct repository URL. Also, make sure to include a `requirements.txt` file in your project with all the necessary dependencies, and create a `LICENSE` file if you haven't already.
