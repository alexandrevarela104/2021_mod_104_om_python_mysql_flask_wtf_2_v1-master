"""
    Fichier : 1_run_server_flask.py
    Auteur : OM 2021.03.15
    Démarrer le serveur grâce au microframework FLASK (basé sur JINJA (coté HTML)
    et Werkzeug (Web Server Gateway Interface) https://wsgi.readthedocs.io/en/latest/

    Connection à la base de données.
    Nécessite un fichier de configuration externe : /.env
"""

from flask import flash
from flask import render_template

from APP_FILMS import obj_mon_application

from APP_FILMS import DEBUG_FLASK
from APP_FILMS import ADRESSE_SRV_FLASK
from APP_FILMS import PORT_FLASK

"""
    Pour définir sa propre page d'erreur 404
    Ce code est repris de la documentation FLASK
    https://flask-doc.readthedocs.io/en/latest/patterns/errorpages.html
"""


@obj_mon_application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


"""
    Grâce à la méthode "flash" cela permet de "raise" (remonter) les erreurs "try...execpt" dans la page "home.html"
"""


@obj_mon_application.errorhandler(Exception)
def om_104_exception_handler(error):
    flash(f"Erreur : {error}", "danger")
    return render_template("home.html")


if __name__ == "__main__":
    """
        Pour montrer qu'on peut paramétrer Flask :
        On active le mode DEBUG
        L'adresse IP du serveur mis en place par Flask peut être changée.
        Pour ce fichier on impose le numéro du port.
    """
    print("obj_mon_application.url_map ____> ", obj_mon_application.url_map)
    obj_mon_application.run(debug=DEBUG_FLASK,
                            host=ADRESSE_SRV_FLASK,
                            port=PORT_FLASK)
