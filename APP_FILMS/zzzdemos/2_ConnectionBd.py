"""
    Fichier : 2_Connectionbd.py
    Auteur : OM 2021.03.03 Connection par l'instanciation de la classe Toolsbd.

    On obtient un objet "objet_connectbd"
    Cela permet de se connecter à la base de donnée.
"""

from APP_FILMS.database.database_tools import Toolsbd

try:

    """
        Une connection à la BD simplement avec l'instanciation de la "CLASSE" Toolsbd()
        Un curseur va être nécessaire pour se déplacer dans la BD.
    """
    objet_connectbd = Toolsbd()
    connect_mabd = objet_connectbd.connect_database()
    curseur_mabd = connect_mabd.cursor()

    """
        Une seule requête pour montrer la récupération des données dans la BD en MySql.
        Il n'y a aucun contrôle, aucun test, sans traitements d'erreurs.
        Tous ces tests restent à découvrir dans le sujet suivant.
    """
    strsql_genres_afficher = """SELECT id_user, nom_user, email, password FROM t_user ORDER BY id_user ASC"""
    curseur_mabd.execute(strsql_genres_afficher)
    data_genres = curseur_mabd.fetchall()

    print("data_genres ", data_genres, " Type : ", type(data_genres))

    curseur_mabd.close()
    connect_mabd.close()

except Exception as ErreurConnectionBD:
    print(f"Connection à la BD Impossible !"
          f"{ErreurConnectionBD.args[0]} , "
          f"{ErreurConnectionBD}")



