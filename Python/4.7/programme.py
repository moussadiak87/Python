from lib1 import Client, Courtier

mody = Client()
mody.set_age(input("Veuillez entrer votre age"))
mody.set_nb_annee_permis(input("Veuillez entrer votre nb d'année de permis"))
mody.set_nb_accident(input("Veuillez entrer votre nb d'accidents"))
mody.set_nb_annee_anciennete (input("Veuillez entrer votre nb d'année d'ancienneté"))

mon_courtier = Courtier()
mon_courtier.etablir_devis(mody)

