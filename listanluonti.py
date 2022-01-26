import sqlite3 as sql

def ostoslista(reseptit):
    db = sql.connect("database.db")
    data = db.execute("Select id, resepti, annoksia from Reseptit").fetchall()
    indeksit = []
    ainekset = []
    for resepti in reseptit:
        indeksit.append(resepti[0])
    for indeksi in indeksit:
        db = sql.connect("database.db")
        data = db.execute(f"Select nimi, kpl, osasto from Ainesosat where resepti = {indeksi}").fetchall()
        db.close()
        for tulos in data:
            ainesosa = (tulos[0], tulos[1], tulos[2])
            ainekset.append(ainesosa)
    tulosdict = {}
    for aines in ainekset:
        if aines[0] not in tulosdict:
            if aines[1] == None:
                kplJaOsasto = [0, aines[2]]
                tulosdict.update({aines[0]: kplJaOsasto})
            else:
                kplJaOsasto = [aines[1], aines[2]]
                tulosdict.update({aines[0]: kplJaOsasto})
        else:
            if aines[1] != None:
                tulosdict[aines[0]][0] += aines[1]
    tuloste = ""
    i = 0
    while i < 10:
        for element in tulosdict:
            if tulosdict[element][1] == i:
                tuloste += str(element)
                if tulosdict[element][0] != None:
                    if tulosdict[element][0] != 0:
                        if tulosdict[element][0].is_integer():
                            maara = int(tulosdict[element][0])
                            tuloste += f": {maara}"
                        else:
                            maara = round(tulosdict[element][0], 2)
                            tuloste += f": {maara}"
                tuloste += "\n"
        i += 1
    print(tuloste)
    return tuloste

