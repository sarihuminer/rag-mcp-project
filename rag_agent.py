from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from tools import read_file, chunk_text_word_aware, store_and_search_chunks

def build_agent():
    """בונה סוכן RAG עם כלי MCP"""
    # יצירת מודל שפה מקומי
    llm = OllamaLLM(model="llama3.2:3b", base_url="http://localhost:11434")
    
    # רשימת כלי MCP
    tools = [
        read_file,
        chunk_text_word_aware,
        store_and_search_chunks,
    ]
    
    # יצירת סוכן עם כלי MCP
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )
    
    return agent