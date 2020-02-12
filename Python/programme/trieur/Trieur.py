class Trieur(): 
    def __init__(self):
        self.age = -1
        self.categorie = ""
        self.liste_categorie = ["poussin", "pupille", "minime", "cadet", "aucune"]

    def trier(self): 
        instruction 1 
        instruction 2 
    
    def affecter_categorie(self): 
        if self.age >= 6 : 
            if self.age <= 7:
                print ("Tu es dans la categorie", self.liste_categorie[0])
                return self.liste_categorie[0]
            elif self.age <= 9:
                print("Tu es dans la categorie", self.liste_categorie[1]+".")
                print("Tu es dans la categorie " + self.liste_categorie[1]+ ".")
                return self.liste_categorie[1]
            elif self.age <= 11:
                print ("tu es dans la categorie", self.liste_categorie[2])
                return self.liste_categorie[2]
            else:
                print ("tu es dans la categorie", self.liste_categorie[3])
                return self.liste_categorie[3]
        else : 
            print ("tu es dans", self.liste_categorie[4], "categorie.")
            return self.liste_categorie [4]
