from deepagents import create_deep_agent
from langchain_ollama import ChatOllama

from model.promts import RESEARCH_WORKFLOW_INSTRUCTIONS
from tools.fetcher import HttpxMarkdownFetch
from tools.searcher import SearXNGSearch
from tools.tools_templates import SearchAndFetchTool, ThinkTool

search_and_fetch = SearchAndFetchTool(
    search_tool=SearXNGSearch(base_url="http://localhost:8080"),
    fetch_tool=HttpxMarkdownFetch(timeout=10),
)
think_tool = ThinkTool()


model = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://localhost:11434",
    temperature=0,
)

agent = create_deep_agent(
    model=model,
    tools=[search_and_fetch, think_tool],
    system_prompt=RESEARCH_WORKFLOW_INSTRUCTIONS,
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Какие тенденции в развитии LLM имеют место в 2025-2026 году?",
            }
        ]
    }
)

final_message = result["messages"][-1]
with open("result.md", "w", encoding="utf-8") as f:
    f.write(final_message.content)
