# import csv
# import os
# from langchain.utilities import SQLDatabase
# #connexion a la base de donnees 
# host = 'localhost'
# port = '3306'
# username = 'root'
# password = 'school'
# database_schema = 'db_school'
# mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"
# db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=2)

# # Importation des données du CSV dans la base de données
# with open(f"{os.getcwd()}/ess.csv", newline='') as csvfile:
#     spamreader = csv.reader(csvfile)
#     for row in spamreader:
#         print(row[1])
#         req = f"INSERT INTO students (student_id, first_name, last_name, course_name, grade) VALUES ({row[0]}, '{row[1]}', '{row[2]}','{row[3]}',{row[4]});"
#         print(db.run(req))

###################################################################

import sqlite3
import csv
import os

# ✅ Chemin vers la nouvelle base SQLite
sqlite_path = os.path.join(os.getcwd(), "csv.db")

# ✅ Connexion à SQLite
conn = sqlite3.connect(sqlite_path)
cursor = conn.cursor()

# ✅ Création de la table 'students'
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    course_name TEXT NOT NULL,
    grade REAL
);
""")
conn.commit()

# ✅ Chargement du CSV
csv_path = os.path.join(os.getcwd(), "ess.csv")

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0 and not row[0].isdigit():  # sauter l'entête s'il y en a
            continue
        try:
            student_id = int(row[0])
            first_name = row[1].strip()
            last_name = row[2].strip()
            course_name = row[3].strip()
            grade = float(row[4])

            # ✅ Insertion sécurisée avec paramètres
            cursor.execute("""
                INSERT INTO students (student_id, first_name, last_name, course_name, grade)
                VALUES (?, ?, ?, ?, ?)
            """, (student_id, first_name, last_name, course_name, grade))
        except Exception as e:
            print(f"Erreur à la ligne {i+1} : {e}")

# ✅ Finaliser et fermer
conn.commit()
conn.close()

print("🎉 Migration vers SQLite terminée avec succès !")

