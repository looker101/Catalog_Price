# SENZA BARRA
import pandas as pd
try:
    david_beckham = pd.read_excel("db.xlsx")


    def dbe(x):
        return round(x * 0.65)

    david_beckham["Variant Price"].astype("float64")

    david_beckham[["Variant Price", "Variant Compare At Price"]] = david_beckham[["Variant Price", "Variant Compare At Price"]].fillna(0)

    david_beckham["Variant Price"] = david_beckham["Variant Compare At Price"].apply(dbe)

    david_beckham["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    david_beckham["Variant Price"] = david_beckham["Variant Price"].apply(arrotondamento)

    #Template Suffix
    david_beckham["Template Suffix"] = "Default product"
    #david_beckham["Template Suffix"] = david_beckham["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    david_beckham["Tags"] = david_beckham["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'david_beckham_ok.xlsx'

    file = david_beckham.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito db.xlsx (David Beckham)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")