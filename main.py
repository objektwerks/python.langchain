from langchain import OpenAI
from langchain.chains import LLMChain

import os

def main():
    apiKey = os.getenv('OPENAI_API_KEY')
    print(f"OpenAI api key: {apiKey}")



if __name__ == "__main__":
    main()