from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_date_and_time() -> dict:
    """Returns the current date and time in a dictionary format"""
    from datetime import datetime
    now = datetime.now()
    return {
        "date_and_time"  : now.strftime(" %d / %m / %Y %H:%M:%S"),
    }
def get_randomuser_from_randomuserme() -> dict:
    """Returns a random user's name, phone number and email from randomuser.me API"""
    import requests
    response = requests.get("https://randomuser.me/api/")
    if response.status_code==200:
        user=response.json()
    else:
        return {"error" : "Failed to fetch data from randomuser.me"}


root_agent = Agent(
    name = "tools_agent",
    description="An agent that can use Google Search",
    tools = [get_current_date_and_time],
    model = "gemini-2.5-flash",
    instruction="""
    """
)