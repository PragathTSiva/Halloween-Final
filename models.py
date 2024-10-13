from pydantic import BaseModel, Field
from typing import List, Optional

class CostumeItem(BaseModel):
    name: str = Field(..., description="The name of the individual costume item")
    link: str = Field(..., description="The purchase link for the costume item")
    price: float = Field(..., description="The price of the costume item")

class IndividualCostume(BaseModel):
    character: str = Field(..., description="The character or role in the group costume")
    description: str = Field(..., description="Description of the individual costume")
    items: List[CostumeItem] = Field(..., description="The list of items for this individual costume")
    total_cost: float = Field(..., description="The total cost of the individual costume")

class GroupCostume(BaseModel):
    date: str = Field(..., description="The date for this group costume")
    theme: str = Field(..., description="The theme of the group costume")
    costumes: List[IndividualCostume] = Field(..., description="The list of individual costumes in the group")
    total_cost: float = Field(..., description="The total cost for the entire group costume")

class Party(BaseModel):
    Date: str = Field(..., description="The date of the event")
    Event_name: str = Field(..., description="The name of the event")
    Date_and_time: str = Field(..., description="The date and time of the event")
    Exact_location: str = Field(..., description="The exact location of the event")
    Venue_type: str = Field(..., description="The type of venue for the event")
    Distance_from_campus: float = Field(..., description="The distance from campus in miles")
    Ticket_price: str = Field(..., description="The price range for tickets")
    Where_to_buy_tickets: str = Field(..., description="Where to purchase tickets")
    Special_instructions_or_notes: str = Field(..., description="Any special instructions or notes for the event")

class HalloweenPartyPlan(BaseModel):
    parties: List[Party] = Field(..., description="The list of Halloween parties")

class HalloweenCostumePlan(BaseModel):
    group_costumes: List[GroupCostume] = Field(..., description="A list of group costumes for different dates")