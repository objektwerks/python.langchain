from langchain import OpenAI
from langchain.chains import LLMChain

import os


def main():
    apiKey: str | None = os.getenv("OPENAI_API_KEY")
    assert apiKey, "*** Require OpenAI api key!"

    llm = OpenAI(model_name="text-davinci-003")

    prompt = "Write a story about a pizza."
    print(f"*** Request: {prompt}")

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run()
    print(f"*** Response: {response}")


if __name__ == "__main__":
    main()
