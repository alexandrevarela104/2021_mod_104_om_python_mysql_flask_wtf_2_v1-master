"""
    Auteur : OM 2021.03.24
    Définition d'une "route" /mon_premier_wtform

    Test : ex : http://127.0.0.1:5005/mon_premier_wtform

    Paramètres : sans

    But : Pour apprivoiser les WTF forms. (Python et FLask)


"""
from flask import flash
from flask import redirect
from flask import render_template

from APP_FILMS import obj_mon_application
from APP_FILMS.essais_wtf_forms.wtf_forms_1 import MonPremierWTForm


@obj_mon_application.route("/mon_premier_wtform", methods=['GET', 'POST'])
def mon_premier_wtform():
    form = MonPremierWTForm()
    if form.validate_on_submit():
        flash(f"Données du form : {form.username.data}, "
              f"nepascliquer={form.case_cocher_npc.data}, "
              f"{form.nom_utilisateur_wtf.data}", "success")
        return redirect('/homepage')
    else:
        flash(f"il se passe un truc dans le ELSE du petit mon_premier_wtform")
    return render_template('zzz_essais_om_104/essai_form_login.html', title='Mon joli premier WTF', form=form)
