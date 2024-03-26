# CON BARRA

import pandas as pd
try:
    pucci = pd.read_excel("pucci.xlsx")

    def emilioPucci(x):
        return round(x * 0.65)

    pucci["Variant Price"] = pucci["Variant Price"].astype("float64")

    pucci[["Variant Price", "Variant Compare At Price"]] = pucci[["Variant Price", "Variant Compare At Price"]].fillna(0)

    pucci["Variant Price"] = pucci["Variant Compare At Price"].apply(emilioPucci)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    pucci["Variant Price"] = pucci["Variant Price"].apply(arrotondamento)

    # Template Suffix
    pucci["Template Suffix"] = "Default product"
    #pucci["Template Suffix"] = pucci["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    pucci["Tags"] = pucci["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'pucci_ok.xlsx'

    file = pucci.to_excel(salva, index=False)

    if __name__ == "__main__":
        print(f"Pucci aggiornato correttamente nella directory {directory}")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito pucci.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")