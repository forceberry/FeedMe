import arvoreseptit
import ostoslista
import poistaresepti
from naytareseptit import NaytaReseptit
import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from autocomplete import AutocompleteEntry

LARGEFONT =("Verdana", 20)

db = sql.connect("database.db")
def update():
		data = db.execute("Select nimi from Ainesosat").fetchall()
		return data

class LisaaResepti(tk.Frame):
	def __init__(self, parent, controller):
		ainesosat = update()
		nimet = set()
		nimilist = []
		for aines in ainesosat:
			aines = aines[0].lower()
			nimet.add(aines)
		for aines in nimet:
			nimilist.append(aines)
		nimilist.sort()
		print(nimilist)

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Lisää resepti", font = LARGEFONT)
		label.grid(row = 0, column = 0, columnspan = 4, padx = 3, pady = 10, sticky="w")

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Luo ostoslista",
        command = lambda : controller.show_frame(ostoslista.Ostoslista))
	
		# putting the button in its place by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky="ew")

		button2 = ttk.Button(self, text ="Arvo reseptit",
        command = lambda : controller.show_frame(arvoreseptit.ArvoReseptit))
	
		# putting the button in its place by using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky="ew")

		button3 = ttk.Button(self, text ="Näytä kaikki reseptit",
		command = lambda : controller.show_frame(NaytaReseptit))
	
		# putting the button in its place by using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky="ew")

		# button to show frame 2 with text layout2
		button4 = ttk.Button(self, text ="Lisää Resepti")
	
		# putting the button in its place by using grid
		button4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky="ew")

		# button to show frame 2 with text layout2
		button5 = ttk.Button(self, text ="Poista resepti",
		command = lambda : controller.show_frame(poistaresepti.PoistaResepti))
	
		# putting the button in its place by using grid
		button5.grid(row = 5, column = 1, padx = 10, pady = 10, sticky="ew")

		lbl_resepti = ttk.Label(self, text="Resepti:")
		ent_resepti = ttk.Entry(self, width=20)
		lbl_annoksia = ttk.Label(self, text="Annoksia:")
		ent_annoksia = ttk.Entry(self, width=20)
		lbl_resepti.grid(row=2, column=2, sticky="e")
		ent_resepti.grid(row=2, column=3, padx = 3, sticky="w")
		lbl_annoksia.grid(row=2, column=4, sticky="e")
		ent_annoksia.grid(row=2, column=5, padx = 3, sticky="w")
		lbl_ainekset = ttk.Label(self, text="Ainekset")
		lbl_ainekset.grid(row=3, column=2, sticky="e")
		ent_aines1 = AutocompleteEntry(nimet, self)
		lbl_maara1 = ttk.Label(self, text="Määrä:")
		ent_maara1 = ttk.Entry(self, width=20)
		ent_aines1.grid(row=4, column=3, padx = 3, sticky="w")
		lbl_maara1.grid(row=4, column=4, sticky="e")
		ent_maara1.grid(row=4, column=5, padx = 3, sticky="w")
		ent_aines2 = AutocompleteEntry(nimet, self)
		lbl_maara2 = ttk.Label(self, text="Määrä:")
		ent_maara2 = ttk.Entry(self, width=20)
		ent_aines2.grid(row=5, column=3, padx = 3, sticky="w")
		lbl_maara2.grid(row=5, column=4, sticky="e")
		ent_maara2.grid(row=5, column=5, padx = 3, sticky="w")
		ent_aines3 = AutocompleteEntry(nimet, self)
		lbl_maara3 = ttk.Label(self, text="Määrä:")
		ent_maara3 = ttk.Entry(self, width=20)
		ent_aines3.grid(row=6, column=3, padx = 3, sticky="w")
		lbl_maara3.grid(row=6, column=4, sticky="e")
		ent_maara3.grid(row=6, column=5, padx = 3, sticky="w")
		ent_aines4 = AutocompleteEntry(nimet, self)
		lbl_maara4 = ttk.Label(self, text="Määrä:")
		ent_maara4 = ttk.Entry(self, width=20)
		ent_aines4.grid(row=7, column=3, padx = 3, sticky="w")
		lbl_maara4.grid(row=7, column=4, sticky="e")
		ent_maara4.grid(row=7, column=5, padx = 3, sticky="w")
		ent_aines5 = AutocompleteEntry(nimet, self)
		lbl_maara5 = ttk.Label(self, text="Määrä:")
		ent_maara5 = ttk.Entry(self, width=20)
		ent_aines5.grid(row=8, column=3, padx = 3, sticky="w")
		lbl_maara5.grid(row=8, column=4, sticky="e")
		ent_maara5.grid(row=8, column=5, padx = 3, sticky="w")
		ent_aines6 = AutocompleteEntry(nimet, self)
		lbl_maara6 = ttk.Label(self, text="Määrä:")
		ent_maara6 = ttk.Entry(self, width=20)
		ent_aines6.grid(row=9, column=3, padx = 3, sticky="w")
		lbl_maara6.grid(row=9, column=4, sticky="e")
		ent_maara6.grid(row=9, column=5, padx = 3, sticky="w")
		ent_aines7 = AutocompleteEntry(nimet, self)
		lbl_maara7 = ttk.Label(self, text="Määrä:")
		ent_maara7 = ttk.Entry(self, width=20)
		ent_aines7.grid(row=10, column=3, padx = 3, sticky="w")
		lbl_maara7.grid(row=10, column=4, sticky="e")
		ent_maara7.grid(row=10, column=5, padx = 3, sticky="w")
		ent_aines8 = AutocompleteEntry(nimet, self)
		lbl_maara8 = ttk.Label(self, text="Määrä:")
		ent_maara8 = ttk.Entry(self, width=20)
		ent_aines8.grid(row=11, column=3, padx = 3, sticky="w")
		lbl_maara8.grid(row=11, column=4, sticky="e")
		ent_maara8.grid(row=11, column=5, padx = 3, sticky="w")
		ent_aines9 = AutocompleteEntry(nimet, self)
		lbl_maara9 = ttk.Label(self, text="Määrä:")
		ent_maara9 = ttk.Entry(self, width=20)
		ent_aines9.grid(row=12, column=3, padx = 3, sticky="w")
		lbl_maara9.grid(row=12, column=4, sticky="e")
		ent_maara9.grid(row=12, column=5, padx = 3, sticky="w")
		ent_aines10 = AutocompleteEntry(nimet, self)
		lbl_maara10 = ttk.Label(self, text="Määrä:")
		ent_maara10 = ttk.Entry(self, width=20)
		ent_aines10.grid(row=13, column=3, padx = 3, sticky="w")
		lbl_maara10.grid(row=13, column=4, sticky="e")
		ent_maara10.grid(row=13, column=5, padx = 3, sticky="w")
		ent_aines11 = AutocompleteEntry(nimet, self)
		lbl_maara11 = ttk.Label(self, text="Määrä:")
		ent_maara11 = ttk.Entry(self, width=20)
		ent_aines11.grid(row=14, column=3, padx = 3, sticky="w")
		lbl_maara11.grid(row=14, column=4, sticky="e")
		ent_maara11.grid(row=14, column=5, padx = 3, sticky="w")
		ent_aines12 = AutocompleteEntry(nimet, self)
		lbl_maara12 = ttk.Label(self, text="Määrä:")
		ent_maara12 = ttk.Entry(self, width=20)
		ent_aines12.grid(row=15, column=3, padx = 3, sticky="w")
		lbl_maara12.grid(row=15, column=4, sticky="e")
		ent_maara12.grid(row=15, column=5, padx = 3, sticky="w")
		ent_aines13 = AutocompleteEntry(nimet, self)
		lbl_maara13 = ttk.Label(self, text="Määrä:")
		ent_maara13 = ttk.Entry(self, width=20)
		ent_aines13.grid(row=16, column=3, padx = 3, sticky="w")
		lbl_maara13.grid(row=16, column=4, sticky="e")
		ent_maara13.grid(row=16, column=5, padx = 3, sticky="w")
		ent_aines14 = AutocompleteEntry(nimet, self)
		lbl_maara14 = ttk.Label(self, text="Määrä:")
		ent_maara14 = ttk.Entry(self, width=20)
		ent_aines14.grid(row=17, column=3, padx = 3, sticky="w")
		lbl_maara14.grid(row=17, column=4, sticky="e")
		ent_maara14.grid(row=17, column=5, padx = 3, sticky="w")
		ent_aines15 = AutocompleteEntry(nimet, self)
		lbl_maara15 = ttk.Label(self, text="Määrä:")
		ent_maara15 = ttk.Entry(self, width=20)
		ent_aines15.grid(row=18, column=3, padx = 3, sticky="w")
		lbl_maara15.grid(row=18, column=4, sticky="e")
		ent_maara15.grid(row=18, column=5, padx = 3, sticky="w")
		lbl_empty = ttk.Label(self)
		lbl_empty.grid(row=19, column=4, pady = 15, sticky="ew")


		clickbutton = ttk.Button(self, text="Tallenna")
		def handle_click(event):
			print("Tallennettu!")
			ruoka = ent_resepti.get()
			ruoka = ruoka.capitalize()
			annokset = ent_annoksia.get()
			annokset = int(annokset)
			print(f"{ruoka}, {annokset} annosta.")
			db = sql.connect("database.db")
			db.execute(f'Insert into Reseptit (resepti, annoksia) values ("{ruoka}", {annokset})')
			id = db.execute(f'Select id from Reseptit where resepti="{ruoka}"').fetchone()
			resepti_id = int(id[0])
			ainesosat = []
			ainesosa1_nimi = ent_aines1.get()
			ainesosa1_maara = ent_maara1.get()
			if ainesosa1_maara != "":
				ainesosa1_maara = ainesosa1_maara.replace(",", ".")
				ainesosa1_maara = float(ainesosa1_maara)
			ainesosatTuple = (ainesosa1_nimi.capitalize(), ainesosa1_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa2_nimi = ent_aines2.get()
			ainesosa2_maara = ent_maara2.get()
			if ainesosa2_maara != "":
				ainesosa2_maara = ainesosa2_maara.replace(",", ".")
				ainesosa2_maara = float(ainesosa2_maara)
			ainesosatTuple = (ainesosa2_nimi.capitalize(), ainesosa2_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa3_nimi = ent_aines3.get()
			ainesosa3_maara = ent_maara3.get()
			if ainesosa3_maara != "":
				ainesosa3_maara = ainesosa3_maara.replace(",", ".")
				ainesosa3_maara = float(ainesosa3_maara)
			ainesosatTuple = (ainesosa3_nimi.capitalize(), ainesosa3_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa4_nimi = ent_aines4.get()
			ainesosa4_maara = ent_maara4.get()
			if ainesosa4_maara != "":
				ainesosa4_maara = ainesosa4_maara.replace(",", ".")
				ainesosa4_maara = float(ainesosa4_maara)
			ainesosatTuple = (ainesosa4_nimi.capitalize(), ainesosa4_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa5_nimi = ent_aines5.get()
			ainesosa5_maara = ent_maara5.get()
			if ainesosa5_maara != "":
				ainesosa5_maara = ainesosa5_maara.replace(",", ".")
				ainesosa5_maara = float(ainesosa5_maara)
			ainesosatTuple = (ainesosa5_nimi.capitalize(), ainesosa5_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa6_nimi = ent_aines6.get()
			ainesosa6_maara = ent_maara6.get()
			if ainesosa6_maara != "":
				ainesosa6_maara = ainesosa6_maara.replace(",", ".")
				ainesosa6_maara = float(ainesosa6_maara)
			ainesosatTuple = (ainesosa6_nimi.capitalize(), ainesosa6_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa7_nimi = ent_aines7.get()
			ainesosa7_maara = ent_maara7.get()
			if ainesosa7_maara != "":
				ainesosa7_maara = ainesosa7_maara.replace(",", ".")
				ainesosa7_maara = float(ainesosa7_maara)
			ainesosatTuple = (ainesosa7_nimi.capitalize(), ainesosa7_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa8_nimi = ent_aines8.get()
			ainesosa8_maara = ent_maara8.get()
			if ainesosa8_maara != "":
				ainesosa8_maara = ainesosa8_maara.replace(",", ".")
				ainesosa8_maara = float(ainesosa8_maara)
			ainesosatTuple = (ainesosa8_nimi.capitalize(), ainesosa8_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa9_nimi = ent_aines9.get()
			ainesosa9_maara = ent_maara9.get()
			if ainesosa9_maara != "":
				ainesosa9_maara = ainesosa9_maara.replace(",", ".")
				ainesosa9_maara = float(ainesosa9_maara)
			ainesosatTuple = (ainesosa9_nimi.capitalize(), ainesosa9_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa10_nimi = ent_aines10.get()
			ainesosa10_maara = ent_maara10.get()
			if ainesosa10_maara != "":
				ainesosa10_maara = ainesosa10_maara.replace(",", ".")
				ainesosa10_maara = float(ainesosa10_maara)
			ainesosatTuple = (ainesosa10_nimi.capitalize(), ainesosa10_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa11_nimi = ent_aines11.get()
			ainesosa11_maara = ent_maara11.get()
			if ainesosa11_maara != "":
				ainesosa11_maara = ainesosa11_maara.replace(",", ".")
				ainesosa11_maara = float(ainesosa11_maara)
			ainesosatTuple = (ainesosa11_nimi.capitalize(), ainesosa11_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa12_nimi = ent_aines12.get()
			ainesosa12_maara = ent_maara12.get()
			if ainesosa12_maara != "":
				ainesosa12_maara = ainesosa12_maara.replace(",", ".")
				ainesosa12_maara = float(ainesosa12_maara)
			ainesosatTuple = (ainesosa12_nimi.capitalize(), ainesosa12_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa13_nimi = ent_aines13.get()
			ainesosa13_maara = ent_maara13.get()
			if ainesosa13_maara != "":
				ainesosa13_maara = ainesosa13_maara.replace(",", ".")
				ainesosa13_maara = float(ainesosa13_maara)
			ainesosatTuple = (ainesosa13_nimi.capitalize(), ainesosa13_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa14_nimi = ent_aines14.get()
			ainesosa14_maara = ent_maara14.get()
			if ainesosa14_maara != "":
				ainesosa14_maara = ainesosa14_maara.replace(",", ".")
				ainesosa14_maara = float(ainesosa14_maara)
			ainesosatTuple = (ainesosa14_nimi.capitalize(), ainesosa14_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			ainesosa15_nimi = ent_aines15.get()
			ainesosa15_maara = ent_maara15.get()
			if ainesosa15_maara != "":
				ainesosa15_maara = ainesosa15_maara.replace(",", ".")
				ainesosa15_maara = float(ainesosa15_maara)
			ainesosatTuple = (ainesosa15_nimi.capitalize(), ainesosa15_maara)
			if ainesosatTuple[0] != "":
				ainesosat.append(ainesosatTuple)
			for aines in ainesosat:
				if aines[0] == "":
					print("Tyhjä!")
				if aines[1] == "":
					db.execute(f'Insert into Ainesosat (nimi, resepti) values ("{aines[0]}", {resepti_id})')
				else:
					db.execute(f'Insert into Ainesosat (nimi, resepti, kpl) values ("{aines[0]}", {resepti_id}, {aines[1]})')
			db.commit()
			db.close()
			ent_resepti.delete(0, tk.END)
			ent_annoksia.delete(0, tk.END)
			ent_aines1.delete(0, tk.END)
			ent_maara1.delete(0, tk.END)
			ent_aines2.delete(0, tk.END)
			ent_maara2.delete(0, tk.END)
			ent_aines3.delete(0, tk.END)
			ent_maara3.delete(0, tk.END)
			ent_aines4.delete(0, tk.END)
			ent_maara4.delete(0, tk.END)
			ent_aines5.delete(0, tk.END)
			ent_maara5.delete(0, tk.END)
			ent_aines6.delete(0, tk.END)
			ent_maara6.delete(0, tk.END)
			ent_aines7.delete(0, tk.END)
			ent_maara7.delete(0, tk.END)
			ent_aines8.delete(0, tk.END)
			ent_maara8.delete(0, tk.END)
			ent_aines9.delete(0, tk.END)
			ent_maara9.delete(0, tk.END)
			ent_aines10.delete(0, tk.END)
			ent_maara10.delete(0, tk.END)
			ent_aines11.delete(0, tk.END)
			ent_maara11.delete(0, tk.END)
			ent_aines12.delete(0, tk.END)
			ent_maara12.delete(0, tk.END)
			ent_aines13.delete(0, tk.END)
			ent_maara13.delete(0, tk.END)
			ent_aines14.delete(0, tk.END)
			ent_maara14.delete(0, tk.END)
			ent_aines15.delete(0, tk.END)
			ent_maara15.delete(0, tk.END)

		clickbutton.grid(row=3, column=4)
		clickbutton.bind("<Button-1>", handle_click)
