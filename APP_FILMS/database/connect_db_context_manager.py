"""
    Fichier : connect_db_context_manager.py
    Auteur : OM 2021.03.15
    But : Classe pour se connecter à la base de donnée.

    La notion en Python de "context manager" aide à simplifier le code.
    https://docs.python.org/3/library/stdtypes.html#typecontextmanager
    https://book.pythontips.com/en/latest/context_managers.html

    Le coeur du système pour la connexion à la BD
    Si on utilise MAMP il faut indiquer le port
    https://dev.mysql.com/downloads/connector/python/

"""
from flask import flash
from pymysql.constants import CLIENT

from APP_FILMS import HOST_MYSQL
from APP_FILMS import NAME_BD_MYSQL
from APP_FILMS import PASS_MYSQL
from APP_FILMS import USER_MYSQL
from APP_FILMS import PORT_MYSQL
from APP_FILMS.erreurs import msg_erreurs
from APP_FILMS.erreurs.exceptions import *


class MaBaseDeDonnee():
    # Quand on instancie la classe il interprète le code __init__
    def __init__(self):
        self.connexion_bd = None
        try:
            """
                SE CONNECTE A LA BASE DE DONNEE
                autocommit doit être à False, sa valeur est testée lors de la sortie de cette classe.
            """
            self.connexion_bd = pymysql.connect(host=HOST_MYSQL,
                                                user=USER_MYSQL,
                                                password=PASS_MYSQL,
                                                db=NAME_BD_MYSQL,
                                                port=PORT_MYSQL,
                                                client_flag=CLIENT.MULTI_STATEMENTS,
                                                cursorclass=pymysql.cursors.DictCursor,
                                                autocommit=False)
            print("Avec CM BD  CONNECTÉE, TOUT va BIEN !! Dans le constructeur")
            print("self.con....", dir(self.connexion_bd), "type of self.con : ", type(self.connexion_bd))

        except (Exception,
                ConnectionRefusedError,
                pymysql.err.OperationalError,
                pymysql.err.DatabaseError) as erreur:
            flash(f"Flash....BD NON CONNECTÉE. Erreur : {erreur.args[1]}", "danger")
            print("erreur...MaBaseDeDonnee.__init__ ", erreur.args[1])
            raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[1]}")
        print("Avec CM BD  INIT !! ")

    """
        Après la méthode __init__ il passe à __enter__, c'est là qu'il faut surveiller le bon déroulement
        des actions. en cas de problèmes il ne va pas dans la méthode __exit__
    """

    def __enter__(self):
        return self

    """
        Méthode de sortie de la classe, c'est là que se trouve tout ce qui doit être fermé
        Si un problème (une Exception est levée avant (__init__ ou __enter__) cette méthode
        n'est pas interprétée
    """

    def __exit__(self, exc_type, exc_val, traceback):
        # La valeur des paramètres est "None" si tout s'est bien déroulé.
        print("exc_val ", exc_val)
        """
            Si la sortie se passe bien ==> commit. Si exception ==> rollback
            
            Tous les paramètres sont de valeur "None" s'il n'y a pas eu d'EXCEPTION.
            En Python "None" est défini par la valeur "False"
        """
        if exc_val is None:
            print("commit !! Dans le destructeur ")
            self.connexion_bd.commit()
        else:
            print("rollback !! Dans le destructeur ")
            self.connexion_bd.rollback()

        # Fermeture de la connexion à la base de donnée.
        self.connexion_bd.close()
        print("La BD est FERMÉE !! Dans le destructeur")

    """
        Les méthodes suivantes sont définies pour utiliser les "context manager"
        Une fois que l'interprétation de l'un ou l'autre de ces méthodes est terminée
        le destructeur "__exit__" sera automatiquement interprété.
        Ainsi après avoir exécuté la requête MySql on va faire un commit (enregistrer les modifications)
        s'il n'y a pas erreur ou un rollback (retour en arrière) en cas d'erreur
        et finalement fermer la connexion à la BD.
    """

    def mabd_execute(self, sql, params=None):
        print("execute", sql, " params", params)
        return self.connexion_bd.cursor().execute(sql, params or ())

    def mabd_fetchall(self):
        return self.connexion_bd.cursor().fetchall()
