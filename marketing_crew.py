from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool
import requests

# Define a tool that inherits from BaseTool
class SearchTool(BaseTool):
    name: str = "Search Tool"  
    description: str = "Performs a search to retrieve relevant information."  

    def _run(self, query: str):
        
        print(f"Performing search for: {query}")
        return {"result": f"Mock results for {query}"}

    async def _arun(self, query: str):
        return self._run(query)

search_tool = SearchTool()

# Define Agents
market_researcher = Agent(
    role='Market Research Specialist',
    goal='Conduct market research for {product/service}.',
    backstory='A skilled researcher passionate about actionable insights.',
    tools=[search_tool]
)

content_creator = Agent(
    role='Content Creator',
    goal='Create engaging content for {product/service}.',
    backstory='A creative professional crafting resonating messages.',
    tools=[search_tool]
)

seo_specialist = Agent(
    role='SEO Specialist',
    goal='Optimize website SEO for {product/service}.',
    backstory='An expert in improving search rankings and organic growth.',
    tools=[search_tool]
)

campaign_manager = Agent(
    role='Campaign Manager',
    goal='Plan and execute campaigns for {product/service}.',
    backstory='A strategist focused on campaign ROI and performance.',
    tools=[search_tool]
)

# Define Tasks
research_task = Task(
    description='Conduct market research for {product/service}.',
    expected_output='A report with market insights, competitor analysis, and recommendations.',
    agent=market_researcher
)

content_task = Task(
    description='Develop a content strategy for {product/service}.',
    expected_output='A structured content plan with blog, social, and video ideas.',
    agent=content_creator
)

seo_task = Task(
    description='Analyze website SEO for {product/service} and suggest improvements.',
    expected_output='A report with SEO recommendations.',
    agent=seo_specialist
)

campaign_task = Task(
    description='Plan and launch an ad campaign for {product/service}.',
    expected_output='A campaign strategy with performance metrics.',
    agent=campaign_manager
)

# Create the Crew
marketing_crew = Crew(
    agents=[market_researcher, content_creator, seo_specialist, campaign_manager],
    tasks=[research_task, content_task, seo_task, campaign_task],
    process=Process.sequential  # Tasks are performed one after another
)

# Kickoff the process
result = marketing_crew.kickoff(inputs={'product/service': 'Eco-friendly Gadgets'})
print(result)




