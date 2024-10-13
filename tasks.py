from crewai import Task
from typing import List, Dict
import models

class HalloweenPlannerTasks:
    def __init__(self, tasks_config, agents):
        self.tasks_config = tasks_config
        self.agents = agents

    def generate_costume_ideas_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_costume_ideas_task'],
            agent=self.agents.costume_idea_generator(),
        )

    def find_costume_items_task(self) -> Task:
        return Task(
            config=self.tasks_config['find_costume_items_task'],
            agent=self.agents.costume_shopper(),
            output_json=models.HalloweenCostumePlan    
        )
    

    def find_parties_task(self) -> Task:
        return Task(
            config=self.tasks_config['find_parties_task'],
            agent=self.agents.party_finder(),
        )

    def research_party_tickets_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_party_tickets_task'],
            agent=self.agents.ticket_researcher(),
            output_json=models.HalloweenPartyPlan
        )
