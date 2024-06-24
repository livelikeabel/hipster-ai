import os
from crewai import Agent
from crewai_tools import SerperDevTool, BrowserbaseLoadTool, EXASearchTool

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

search_tool = SerperDevTool()
browser_tool = BrowserbaseLoadTool()
exa_search_tool = EXASearchTool()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[search_tool, browser_tool],
)

print(researcher)
