from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

## Reserach Task
research_task = Task(
    description =(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 Paragraph long report based on the topic{topic} of the video',
    tools=[yt_tool],
    agent=[blog_researcher],
    
)
# Writing Task with language model configuration
write_task= Task(
    description ="""
    Write a comprehensive blog on the given topic {topic} and create the content for the blog
    
    """,
    expected_output='A comprehensive blog on the given topic {topic}',
    tools=[yt_tool],
    agents=[blog_writer],
    async_execution=False,
    output_file='blog.md',
    )

        