from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List, Optional

class IndividualCostume(BaseModel):
    character: str = Field(..., description="The specific character or role for this costume")
    description: str = Field(..., description="Brief description of the individual costume")

class CostumeIdea(BaseModel):
    theme: str = Field(..., description="The group costume theme")
    description: str = Field(..., description="Description of the overall costume idea")
    costumes: List[IndividualCostume] = Field(..., description="List of individual costumes for each person")

class Party(BaseModel):
    name: str = Field(..., description="Name of the party")
    date: str = Field(..., description="Date of the party")
    time: str = Field(..., description="Time of the party")
    location: str = Field(..., description="Location of the party")
    description: str = Field(..., description="Description of the party")

class DayPlan(BaseModel):
    date: str = Field(..., description="The date of the day plan")
    costume_idea: CostumeIdea = Field(..., description="The costume idea for the day")
    party: Party = Field(..., description="The party for the day")
    estimated_cost: float = Field(..., description="Estimated cost for the day")

class Itinerary(BaseModel):
    trip: List[DayPlan] = Field(..., description="The day plans of the trip")

@CrewBase
class HalloweenPartyCrew():
    """Halloween Party Crew - Plans an itinerary for Halloween parties geared towards college students."""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def group_costume_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['group_costume_planner'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def party_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['party_finder'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @agent
    def itinerary_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_compiler'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
        )
    
    @task
    def group_costume_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['group_costume_planning_task'],
            agent=self.group_costume_planner(),
        )
    
    @task
    def party_finding_task(self) -> Task:
        return Task(
            config=self.tasks_config['party_finding_task'],
            agent=self.party_finder(),
        )
    
    @task
    def itinerary_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_compilation_task'],
            agent=self.itinerary_compiler(),
            output_json=Itinerary,
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates a HalloweenParty Crew"""
        return Crew(
            agents=self.agents,
            tasks=[
                self.group_costume_planning_task(),
                self.party_finding_task(),
                self.itinerary_compilation_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
