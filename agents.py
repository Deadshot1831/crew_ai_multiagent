from crewai import Agent
from tools import yt_tool


##Create a senior blog content researcher

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal ='get the relevant video content for the topic{topic} from youtube channel',
    verbose= True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science , Machine Learning And Gen AI and providing solution"

    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True,
)
## Create a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Write the blog on the topic {topic} from the content provided by the researcher',
    verbose=True,
    memory=True,
    backstory= (
        """
        Expert in writing blogs in AI Data Science, Machine Learning And Gen AI and providing solution
        
        """
        ),
    tools=[],
    allow_delegation=False,
)