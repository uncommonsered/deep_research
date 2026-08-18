from deepagents import create_deep_agent
from langchain_ollama import ChatOllama

from model.promts import RESEARCH_WORKFLOW_INSTRUCTIONS
from tools.fetcher import HttpxMarkdownFetch
from tools.searcher import SearXNGSearch
from tools.tools_templates import SearchAndFetchTool

search_and_fetch = SearchAndFetchTool(
    search_tool=SearXNGSearch(base_url="http://localhost:8080"),
    fetch_tool=HttpxMarkdownFetch(timeout=10),
)


model = ChatOllama(
    model="qwen3:8b",
    base_url="http://localhost:11434",
    temperature=0,
)

agent = create_deep_agent(
    model=model, tools=[search_and_fetch], system_prompt=RESEARCH_WORKFLOW_INSTRUCTIONS
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Найди информацию о LangGraph и кратко объясни, что это такое.",
            }
        ]
    }
)

final_message = result["messages"][-1]
with open("result.md", "w", encoding="utf-8") as f:
    f.write(final_message.content)
