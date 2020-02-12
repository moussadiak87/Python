from tkinter import Tk, Entry, Button
window = Tk()
window.title("ma calculette")
screen = Entry(window)
screen.grid(column = 0 ,row = 0, columnspan = 3) 

pave_numerique = []
pave_operateur = []

for i in range (0,11):
    if i == 10: 
        pave_numerique.append(Button(window, text = "."))
    else : 
        pave_numerique.append(Button(window, text = i))
    
for i in range (0, 11):
    if i == 0 : 
        pave_numerique[i].grid(column = 1, row = 4)
    elif i == 10:
        pave_numerique[i].grid(column = 0, row = 4)
    else : 
        pave_numerique[i].grid(column = (i-1)%3, row = ((i-1)//3)+1)
    

window.geometry("600x400")
window.mainloop()