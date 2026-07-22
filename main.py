import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-flash-latest")
response=llm.invoke("what is the meaning of life?")
print(response)

