from calculatrice_graphique import Calculatrice_graphique
from calculatrice_logique import *

print (__name__)


if __name__ == "__main__":
    ma_logique = Calculatrice_logique()
    ma_calc = Calculatrice_graphique(ma_logique)
    ma_calc.creer_pave_numerique()
    ma_calc.creer_pave_operateur()
    ma_calc.agencer_elements()
    ma_calc.associer_commande_pave_numerique()
    ma_calc.associer_commande_pave_operateur()
    ma_calc.fenetre.mainloop()


