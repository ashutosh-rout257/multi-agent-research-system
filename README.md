# Multi-Agent AI Research Assistant

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LCEL](https://img.shields.io/badge/Pipeline-LCEL-4B8BBE?style=flat-square)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-8A2BE2?style=flat-square)

> A fully autonomous team of AI agents that searches, reads, writes, and critiques to produce a professional research report on any topic.

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f9ed.png" width="28" height="28" align="absmiddle"> Overview <a name="overview"></a>

This project is a **Multi-Agent Research Assistant** — a fully autonomous AI system that thinks, searches, reads, and writes on its own. Instead of a single AI answering your question from memory, a team of specialized intelligent agents collaborate to produce a professional research report on any topic you give them.

Every agent is powered by a Large Language Model (LLM), connected through LangChain's modern LCEL pipeline, and orchestrated through a shared memory system that makes them work as one unified brain.

This is not a chatbot and not a simple Q&A tool — it is a production-level agentic AI system.

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4cc.png" width="28" height="28" align="absmiddle"> Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Methods Used](#methods-used)
- [Key Insights](#key-insights)
- [Models Used](#models-used)
- [Results & Conclusion](#results--conclusion)
- [Author & Contact](#author--contact)

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/2753.png" width="28" height="28" align="absmiddle"> Problem Statement <a name="problem-statement"></a>

A single AI answering from memory can be outdated, shallow, and unverified. The goal of this project is to build a system where multiple specialized agents work together — gathering live information from the internet, extracting meaningful content, writing a structured report, and reviewing its quality — to produce reliable, well-researched output on any topic.

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f5c2.png" width="28" height="28" align="absmiddle"> Dataset <a name="dataset"></a>

- **Type:** No fixed dataset — the system works on live data.
- **Source:** Relevant and recent sources found on the live internet by the Search Agent at runtime.
- **Input:** A research topic given by the user.
- **Output:** A structured, detailed research report.

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f6e0.png" width="28" height="28" align="absmiddle"> Tools & Technologies <a name="tools--technologies"></a>

- **Language:** Python
- **Framework:** LangChain
- **Pipeline:** LCEL (LangChain Expression Language) using `prompt | llm | StrOutputParser()`
- **Agent Engine:** `create_agent()` from `langchain.agents`, powered by LangGraph internally
- **Search API:** Tavily API (live internet search results)
- **Web Scraping:** BeautifulSoup (clean, readable text from web pages)
- **AI Model:** Google Gemini 3.5 Flash-Lite (LLM powering every agent)
- **Frontend:** Streamlit
- **Architecture:** Multi-agent system with shared memory

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/2699.png" width="28" height="28" align="absmiddle"> Methods Used <a name="methods-used"></a>

1. The user provides a research topic.
2. **`tools.py`** — reusable tools defined with the `@tool` decorator:
   - `web_search`: talks to the Tavily API and fetches live search results from the internet
   - `scrape_url`: takes a URL, visits the page, and extracts clean readable text using BeautifulSoup
3. **`agents.py`** — the heart of the project, with 4 components:
   - **Search Agent:** built with `create_agent()` from `langchain.agents` by passing the model and tools; returns a ready-to-use agent graph powered by LangGraph 
   - **Reader Agent:** built with the same `create_agent()` pattern, using the `scrape_url` tool
   - **Writer Chain:** built with LCEL pipe syntax ; takes all the research and writes a full report
   - **Critic Chain:** also built with LCEL pipe syntax; reads the report and gives a score and feedback
4. **`pipeline.py`** — the supervisor:
   - A single function, `run_research_pipeline`, calls all 4 agents and chains in the correct order
   - Results are passed between them using a shared state dictionary
   - Agents use message-based input/output
   

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png" width="28" height="28" align="absmiddle"> Key Insights <a name="key-insights"></a>

- Splitting the work across specialized agents gives each step a clear role, instead of relying on a single AI to do everything.
- Using live internet sources keeps reports relevant and recent, rather than limited to what an AI remembers.
- The Critic Agent adds a review step that works like a senior researcher reviewing a junior's work.
- A shared memory system lets all agents work together as one unified brain.
- The LCEL pipeline connects every agent in a modern, modular way.

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f916.png" width="28" height="28" align="absmiddle"> Models Used <a name="models-used"></a>

Every agent is powered by a Large Language Model (LLM) — the **gemini-3.5-flash-lite**:

- **Search Agent:** Uses the `web_search` tool (Tavily API) to find the most relevant and recent sources on the live internet.
- **Reader Agent:** Uses the `scrape_url` tool (BeautifulSoup) to dive deep into those sources and extract meaningful content.
- **Writer Chain:** Takes all the gathered research and writes a well-structured, detailed report (LCEL pipeline).
- **Critic Chain:** Reads the report, then gives a score and feedback (LCEL pipeline).

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ca.png" width="28" height="28" align="absmiddle"> Results & Conclusion <a name="results--conclusion"></a>

- The system autonomously produces a professional research report on any topic, from searching to final review.
- Each report is scored and reviewed by the Critic Agent before it is considered complete.
- The project shows that a team of collaborating agents can deliver more reliable research than a single AI answering from memory.
- It demonstrates a production-level agentic AI architecture, built with LangChain's LCEL pipeline and shared memory.

---

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f464.png" width="28" height="28" align="absmiddle"> Author & Contact <a name="author--contact"></a>

- **Author:** Ashutosh Rout
- **Email:** ashutoshrout704@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/ashutosh-rout-aa60832a1/
- **GitHub:** https://github.com/ashutosh-rout257
