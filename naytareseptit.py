import arvoreseptit
import lisaaresepti
import ostoslista
import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

def update():
	db = sql.connect("database.db")
	data = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
	db.close()
	return data

def sorter(x):
	return x[1]

LARGEFONT =("Verdana", 20)

class NaytaReseptit(tk.Frame):
	
	def __init__(self, parent, controller):
		reseptit = update()

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Näytä kaikki reseptit", font = LARGEFONT)
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

		button3 = ttk.Button(self, text ="Näytä kaikki reseptit")
	
		# putting the button in its place by using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky="ew")

		## button to show frame 2 with text layout2
		button4 = ttk.Button(self, text ="Lisää Resepti",
		command = lambda : controller.show_frame(lisaaresepti.LisaaResepti))
	
		# putting the button in its place by using grid
		button4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky="ew")

		reseptit.sort(key=sorter)
		kaikki_reseptit = ""
		for resepti in reseptit:
			kaikki_reseptit += f"{resepti[1]}, {resepti[2]} annosta\n"

		lbl_reseptit = ttk.Label(self, text=kaikki_reseptit)
		lbl_reseptit.grid(row = 1, column = 4, rowspan=99)
