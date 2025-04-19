import csv
import os
from langchain.utilities import SQLDatabase
#connexion a la base de donnees 
host = 'localhost'
port = '3306'
username = 'root'
password = 'xxxxxxxxxxxxxxxx'
database_schema = 'xxxxxxxxxxxxxxxx'
mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"
db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=2)

# Importation des données du CSV dans la base de données
with open(f"{os.getcwd()}/ess.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[1])
        req = f"INSERT INTO students (student_id, first_name, last_name, course_name, grade) VALUES ({row[0]}, '{row[1]}', '{row[2]}','{row[3]}',{row[4]});"
        print(db.run(req))

