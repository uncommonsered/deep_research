from tools.fetcher import HttpxMarkdownFetch
from tools.searcher import SearXNGSearch
from tools.tools_templates import SearchAndFetchTool


def test_search_and_fetch_tool():

    search_tool = SearXNGSearch()
    fetch_tool = HttpxMarkdownFetch()
    search_and_fetch_tool = SearchAndFetchTool(
        search_tool=search_tool, fetch_tool=fetch_tool
    )
    query = "Какие тенденции в развитии LLM имеют место в 2025-2026 году?"

    content = search_and_fetch_tool.search_and_fetch(query)

    assert isinstance(content, str), "Fetched content should be a string"
    assert len(content) > 0, "Fetched content should not be empty"

    print("SearchAndFetchTool start" + "\n\n")
    print(content)
    print("SearchAndFetchTool end" + "\n\n")


if __name__ == "__main__":
    test_search_and_fetch_tool()
