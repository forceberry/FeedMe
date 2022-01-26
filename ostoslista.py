import arvoreseptit
import lisaaresepti
import naytareseptit
from listanluonti import ostoslista
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3 as sql
db = sql.connect("database.db")
def update():
		data = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
		return data

LARGEFONT =("Verdana", 20)

class Ostoslista(tk.Frame):
    def __init__(self, parent, controller):
        reseptit = update()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Ostoslista", font = LARGEFONT)
        label.grid(row = 0, columnspan=5, padx = 10, pady = 10, sticky="ew")

        # button to show frame 2 with text layout2
        button1 = ttk.Button(self, text ="Luo ostoslista")
	
		# putting the button in its place by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky="ew")

		# button to show frame 2 with text
		# layout2
        button2 = ttk.Button(self, text ="Arvo reseptit",
        command = lambda : controller.show_frame(arvoreseptit.ArvoReseptit))
	
		# putting the button in its place by using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky="ew")
        
        button3 = ttk.Button(self, text ="Näytä kaikki reseptit",
		command = lambda : controller.show_frame(naytareseptit.NaytaReseptit))
	
		# putting the button in its place by using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky="ew")

		# button to show frame 2 with text layout2
        button4 = ttk.Button(self, text ="Lisää Resepti",
		command = lambda : controller.show_frame(lisaaresepti.LisaaResepti))

        # putting the button in its place by using grid
        button4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky="ew")

        def sorter(x):
            return x[1]
            
        reseptit.sort(key=sorter)
        kaikki_reseptit = []
        for resepti in reseptit:
            kaikki_reseptit.append(resepti[1])
        if kaikki_reseptit == []:
            kaikki_reseptit.append("Ei reseptejä")
        variable = StringVar(self)
        variable.set("Reseptit") # default value
        w = OptionMenu(self, variable, *kaikki_reseptit)
        w.config(width=30)
        w.grid(row = 1, column = 4)

        valitut_reseptit = []
        ostokset = ""

        def ok():
            print ("value is:" + variable.get())
            ruoka = variable.get()
            try:
                if ruoka != "Reseptit":
                    db = sql.connect("database.db")
                    id = db.execute(f'Select id, resepti, annoksia from Reseptit where resepti="{ruoka}"').fetchone()
                    resepti_id = int(id[0])
                    annoksia = int(id[2])
                    resepti = (resepti_id, id[1], annoksia)
                    print("ID:", resepti_id)
                    valitut_reseptit.append(resepti)
                    variable.set("Reseptit")
                    reseptilista = ""
                    for res in valitut_reseptit:
                        reseptilista += f"{res[1]}, {res[2]} annosta\n"
                    lbl_reseptilista.config(text=reseptilista)
                    print("Reseptilista:", reseptilista)
            except:
                print("Reseptiä ei löytyny")
            else:
                print(valitut_reseptit)

        btn = Button(self, text="Lisää resepti", command=ok)
        btn.grid(row = 1, column = 5, sticky="w")

        def ostosclick(event, reseptit):
            lista = ostoslista(valitut_reseptit)
            lbl_ostoslista.config(text=lista)

        def handle_click(event):
            luoLista = ttk.Button(self, text="Mitä tämä tekee")
            luoLista.bind("<Button-1>", ostosclick(event, reseptit))

        lbl_ostoslista = ttk.Label(self, text=ostokset)
        lbl_ostoslista.grid(row = 2, column = 5, padx=10, columnspan=5, rowspan=50)

        lbl_reseptilista = ttk.Label(self, text=ostokset)
        lbl_reseptilista.grid(row = 4, column = 2, padx=10, columnspan=3, rowspan=50, sticky="nw")

        savebutton = ttk.Button(self, text="Luo ostoslista")
        savebutton.grid(row=2, column=4, sticky="w")
        savebutton.bind("<Button-1>", handle_click)

        def delclick(event):
            valitut_reseptit.clear()
            lbl_reseptilista.config(text="")

        delbutton = ttk.Button(self, text="Tyhjennä ostoslista")
        delbutton.grid(row=3, column=4, sticky="w")
        delbutton.bind("<Button-1>", delclick)