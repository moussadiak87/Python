from arithmetique import Calculette
from vue import Ihm_calculette
# definir cahier des charges
# intro basic jacobson 
# cadrer les classes 

ma_calc = Calculette()
view = Ihm_calculette(ma_calc)
view.lay_elements()



"""
valeur, souhait, row //3, col %3, solution 
1 			(1, 0) ,	0			, 1				valeur % 3 - valeur
2 			(1, 1) , 	0			, 1
3 			(1, 2) , 	1			, 
4 			(2, 0) , 				, 
5 			(2, 1) , 				, 
6 			(2, 2) , 				, 
7 			(3, 0) , 				, 
8 			(3, 1) , 				, 
9 			(3, 2) , 				, 
0				(4, 1) ,				, 
"""