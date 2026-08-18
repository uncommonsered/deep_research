from deepagents import create_deep_agent
from langchain_ollama import ChatOllama

from model.promts import RESEARCH_WORKFLOW_INSTRUCTIONS
from tools.local_tools import HttpxMarkdownFetch, ReflectionTool, SearXNGSearch


search_tool = SearXNGSearch(base_url="http://localhost:8080")
fetch_tool = HttpxMarkdownFetch(timeout=10)
think_tool = ReflectionTool()


model = ChatOllama(
    model="qwen3.5:9b",
    base_url="http://localhost:11434",
    temperature=0,
    num_ctx=16384
)

agent = create_deep_agent(
    model=model,
    tools=[search_tool, fetch_tool, think_tool],
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

print(result)