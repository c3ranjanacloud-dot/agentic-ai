from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good morning {name}! My mood is amazing. How can I assist you today?"

def evening_greet(name: str) -> str:
    return f"Good evening {name}! My mood is a bit low.How can I assist you today?"
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that will answer user query related to google cloud.',
    instruction=""" You are AI assistant that helps user with google cloud queries.First greet the user based on user's greet and ask for name.
                    If user greets good morning use morning_greet tool.
                    If user greets good evening use evening_greet tool.
                """,
    tools= [morning_greet,evening_greet]
)
