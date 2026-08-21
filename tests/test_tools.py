from tools.local_tools import HttpxMarkdownFetch, SearXNGSearch


def test_search_and_fetch_tool():

    search_tool = SearXNGSearch()
    fetch_tool = HttpxMarkdownFetch()
    query = "Какие тенденции в развитии LLM имеют место в 2025-2026 году? Статьи arxiv"

    urls = search_tool.search(query, max_results=20)
    print(urls)

    urls_to_test = ["https://arxiv.org/pdf/2309.11145", "https://pypi.org/project/langchain-pymupdf4llm/"]
    content = fetch_tool.fetch(urls_to_test)

    assert isinstance(content, str), "Fetched content should be a string"
    assert len(content) > 0, "Fetched content should not be empty"

    print("FetchTool start" + "\n\n")
    print(content)
    print("FetchTool end" + "\n\n")


if __name__ == "__main__":
    test_search_and_fetch_tool()
