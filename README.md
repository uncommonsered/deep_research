# Deep Research Agent

Локальный LLM ассистент для проведения исследований по концепции Deep Research.
Способен разбить задачу на этапы, выполнять веб-поиск, рефлексировать над задачей и формировать итоговый отчет в формате markdown

## Структура проекта

```text
deep_research/
├── infrastructure/
│   ├── core-config/
│   │   └── settings.yml
│   ├── .env.example
│   └── docker-compose.yml
├── model/
│   ├── agent.py
│   └── promts.py
├── tests/
│   └── test_tools.py
├── tools/
│   ├── local_tools.py
│   └── tools_templates.py
├── .gitignore
├── example_research.ipynb
└── utils.py
```

## Запуск и установка

Клонируем репозиторий и переходим в корневую папку:

```bash
git clone https://github.com/uncommonsered/deep_research 
cd deep_research
```

Создаем виртуальное окружение и устанавливаем необходимые библиотеки:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```


### Запуск модели

Создаем файл с настройками окружения (подробнее в `.env.example`) `.env`:

```bash
cd infrastructure

nano .env
```

Для работы необходимо заполнить следующие поля в `.env`:

```env
SEARXNG_SECRET="some_secret_string"
SEARXNG_HOST=127.0.0.1
SEARXNG_PORT=8080
```

Запускаем сервисы и развертываем модель в контейнере с ollama с любой моделью из доступных [тут](https://ollama.com/library):

```bash
docker compose up -d
docker exec -it ollama ollama run qwen3.5:9b
```

## Запуск агента

Из корня проекта:

```bash
python3 -m model.agent
```

После выполнения результат сохраняется в `result.md`.
Примеры работы указанной модели и порядок вызовов тулов можно посмотреть в `example_research.ipynb`.