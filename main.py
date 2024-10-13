from crewai import Crew, Process
from agents import HalloweenPlannerAgents
from tasks import HalloweenPlannerTasks
import yaml
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

class HalloweenPlannerCrew:
    def __init__(self):
        self.agents_config = load_config('config/agents.yaml')
        self.tasks_config = load_config('config/tasks.yaml')
        self.agents = HalloweenPlannerAgents(self.agents_config)
        self.tasks = HalloweenPlannerTasks(self.tasks_config, self.agents)

    def costume_crew(self) -> Crew:
        """Creates a Costume Crew"""
        return Crew(
            agents=[
                self.agents.costume_idea_generator(),
                self.agents.costume_shopper(),
            ],
            tasks=[
                self.tasks.generate_costume_ideas_task(),
                self.tasks.find_costume_items_task(),   
            ],
            process=Process.sequential,
            verbose=True,
        )

    def party_crew(self) -> Crew:
        """Creates a Party Crew"""
        return Crew(
            agents=[
                self.agents.party_finder(),
                self.agents.ticket_researcher(),
            ],
            tasks=[
                self.tasks.find_parties_task(),
                self.tasks.research_party_tickets_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )

def run_crew():
    inputs = {
        'out_dates': ['2024-10-24', '2024-10-25', '2024-10-26', '2024-10-27'],
        'num_people': 4,
        'interests': ['Basketball', 'Rainbow Six Siege', 'Mcdonalds Food', 'Gambling'],
        'location': 'University of Illinois at Urbana-Champaign',
        'age': 21,
        'budget': 500
    }

    halloween_planner = HalloweenPlannerCrew()
    costume_results = halloween_planner.costume_crew().kickoff(inputs=inputs)
    party_results = halloween_planner.party_crew().kickoff(inputs=inputs)

    print(f"Costume Results: {costume_results}")
    print(f"Party Results: {party_results}")

if __name__ == "__main__":
    run_crew()