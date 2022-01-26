import lisaaresepti
import naytareseptit
import ostoslista
from listanluonti import ostoslista as ol
import tkinter as tk
from tkinter import ttk
from arpajaiset import arpajaiset

LARGEFONT =("Verdana", 20)

class ArvoReseptit(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Arvo reseptit", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)

		# button to show frame 2 with text layout2
		button1 = ttk.Button(self, text ="Luo ostoslista",
        command = lambda : controller.show_frame(ostoslista.Ostoslista))
	
		# putting the button in its place by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky="ew")
        
		button2 = ttk.Button(self, text ="Arvo reseptit")
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky="ew")

		button3 = ttk.Button(self, text ="Näytä kaikki reseptit",
		command = lambda : controller.show_frame(naytareseptit.NaytaReseptit))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky="ew")

		## button to show frame 2 with text layout2
		button4 = ttk.Button(self, text ="Lisää Resepti",
		command = lambda : controller.show_frame(lisaaresepti.LisaaResepti))
	
		# putting the button in its place by
		# using grid
		button4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky="ew")

		lbl_annoksia2 = ttk.Label(self, text="Kahden annoksen reseptejä:")
		ent_annoksia2 = ttk.Entry(self, width=4)

		lbl_annoksia3 = ttk.Label(self, text="Kolmen annoksen reseptejä:")
		ent_annoksia3 = ttk.Entry(self, width=4)

		lbl_annoksia4 = ttk.Label(self, text="Neljän annoksen reseptejä:")
		ent_annoksia4 = ttk.Entry(self, width=4)

		reseptit = []
		ostokset = ""

		def ostosclick(event, reseptit):
			lista = ol(reseptit)
			lbl_ostoslista.config(text=lista)

		savebutton = ttk.Button(self, text="Arvo reseptit")
		def handle_click(event):
			annoksia2 = ent_annoksia2.get()
			annoksia3 = ent_annoksia3.get()
			annoksia4 = ent_annoksia4.get()
			if annoksia2.isnumeric():
				annoksia2 = int(annoksia2)
			else:
				annoksia2 = 0
			if annoksia3.isnumeric():
				annoksia3 = int(annoksia3)
			else:
				annoksia3 = 0
			if annoksia4.isnumeric():
				annoksia4 = int(annoksia4)
			else:
				annoksia4 = 0
			tulos = (annoksia2, annoksia3, annoksia4)
			print(f"Arvottu! {annoksia2} kahden annoksen, {annoksia3} kolmen annoksen ja {annoksia4} neljän annoksen reseptejä.")
			reseptit = arpajaiset(tulos)
			reseptitxt = ""
			for resepti in reseptit:
				reseptitxt += f"{resepti[1]}\n"
			lbl_reseptit.config(text=reseptitxt)
			luoLista = ttk.Button(self, text="Luo ostoslista")
			luoLista.bind("<Button-1>", ostosclick(event, reseptit))
			luoLista.grid(row=2, column=4)

		lbl_reseptit = ttk.Label(self, text=reseptit)
		lbl_reseptit.grid(row = 4, column = 2, columnspan=5, rowspan=15, sticky="w")

		lbl_ostoslista = ttk.Label(self, text=ostokset)
		lbl_ostoslista.grid(row = 1, column = 5, padx=10, columnspan=5, rowspan=50)

		lbl_annoksia2.grid(row=1, column=2, sticky="e")
		ent_annoksia2.grid(row=1, column=3, padx = 3, sticky="w")

		lbl_annoksia3.grid(row=2, column=2, sticky="e")
		ent_annoksia3.grid(row=2, column=3, padx = 3, sticky="w")

		lbl_annoksia4.grid(row=3, column=2, sticky="e")
		ent_annoksia4.grid(row=3, column=3, padx = 3, sticky="w")

		savebutton.grid(row=1, column=4)
		savebutton.bind("<Button-1>", handle_click)