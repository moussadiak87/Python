from tkinter import Tk, Entry, Button
window = Tk()
window.title("ma calculette")
mon_ecran = Entry(window)
mon_ecran.grid(column = 0 ,row = 0, columnspan = 3) 

pave_numerique = []
pave_operateur = []

symboles_operateurs = ["=", "+", "-", "/", "*", "C"]

for i in range (0,11):
    if i == 10: 
        pave_numerique.append(Button(window, text = "."))
    else : 
        pave_numerique.append(Button(window, text = i, command = afficher)

for i in range (0, 11):
    if i == 0 : 
        pave_numerique[i].grid(column = 1, row = 4)
    elif i == 10:
        pave_numerique[i].grid(column = 0, row = 4)
    else : 
        pave_numerique[i].grid(column = (i-1)%3, row = ((i-1)//3)+1)
    
for i in range (0, len(symboles_operateurs)):
    pave_operateur.append(Button(window, text = symboles_operateurs[i]))
    if i == 0: 
        pave_operateur[i].grid(column = 2, row = 4)
    else :
        pave_operateur[i].grid(column = 3, row = i)

window.mainloop()