"""
Class Client
- age
- nb_année_permis
- nb_accident
- nb_année_ancienneté

Class Courtier
- maison_mère
+ etablir_devis(un client)
"""


class Client () :
    def __init__(self) :
        self.age = -1
        self.nb_annee_permis = -1
        self.nb_accident = -1
        self.nb_annee_anciennete = -1

    def get_age(self):
        return self.age

    def get_nb_annee_permis(self):
        return self.nb_annee_permis

    def get_nb_accident(self):
        return self.nb_accident

    def get_nb_annee_anciennete(self):
        return self.nb_annee_anciennete

    def set_age (self, un_age):
        self.age = int(un_age)

    def set_nb_annee_permis (self, un_nb_d_annee):
        self.nb_annee_permi = int(un_nb_d_annee)

    def set_nb_accident (self, un_nb_d_accident):
        self.nb_accident = int(un_nb_d_accident)

    def set_nb_annee_anciennete (self, un_nb_d_annee):
        self.nb_annee_anciennete = int(un_nb_d_annee)

class Courtier () :
    def __init__(self) :
        self.tarif = ""

    def set_tarif(self, une_couleur):
        self.tarif = une_couleur

    def etablir_devis(self, un_client):
        if un_client.get_age() < 25 and un_client.get_nb_annee_permis() < 2 and un_client.get_nb_accident() == 0:
           print ("Vous beneficiez du tarif rouge")
           self.set_tarif("rouge")
        else :
           print ("C'est impossible, merci, au revoir")


