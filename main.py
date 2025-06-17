from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI

import os


def main():
    apiKey: str | None = os.getenv("OPENAI_API_KEY")
    assert apiKey, "*** Require OpenAI api key!"

    request: str = "Tell me about this beer style, {topic}"
    print(f"*** Request: {request}")
    
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(request)

    model: ChatOpenAI = ChatOpenAI(model="gpt-4o-mini")

    chain: RunnableSerializable = prompt | model | StrOutputParser()

    topic: str = "Indian Pale Ale"
    print(f"*** Topic: {topic}")

    response: str = chain.invoke({"topic": topic})
    print(f"*** Response: {response}")


if __name__ == "__main__":
    main()
