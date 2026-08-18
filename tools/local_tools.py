import httpx
import requests
import trafilatura
from markdownify import markdownify

from tools.tools_templates import FetchTool, SearchTool, ThinkTool


class HttpxMarkdownFetch(FetchTool):
    timeout: int = 10

    def fetch(self, urls: list[str]) -> str:
        final_content = ""

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }

        for url in urls:
            try:
                response = httpx.get(
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    follow_redirects=True,
                )
                response.raise_for_status()

                text = trafilatura.extract(
                    response.text,
                    include_links=True,
                    include_tables=True,
                    output_format="markdown",
                )

                if not text:
                    text = "Failed to extract page content"

                final_content += f"url: {url}\ncontent:\n{text}\n\n"

            except Exception as e:
                final_content += f"url: {url}\ncontent: Error fetching: {e}\n\n"

        return final_content


class SearXNGSearch(SearchTool):
    base_url: str = "http://localhost:8080"

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
        return [result["url"] for result in data["results"][:max_results]]


class ReflectionTool(ThinkTool):
    def think(self, reflection) -> str:
        return f"Reflected {reflection}"
