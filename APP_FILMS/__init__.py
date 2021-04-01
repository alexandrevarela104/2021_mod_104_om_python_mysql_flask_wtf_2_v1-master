"""
    Fichier : __init__.py
    Auteur : OM 2021.03.15 Initialisation de l'application.

    Est interprété "automatiquement" lorsque "1_run_server_flask.py" est interprété en premier.

    Variables indispensables pour le serveur MySql et pour le microframework Flask.
    Paramètres : Fichier nommé ".env" situé dans le répertoire principal
                Le fichier ".env" DOIT être signalé dans le ".gitignore",
                car il contient des données confidentielles (key, passwords, etc)
"""

import sys

from flask import Flask
import environs
from environs import Env

HOST_MYSQL = None
USER_MYSQL = None
PASS_MYSQL = None
PORT_MYSQL = None
NAME_BD_MYSQL = None
NAME_FILE_DUMP_SQL_BD = None

ADRESSE_SRV_FLASK = None
DEBUG_FLASK = None
PORT_FLASK = None
SECRET_KEY_FLASK = None

try:

    obj_env = Env()
    obj_env.read_env()
    HOST_MYSQL = obj_env("HOST_MYSQL")
    USER_MYSQL = obj_env("USER_MYSQL")
    PASS_MYSQL = obj_env("PASS_MYSQL")
    PORT_MYSQL = int(obj_env("PORT_MYSQL"))  # Pour la connection à la BD le port doit être une valeur numérique INT
    NAME_BD_MYSQL = obj_env("NAME_BD_MYSQL")
    NAME_FILE_DUMP_SQL_BD = obj_env("NAME_FILE_DUMP_SQL_BD")

    ADRESSE_SRV_FLASK = obj_env("ADRESSE_SRV_FLASK")
    DEBUG_FLASK = obj_env("DEBUG_FLASK")
    PORT_FLASK = obj_env("PORT_FLASK")
    SECRET_KEY_FLASK = obj_env("SECRET_KEY_FLASK")

except environs.EnvError as NameVariableEnv:
    print(f"environs.EnvError Problème avec les variables d'environnement "
          f"{NameVariableEnv.args[0]} , "
          f"{NameVariableEnv}")
    # Erreur très importante d'initialisation des paramètres de l'application. Donc ARRET immédiat.
    sys.exit()
except NameError as NameVariableErrorEnv:
    print(f"Problème avec les noms des variables d'environnement "
          f"{NameVariableErrorEnv.args[0]} , "
          f"{NameVariableErrorEnv.args[0]} , "
          f"{NameVariableErrorEnv}")

except Exception as ErreurFichierEnvironnement:
    raise (f"Problème avec le fichier .env  ")

try:

    # Objet qui fait "exister" notre application
    print(" __name__ ", __name__)
    obj_mon_application = Flask(__name__, template_folder="templates")

    # Flask va pouvoir crypter les cookies
    obj_mon_application.secret_key = SECRET_KEY_FLASK
except Exception as error_app:
    print(f"Problème d'application "
          f"{error_app.args[0]} , "
          f"{error_app}")
    raise

"""
    Tout commence ici. Il faut "indiquer" les routes de l'applicationn.    
    Dans l'aplication les lignes ci-dessous doivent se trouver ici... soit après l'instanciation de la classe "Flask"
"""
from APP_FILMS.database import database_tools

from APP_FILMS.essais_wtf_forms import gestion_essai_wtf

from APP_FILMS.genres import gestion_genres_crud

from APP_FILMS.zzzdemos import routes_demos
