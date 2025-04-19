## PREMIER Projet de Gestion de Base de Données SQL avec Gemini et LangChain

Ce projet utilise LangChain et une base de données MySQL pour effectuer des requêtes SQL avec un prompt NLP et importer des données à partir de fichiers CSV.

## Prérequis

 **Python:** Version 3.8 ou ultérieure.
 **MySQL:**  Installation de MySQL sur votre système.
 **Pip:**  Le gestionnaire de paquets Python pour installer les dépendances. 
 **Google Cloud Platform:**  Un compte Google Cloud Platform pour utiliser l'API Gemini.

## Installation

**Cloner le dépôt:**
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>



## Créer un environnement virtuel:
**Sur Mac et Linux:**

python -m venv venv
source venv/bin/activate


**Sur Windows:**
python -m venv venv
venv\Scripts\activate



## Installer les dépendances:
pip install -r requirements.txt

## Installation de MySQL
Installer MySQL si ce n'est pas déjà fait. Pour macOS, vous pouvez utiliser Homebrew pour l'installation :

**brew install mysql**

Démarrer MySQL et se connecter :

**brew services start mysql**

**mysql -u root -p** 

Sur Windows

Téléchargez le MySQL Installer depuis le site officiel de MySQL.
Lancez l'installateur et suivez les instructions à l'écran. Vous pouvez choisir l'installation par défaut ou une installation personnalisée en fonction de vos besoins.
Pendant l'installation, vous serez invité à définir un mot de passe pour l'utilisateur root. Assurez-vous de mémoriser ce mot de passe car vous en aurez besoin plus tard.
Une fois l'installation terminée, lancez MySQL Workbench (ou l'interface en ligne de commande MySQL) pour vous connecter à votre serveur MySQL et vérifier que tout fonctionne correctement.
## Configurer la base de données MySQL:
Créer la base de données:

CREATE DATABASE nom_de_la_base_de_donnees;

Utiliser la base de données:
USE nom_de_la_base_de_donnees;


Créer la table:
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    course_name VARCHAR(255),
    grade INT
);

## Effectuer les migrations
Assurez-vous que le fichier migration.py est présent à la racine du projet. Lancez la commande suivante pour appliquer les migrations à votre base de données :

**python migration.py**

## Configurer les informations de connexion:
Dans votre fichier .env, définissez les variables suivantes:


DB_HOST=localhost
DB_NAME=nom_de_la_base_de_donnees
DB_USER=root
DB_PASSWORD=votre_mot_de_passe


## Configurer l'API Gemini:

Créer un projet Google AI : Créez un projet sur la plateforme Google AI.
Activer l'API Generative AI : Activez l'API Generative AI dans votre projet et récupérez votre clé API.
Recuperer l'API et ajouter dans la variable en tant que chaine de caractere dans le fichier .env

## Utilisation

Exécuter des requêtes SQL: Le script Python utilise LangChain et Gemini pour permettre de poser des questions à la base de données en langage naturel.
Notes
Ce projet utilise des variables d'environnement. Assurez-vous de créer un fichier .env avec les informations de configuration de la base de données et de l'API Gemini.
Le fichier .env devrait être ignoré dans votre système de version (par exemple, en utilisant .gitignore).


## DEUXIEME Projet de Gestion de Base de Données NOSQL avec Gemini et LangChain

**Installer Mongodb sur windows et MAC**
sur MAC : 
$ brew install mongodb-atlas
$ atlas setup

sur wwindows: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

**Configuration de Mongodb et ATLAS cluster**
https://www.mongodb.com/products/platform/atlas-database

**Creer une base de donnees students_db et une collection students**

**Importer les donnees du csv en dans la collection de documents crees**

****
