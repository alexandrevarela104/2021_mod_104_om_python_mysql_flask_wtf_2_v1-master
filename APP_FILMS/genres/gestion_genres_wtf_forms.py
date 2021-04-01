"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_utilisateur_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utilisateur_wtf = StringField("Clavioter le nom d'utilisateur ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_utilisateur_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    email_regexp = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    email_wtf = StringField("Clavioter l'adresse mail ",
                                      validators=[Length(min=2, max=50, message="min 2 max 20"),
                                                  Regexp(email_regexp,
                                                         message="N'oubliez pas le @, "
                                                                 "le domaine (gmail,hotmail etc...), "
                                                                 "pas d'espace, "
                                                                 "l'extension (.com, .ch etc...)")
                                                  ])
    mot_de_passe_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    mot_de_passe_wtf = StringField("Clavioter le mot de passe ",
                                      validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                  Regexp(mot_de_passe_regexp,
                                                         message="Pas de chiffres, de caractères "
                                                                 "spéciaux, "
                                                                 "d'espace à double, de double "
                                                                 "apostrophe, de double trait union")
                                                  ])
    submit = SubmitField("Enregistrer genre")
