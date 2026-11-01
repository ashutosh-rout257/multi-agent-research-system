from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# Model setup using Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)

# 1st agent - Updated system prompt to guarantee 3 to 5 sources
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="""You are an expert web search agent.
When searching for a topic, you MUST find between 3 to 5 distinct, relevant web sources.
Always output the explicit Title, URL, and key information for each source so downstream agents can cite them."""
    )

# 2nd agent - Updated with explicit instructions to include URL
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt="""You are an expert web reader and scraper agent.
When you select and scrape a web page, your response MUST explicitly include:
1. The exact URL you scraped: 'Source URL: <URL>'
2. The detailed scraped content from that webpage.

Ensure the source URL is clearly stated so the writer can cite it."""
    )

# Writer chain - Updated to format 3-5 clickable markdown links under Sources
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports with clickable source links."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered (includes search results and URLs):
{research}

Structure the report exactly as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (List 3 to 5 actual URLs found in the research context as proper Markdown links in this exact format: 1. [Title of Source](URL))

Be detailed, factual, and professional. Make sure to include 3 to 5 actual hyperlinks found in the research context under Sources."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic chain - Kept completely unchanged
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()