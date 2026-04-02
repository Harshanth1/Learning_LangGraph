# Learning LangGraph — Agent Building Journey

This repository documents my hands-on learning and experimentation with **LangGraph**, a framework for building stateful and multi-agent AI systems on top of LangChain.

The goal of this project is to understand how modern AI agents are designed, built, and deployed — starting from basic concepts and progressing to advanced systems like RAG pipelines and multi-agent architectures.

Most of the concepts in this repository are based on the LangGraph course by Sunny Savita, along with my own implementations and experiments.

Course reference:  
https://www.youtube.com/playlist?list=PLQxDHpeGU14AJ4sBRWLBqjMthxrLXJmgF

---

## What is LangGraph?

LangGraph is a library that allows you to define AI workflows as graphs instead of linear chains.

- Nodes represent tasks (LLM calls, tools, logic)
- Edges define how data flows between tasks
- Supports loops, retries, and conditional execution

It is especially useful for:

- Building tool-using agents  
- Creating multi-agent systems  
- Managing stateful conversations  
- Implementing reasoning workflows (e.g., ReAct)

---

## Repository Structure

### 1. Prerequisites & Foundations  
`pre-requist_for_langgraph/`

Covers the basics required before using LangGraph:

- Introduction to RAG (Retrieval-Augmented Generation)
- LangChain Expression Language (LCEL)
- Tool creation and agent basics
- Environment and API setup

---

### 2. Chatbot with LangGraph  
`ChatBot_with_LangGraph/`

A complete chatbot implementation with memory and tool integration.

- ChatBot notebook for experimentation  
- Python implementation of chatbot logic  
- Streamlit UI for interactive usage  

Key learnings:
- Agent loop (thinking → acting → observing)
- Tool integration (web search, etc.)
- Managing conversation state

---

### 3. Agent Patterns  
`different_structure_pattren/`

Exploration of different agent architectures:

- ReAct Agent (Reasoning + Acting loop)
- Structured Output Agent (JSON/dict responses)

Key learnings:
- Choosing the right agent pattern
- Controlling output formats for downstream systems

---

### 4. RAG with LangGraph  
`different_type_RAG_with_LangGraph/`

Implementation of advanced RAG techniques:

- Agentic RAG (agent decides when to retrieve)
- Corrective RAG (validates retrieved documents)
- Self-RAG (model evaluates its own responses)

Key learnings:
- Improving retrieval quality
- Reducing hallucinations
- Making systems more reliable

---

### 5. Multi-Agent Systems  
`Multi_Agent_System/`

Systems where multiple agents collaborate:

- Supervisor agent for task delegation
- Research agents working together
- Network-based agent communication

Key learnings:
- Agent coordination strategies
- Designing agent hierarchies vs networks
- Structured communication between agents

---

### 6. SQL Agent  
`sql_agent_with_langgraph.ipynb`

An agent that interacts with a MySQL database using natural language.

Example:
- Converts user queries into SQL
- Executes queries
- Returns results in plain English

Key learnings:
- Connecting LLMs with databases
- Automating data querying workflows

---

## Tech Stack

- LangGraph  
- LangChain  
- Groq (LLMs)  
- Tavily (web search)  
- ChromaDB / FAISS (vector databases)  
- Sentence Transformers (embeddings)  
- Streamlit (UI)  
- PyMySQL (database connectivity)  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Harshanth1/Learning_LangGraph.git
cd Learning_LangGraph
```

### 2. Install dependencies
```bash
pip install -r LangGraph-end-to-end/requirements.txt
```

### 3. Configure environment variables
```bash
cp LangGraph-end-to-end/.env.example LangGraph-end-to-end/.env
```

Add your API keys:
```
LANGCHAIN_API_KEY=
GROQ_API_KEY=
TAVILY_API_KEY=
GOOGLE_API_KEY=
```

---

## Recommended Learning Path

Follow this order for best understanding:

1. Prerequisites & Foundations  
2. Chatbot with LangGraph  
3. Agent Patterns  
4. RAG Systems  
5. Multi-Agent Systems  
6. SQL Agent  

---

## Purpose of This Repository

- Build a strong foundation in LangGraph  
- Understand real-world AI agent architectures  
- Experiment with different agent designs  
- Create practical, working systems  

---

## Notes

This is a learning-focused repository. The code includes:

- Guided implementations from tutorials  
- Personal experiments  
- Iterative improvements for better understanding  

---

## Acknowledgement

This work is inspired by the LangGraph course by Sunny Savita, which provides a structured introduction to agent-based systems.

---

## Conclusion

LangGraph enables building flexible and powerful AI systems by modeling workflows as graphs. This repository reflects a step-by-step journey from basic concepts to advanced agent architectures.

Feel free to explore, modify, and build on top of it.
