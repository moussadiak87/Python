
import tkinter as tkr 
def creer_fenetre(nom):
	fenetre = tkr.Tk(className = nom)
	return fenetre	

def creer_ecran(container):
	ecran = tkr.Entry(container)
	return ecran 

def creer_pave_numerique(container):
	pave_numerique = []
	for i in range(0, 10):
		pave_numerique.append(tkr.Button(container, text = str(i), command = ma_fonction))
	pave_numerique.append(tkr.Button(container, text = "."))
	return pave_numerique

def ma_fonction():
	print ('hello world')

def creer_pave_operateur(container):
	operateur = ["+", "-", "*", "/", "=", "C"]
	pave_operateur = []
	for i in range (0, len(operateur)):
		pave_operateur.append(tkr.Button(container, text = operateur[i]))
	return pave_operateur

def ajouter_ecran(un_ecran):
	un_ecran.grid(row = 0, columnspan = 3, sticky="ew")

def ajouter_pave_operateur(un_pave_operateur):
	for i in range (0, len(un_pave_operateur)):
		un_pave_operateur[i].grid(row = i , column = 3, sticky = "ew")

def ajouter_pave_numerique(un_pave_numerique):
	for i in range (len(un_pave_numerique)):
		if (i != 0):
			un_pave_numerique[i].grid(row = ((i-1)//3)+1, column = (i-1)%3, sticky = "ew")
		else:
			un_pave_numerique[i].grid(row = 4, column = 1, sticky = "ew")

def afficher(nombre, un_ecran):
	affichage = ecran.get()
	ecran.delete(0,'end')
	affichage = affichage + str(nombre)
	ecran.insert(0, affichage)

def add_event_listener(un_pave_numerique, un_ecran):
	for nombre in range (len(un_pave_numerique)):
		un_pave_numerique[nombre].configure(command = lambda x = nombre: afficher(x, un_ecran))
	un_pave_numerique[-1].configure(command = lambda : afficher ('.', un_ecran))

"""	
		#un_pave_numerique[0].configure(command = lambda : afficher(0, un_ecran))
		#un_pave_numerique[1].configure(command = lambda : afficher(1, un_ecran))
		#un_pave_numerique[2].configure(command = lambda : afficher(2, un_ecran))
		#un_pave_numerique[3].configure(command = lambda : afficher(3, un_ecran))
		#un_pave_numerique[4].configure(command = lambda : afficher(4, un_ecran))
		#un_pave_numerique[5].configure(command = lambda : afficher(5, un_ecran))
		#un_pave_numerique[6].configure(command = lambda : afficher(6, un_ecran))
		#un_pave_numerique[7].configure(command = lambda : afficher(7, un_ecran))
		#un_pave_numerique[8].configure(command = lambda : afficher(8, un_ecran))
		#un_pave_numerique[9].configure(command = lambda : afficher(9, un_ecran))
		#un_pave_numerique[10].configure(command = lambda : afficher('.', un_ecran))
		






# def ajouter_pave_numerique(un_pave_numerique):
# 	for i in range (0, len(un_pave_numerique)):






# comprehension de liste
# pave_numerique = [tkr.Button(container, text = str(i)) for i in range(0, 10)]
# ma_list = [nombre for nombre in range (0, 10)]
# [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9]

# boutton_0 = Button(container, text = "0")
# boutton_1 = Button(container, text = "1")
# boutton_2 = Button(container, text = "2")
# boutton_3 = Button(container, text = "3")
# boutton_4 = Button(container, text = "4")
# boutton_5 = Button(container, text = "5")
# boutton_6 = Button(container, text = "6")
# boutton_7 = Button(container, text = "7")
# boutton_8 = Button(container, text = "8")
# boutton_9 = Button(container, text = "9")



"""