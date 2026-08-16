import httpx
from markdownify import markdownify
from tools.tools_templates import FetchTool


class HttpxMarkdownFetch(FetchTool):
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def fetch(self, urls: list[str]) -> str:
        final_content = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for url in urls:
            try:
                response = httpx.get(url, headers=headers, timeout=self.timeout)
                response.raise_for_status()
                final_content += (
                    f"url: {url}\ncontent: {markdownify(response.text)}\n\n"
                )
            except Exception as e:
                final_content += f"url: {url}\ncontent: Error fetching: {str(e)}\n\n"
        return final_content
