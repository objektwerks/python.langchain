from langchain import OpenAI
from langchain.chains import LLMChain

import os


def main():
    apiKey = os.getenv("OPENAI_API_KEY")
    print(f"*** OpenAI api key: {apiKey}")

    modelName = "text-davinci-003"
    print(f"*** OpenAI model name: {modelName}")

    llm = OpenAI(model_name=modelName)

    prompt = "Write a story about a pizza."
    print(f"*** Request: {prompt}")

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run()
    print(f"*** Response: {response}")


if __name__ == "__main__":
    main()
