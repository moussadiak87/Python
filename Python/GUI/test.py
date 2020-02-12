from tkinter import *

root = Tk() #créé l'objet fenêtre
root.title("Tk TP style")

x = root.winfo_screenwidth()
y = root.winfo_screenheight()

root.geometry("600x400+" + str(int(x / 2) - 300) + "+" + str(int(y / 2) - 200))  # Permet de centrer l'écran

label0 = Label(root, text= "Label 0", bg= "red")
label1 = Label(root, text= "Label 1", bg= "orange")
label2 = Label(root, text= "Label 2", bg= "purple")
label3 = Label(root, text= "Label 3", bg= "blue")
label4 = Label(root, text= "Label 4", bg= "yellow")
label5 = Label(root, text= "Label 5", bg= "white")
label6 = Label(root, text= "Label 6", bg= "green")

label0.grid(column=0,row=0, columnspan="3", sticky="e,w")
label1.grid(column=0,row=1)
label2.grid(column=1,row=1)
label3.grid(column=2,row=1, rowspan="3", sticky="nw,se")
label4.grid(column=0,row=2)
label5.grid(column=0,row=3)
label6.grid(column=1,row=2,rowspan="2")

root.mainloop()  # lance la fenêt













