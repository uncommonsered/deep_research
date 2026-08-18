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


class ThinkTool(BaseTool):
    name: str = "think_tool"
    description: str = """Инструмент для стратегического анализа прогресса исследования и принятия решений.

    Используйте этот инструмент после каждого поиска, чтобы проанализировать полученные результаты и систематически спланировать следующие шаги.
    Он создаёт осознанную паузу в процессе исследования для принятия качественных решений.

    Когда использовать:
    - После получения результатов поиска: Какую ключевую информацию я нашёл?
    - Перед определением следующих шагов: Достаточно ли у меня информации, чтобы дать исчерпывающий ответ?
    - При оценке пробелов в исследовании: Какой конкретно информации мне всё ещё не хватает?
    - Перед завершением исследования: Могу ли я уже дать полный ответ?

    Анализ должен охватывать:
    1. Анализ текущих результатов — Какую конкретную информацию я собрал?
    2. Оценка пробелов — Какой важной информации всё ещё не хватает?
    3. Оценка качества — Достаточно ли у меня доказательств и примеров для хорошего ответа?
    4. Стратегическое решение — Следует ли продолжить поиск или уже предоставить ответ?

    Args:
        reflection: Подробное размышление о прогрессе исследования, полученных результатах,
                    существующих пробелах и следующих шагах

    Returns:
        Подтверждение того, что размышление было зафиксировано для принятия дальнейших решений
    """

    def _run(self, reflection) -> str:
        return self.think(reflection)

    def think(self, reflection) -> str:
        return f"Reflected {reflection}"


class SearchAndFetchTool(BaseTool):
    name: str = "search_and_fetch"
    description: str = """Поиск информации в интернете по заданному запросу.

    Сначала выполняет поиск для обнаружения релевантных URL-адресов,
    затем загружает найденные веб-страницы и возвращает их полное содержимое в формате Markdown.

    Args:
        query: Поисковый запрос
        max_results: Максимальное количество результатов для возврата (по умолчанию: 2)

    Returns:
        Отформатированные результаты поиска с полным содержимым найденных веб-страниц
    """

    search_tool: SearchTool = Field(exclude=True)
    fetch_tool: FetchTool = Field(exclude=True)

    def search_and_fetch(self, query: str, max_results: int = 2) -> str:
        urls = self.search_tool.search(query, max_results)
        return self.fetch_tool.fetch(urls)

    def _run(self, query: str, max_results: int = 2) -> str:
        return self.search_and_fetch(query, max_results)
