from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

class HalloweenPlannerAgents:
    def __init__(self, agents_config):
        self.agents_config = agents_config

    def costume_idea_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['costume_idea_generator'],
            tools=[],
            verbose=True,
            allow_delegation=False,
            model="gpt-4o" 
        )

    def costume_shopper(self) -> Agent:
        return Agent(
            config=self.agents_config['costume_shopper'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            model="gpt-4o" 
        )
    

    def party_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['party_finder'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            model="gpt-4o" 
        )
    
    def ticket_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['ticket_researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            model="gpt-4o" 
        )    
    