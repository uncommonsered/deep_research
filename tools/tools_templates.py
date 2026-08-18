from abc import ABC, abstractmethod

from langchain_core.tools import BaseTool
from pydantic import Field


class SearchTool(ABC):
    @abstractmethod
    def search(self, query: str) -> list[str]:
        pass


class FetchTool(ABC):
    @abstractmethod
    def fetch(self, urls: list[str]) -> str:
        pass


class SearchAndFetchTool(BaseTool):
    name: str = "search_and_fetch"
    description: str = (
        "Search the web for relevant pages and fetch their full content."
    )

    search_tool: SearchTool = Field(exclude=True)
    fetch_tool: FetchTool = Field(exclude=True)

    def search_and_fetch(self, query: str) -> str:
        urls = self.search_tool.search(query)
        return self.fetch_tool.fetch(urls)

    def _run(self, query: str) -> str:
        return self.search_and_fetch(query)