from calculatrice_graphique import Calculatrice_graphique, afficher
ma_calc = Calculatrice_graphique()
ma_calc.creer_pave_numerique()
ma_calc.creer_pave_operateur()
ma_calc.agencer_elements()
ma_calc.associer_commande_pave_numerique()

ma_calc.fenetre.mainloop()