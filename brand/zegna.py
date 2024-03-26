# CON BARRA

import pandas as pd
try:
    zegna = pd.read_excel("zegna.xlsx")

    def Ermenezegna(x):
        return round(x * 0.65)

    zegna["Variant Price"] = zegna["Variant Price"].astype("float64")

    zegna[["Variant Price", "Variant Compare At Price"]] = zegna[["Variant Price", "Variant Compare At Price"]].fillna(0)

    zegna["Variant Price"] = zegna["Variant Compare At Price"].apply(Ermenezegna)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    zegna["Variant Price"] = zegna["Variant Price"].apply(arrotondamento)

    # Template Suffix
    zegna["Template Suffix"] = "Default product"
    #zegna["Template Suffix"] = zegna["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    zegna["Tags"] = zegna["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'zegna_ok.xlsx'

    file = zegna.to_excel(salva, index=False)

    if __name__ == "__main__":
        print(f"Zegna aggiornato correttamente nella directory {directory}")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito zegna.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")