from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os


def main():
    apiKey: str | None = os.getenv("OPENAI_API_KEY")
    assert apiKey, "*** Require OpenAI api key!"

    prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(
        "Tell me about this beer style {topic}"
    )

    model: ChatOpenAI = ChatOpenAI(model="gpt-4o-mini")

    chain: RunnableSerializable = prompt | model | StrOutputParser()

    response: str = chain.invoke({"topic": "Indian Pale Ale"})
    print(f"*** Response: {response}")


if __name__ == "__main__":
    main()
