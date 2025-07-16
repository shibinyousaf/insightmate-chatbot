# 🤖 InsightMate – Your Smart AI Chat Companion

**InsightMate** is a powerful and friendly AI chatbot agent built with **LangGraph**, **FastAPI**, and **Streamlit**. It connects to cutting-edge LLMs like **Groq (LLaMA 3, Mixtral)** and **OpenAI (GPT-4o)**, and optionally enhances responses with real-time search using **Tavily**.

---

![Built with LangGraph, FastAPI, Streamlit](https://img.shields.io/badge/Built%20With-LangGraph%20%7C%20FastAPI%20%7C%20Streamlit-blue)

---

## 🚀 Features

- 💡 **Multi-Model Support** – Switch easily between Groq and OpenAI models.
- 🔍 **Live Web Search (Optional)** – Leverage Tavily to fetch real-time information.
- 🧠 **Customizable System Prompts** – Personalize your AI’s tone and behavior.
- 💬 **Intuitive UI** – Clean, user-friendly chat interface powered by Streamlit.
- ⚡ **FastAPI Backend** – Efficient and production-ready backend integration.

---

## 📸 Demo

> ![screenshot](https://via.placeholder.com/800x300.png?text=Insert+Streamlit+UI+Screenshot+Here)

---

## 🧰 Tech Stack

| Layer        | Technology                         |
|--------------|-------------------------------------|
| 🧠 LLMs       | [Groq](https://groq.com), [OpenAI](https://openai.com) |
| 🔎 Web Search | [Tavily](https://www.tavily.com/) *(optional)* |
| 🧱 Agent Logic| [LangGraph](https://github.com/langchain-ai/langgraph) |
| ⚙️ Backend    | [FastAPI](https://fastapi.tiangolo.com)            |
| 🖼️ Frontend   | [Streamlit](https://streamlit.io)                  |

---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/shibinyousaf/insightmate-chatbot.git
   cd insightmate-chatbot


## ⚙️ Project Phases and Python Commands

You can run the complete chatbot app in three phases. Make sure the backend runs in a separate terminal window.

###  Phase 1: Create AI Agent

```bash
python ai_agent.py
```


###  Phase 2: Setup Backend with FastAPI

```bash
uvicorn backend:app --reload
```

###  Phase 3: Setup Frontend with Streamlit
```bash
streamlit run frontend.py
```


   
