import requests

from tools.tools_templates import SearchTool


class SearXNGSearch(SearchTool):
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url

    def search(self, query: str, max_results: int) -> list[str]:
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
        return [result["url"] for result in data["results"][: max_results]]
