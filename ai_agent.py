import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

def get_response_from_ai_agent(llm_id, messages, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError(f"Unsupported model provider: {provider}")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Format prompt messages as expected
    formatted_messages = []
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            formatted_messages.append(HumanMessage(content=content))
        elif role == "assistant":
            formatted_messages.append(AIMessage(content=content))
        elif role == "system":
            formatted_messages.append(SystemMessage(content=content))

    # Add the system prompt to the start if provided
    if system_prompt:
        formatted_messages.insert(0, SystemMessage(content=system_prompt))

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    state = {"messages": formatted_messages}
    response = agent.invoke(state)
    final_messages = response.get("messages", [])
    ai_messages = [m.content for m in final_messages if isinstance(m, AIMessage)]
    return ai_messages[-1] if ai_messages else "No response received."