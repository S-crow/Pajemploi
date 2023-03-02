
#pip install easygui
import easygui

salaire_horaire_net = 4
nbre_heures_par_jour = 9
indemnite_entretien_jour = 3.30
indemnite_repas_jour = 4


if __name__ == "__main__":    

    msg ="Combien de jours travaillés ce mois-ci ?"
    title = "Pajemploi++"
    nbre_jr_travailles = easygui.integerbox(msg,title)

    salaire_net = "Salaire net = " + str(nbre_jr_travailles * salaire_horaire_net * nbre_heures_par_jour) + "\n"
    indemnite_entretien = "Indemnité d'entretien = " + str(indemnite_entretien_jour * nbre_jr_travailles) + "\n"
    indemnite_repas = "Indemnité de repas = " + str(indemnite_repas_jour * nbre_jr_travailles) + "\n"


    easygui.msgbox("{}{}{}".format(salaire_net, indemnite_entretien, indemnite_repas), "Pajemploi++")