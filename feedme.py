import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import arvoreseptit
import lisaaresepti
import naytareseptit
import poistaresepti
import ostoslista

db = sql.connect("database.db")
#db.execute("CREATE TABLE Reseptit (id INTEGER PRIMARY KEY, resepti TEXT, annoksia INTEGER)")
#db.execute("CREATE TABLE Ainesosat (id INTEGER PRIMARY KEY, nimi TEXT, resepti INTEGER, kpl REAL)")
#db.commit()

LARGEFONT =("Verdana", 35)

class FeedMe(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting of the different page layouts
		for F in (arvoreseptit.ArvoReseptit, naytareseptit.NaytaReseptit, lisaaresepti.LisaaResepti, poistaresepti.PoistaResepti, ostoslista.Ostoslista):
			frame = F(container, self)
			# initializing frame of that object from startpage, page1, page2 respectively with for loop
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		#self.show_frame(arvoreseptit.ArvoReseptit)
		self.show_frame(ostoslista.Ostoslista)

	# to display the current frame passed as parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# Driver Code
app = FeedMe()
app.title("Feed Me!")
app.mainloop()

#db.execute("Insert into Reseptit (resepti, annoksia) values ('Bataattikeitto', 4)")
reseptit = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
ainekset = db.execute("Select id, nimi, kpl, resepti from Ainesosat").fetchall()
db.close()
print(reseptit)
print(ainekset)
#exit = input()