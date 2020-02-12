import ihm

ma_fenetre = ihm.creer_fenetre("ma calculette")

mon_ecran = ihm.creer_ecran(ma_fenetre)
mon_pave_numerique = ihm.creer_pave_numerique(ma_fenetre)
mon_pave_operateur = ihm.creer_pave_operateur(ma_fenetre)

ihm.ajouter_pave_operateur(mon_pave_operateur)
ihm.ajouter_pave_numerique(mon_pave_numerique)
ihm.ajouter_ecran(mon_ecran)
ihm.add_event_listener(mon_pave_numerique,mon_ecran)

ma_fenetre.mainloop()
