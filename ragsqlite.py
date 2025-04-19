from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re
#########################################
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Connexion à SQLite
db = SQLDatabase.from_uri("sqlite:///csv.db")

# Modèle Gemini
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5)

# Création de la chaîne
chain = create_sql_query_chain(llm, db)

# Exemples de requête
response = chain.invoke({
    "question": "donne moi le nom des etudiants en maths"
})


# Extraire proprement la requête SQL
def extract_sql(text):
    # Cas où le LLM met la requête dans un bloc ```sql
    match = re.search(r"```sql\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Cas où la requête commence après 'SQLQuery:'
    if "SQLQuery:" in text:
        return text.split("SQLQuery:")[1].strip()
    # Dernier recours : cherche un SELECT dans la chaîne
    lines = text.strip().splitlines()
    for line in lines:
        if "SELECT" in line.upper():
            return line.strip()
    return text.strip()

sql_query = extract_sql(response)
print("\n🧾 Requête SQL extraite :", sql_query)

# Exécution
try:
    result = db.run(sql_query)
    print("\n✅ Résultat :", result)
except Exception as e:
    print("\n❌ Erreur lors de l'exécution :", e)