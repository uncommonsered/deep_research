from abc import ABC, abstractmethod


class SearchTool(ABC):
    @abstractmethod
    def search(self, query: str) -> list:
        pass


class FetchTool(ABC):
    @abstractmethod
    def fetch(self, urls: list[str]) -> str:
        pass

class SearchAndFetchTool:
    def __init__(self, search_tool: SearchTool, fetch_tool: FetchTool):
        self.search_tool = search_tool
        self.fetch_tool = fetch_tool

    def search_and_fetch(self, query: str) -> str:
        urls = self.search_tool.search(query)
        return self.fetch_tool.fetch(urls)