from langchain_community.utilities import SQLDatabase
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import create_sql_query_chain
# connexion a la base de donnees 
host = 'localhost'
port = '3306'
username = 'root'
password = 'school'
database_schema = 'db_school'
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"
db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=2)

# creer une chaine langchain
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5)
chain = create_sql_query_chain(llm, db)

# Test the setup
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT COUNT(*) AS total_students FROM students;")
# Queries


response = chain.invoke({"question": "How many students are enrolled in the 'Mathematics' course?"})
splited_response = response.replace("SQLQuery: ", "").replace("```sql", "").replace("```", "")
print(splited_response)
print("response:  ",db.run(splited_response))

