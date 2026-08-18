import requests

from tools.tools_templates import SearchTool


class SearXNGSearch(SearchTool):
    def __init__(self, base_url: str = "http://localhost:8080", max_results: int = 2):
        self.base_url = base_url
        self.max_results = max_results

    def search(self, query: str) -> list[str]:
        response = requests.get(
            f"{self.base_url}/search",
            params={
                "q": query,
                "format": "json",
            },
            timeout=30,
        )

        response.raise_for_status()
        data = response.json()
        return [result["url"] for result in data["results"][: self.max_results]]
