from google.adk.agents import Agent
from google.adk.tools import google_search
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that will answer user query.',
    instruction=""" You are AI assistant that provide users information based on their queries
                """,
    tools= [google_search]
)
