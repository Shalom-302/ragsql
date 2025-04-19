#importations des modules 
import os
import ast 
import certifi
import google.generativeai as genai 
import pymongo
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from pymongo import MongoClient

# Charger les variables d'environnement
load_dotenv()

# Connexion à la base de données MongoDB Atlas via PyMongo
uri = "Ajouter un lien URI depuis le site offciel de mongodb Atlas"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())

# Accéder à la base de données et à la collection
db = client["students_db"]
collection = db["students"]

# Configure l'API Gemini
gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini_api_key)

# Créer le modèle LLM (Gemini)
llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.9, safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },)

# Créer le prompt pour la récupération des données
prompt_template = ChatPromptTemplate.from_template(""" 
Tu es un expert en requettes mongodb tu dois etre capable de donnees et executer les requettes
dans ma collection appele students.
    
   : {user_query}"
    
    
   """)

#Definir la requette
user_query = "retourne un etudiants en maths"
# Generer la requette
invoke = llm.invoke(prompt_template.format(user_query=user_query))
print(invoke.content)


#analyser la requette
def parse_query(query_string):
    # Remove the prefix and suffix
    query_core = query_string.replace("db.", "").replace("find(", "").rstrip(")")
    collection_name, query_params = query_core.split(".", 1)
    query, projection = query_params.split("}, {", 1)
    query = query + "}"
    projection = "{" + projection
    return collection_name, ast.literal_eval(query), ast.literal_eval(projection)

# Example response_query from OpenAI
response_query = "db.collection.find({'field': 'value'}, {'field': 1})"
