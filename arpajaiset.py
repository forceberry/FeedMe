import sqlite3 as sql
import random

def arpajaiset(arvottavat):
    db = sql.connect("database.db")
    data = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
    annoksia2 = []
    annoksia3 = []
    annoksia4 = []
    arvotut = []
    for resepti in data:
        if resepti[2] == 2:
            annoksia2.append(resepti)
        if resepti[2] == 3:
            annoksia3.append(resepti)
        if resepti[2] > 3:
            annoksia4.append(resepti)
    print(data)
    print(arvottavat)
    for _ in range(arvottavat[0]):
        try:
            rand = random.randint(0, len(annoksia2)-1)
        except:
            print("Liian vähän sopivia reseptejä!")
        resepti = annoksia2.pop(rand)
        arvotut.append(resepti)
    for _ in range(arvottavat[1]):
        try:
            rand = random.randint(0, len(annoksia3)-1)
        except:
            print("Liian vähän sopivia reseptejä!")
        resepti = annoksia3.pop(rand)
        arvotut.append(resepti)
    for _ in range(arvottavat[2]):
        try:
            rand = random.randint(0, len(annoksia4)-1)
        except:
            print("Liian vähän sopivia reseptejä!")
        resepti = annoksia4.pop(rand)
        arvotut.append(resepti)
    print(arvotut)
    return(arvotut)

