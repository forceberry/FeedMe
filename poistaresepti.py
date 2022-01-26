import arvoreseptit
import lisaaresepti
import naytareseptit
import ostoslista
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3 as sql
db = sql.connect("database.db")
def update():
		data = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
		return data

LARGEFONT =("Verdana", 20)

class PoistaResepti(tk.Frame):
	
	def __init__(self, parent, controller):
		reseptit = update()

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Poista resepti", font = LARGEFONT)
		label.grid(row = 0, columnspan=5, padx = 10, pady = 10, sticky="ew")

		# button to show frame 2 with text layout2
		button1 = ttk.Button(self, text ="Luo ostoslista",
        command = lambda : controller.show_frame(ostoslista.Ostoslista))
	
		# putting the button in its place by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky="ew")

		button2 = ttk.Button(self, text ="Arvo reseptit",
        command = lambda : controller.show_frame(arvoreseptit.ArvoReseptit))
	
		# putting the button in its place by using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky="ew")

		button3= ttk.Button(self, text ="Näytä kaikki reseptit",
		command = lambda : controller.show_frame(naytareseptit.NaytaReseptit))
	
		# putting the button in its place by using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky="ew")

		## button to show frame 2 with text layout2
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
		w.grid(row = 1, column = 4)

		def ok():
			print ("value is:" + variable.get())
			ruoka = variable.get()
			try:
				if ruoka != "Reseptit":
					db = sql.connect("database.db")
					id = db.execute(f'Select id from Reseptit where resepti="{ruoka}"').fetchone()
					resepti_id = int(id[0])
					print("ID:", resepti_id)
					db.execute(f'Delete from Reseptit where id={resepti_id}')
					db.execute(f'Delete from Ainesosat where resepti={resepti_id}')
					db.commit()
			except:
				print("Reseptiä ei löytyny")
			else:
				print("Valitse resepti...")

		btn = Button(self, text="Poista", command=ok)
		btn.grid(row = 1, column = 5)

		#lbl_reseptit = ttk.Label(self, text=kaikki_reseptit)
		#lbl_reseptit.grid(row = 1, column = 4, rowspan=5)
