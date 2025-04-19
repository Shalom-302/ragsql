from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_google_genai import ChatGoogleGenerativeAI

# Create an instance of the LLM, using the 'gemini-pro' model with a specified creativity level
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5)

# Send a creative prompt to the LLM
response = llm.invoke('Write a paragraph about life on Mars in year 2100.')
print(response.content)
