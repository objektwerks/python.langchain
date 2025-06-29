Python LangChain
----------------
>Python LangChain *beer style* app using OpenAI.

OpenAI
------
>Obtain an OpenAI API key from OpenAI.

>Then create an environment variable: export OPENAI_API_KEY="key-value"

Install
-------
1. ```uv add langchain langchain-openai```
2. ```uv add --dev ruff```

Ruff
----
1. ```uvx ruff format```
2. ```uvx ruff check```

Run
---
1. ```uv run main.py```
>or:
1. ```uv run main.py Pilsner```
>A single word beer style **must** be used, such as: ```uv run main.py PaleAle```

Resources
---------
* [LangChain](https://python.langchain.com/docs/introduction/)
