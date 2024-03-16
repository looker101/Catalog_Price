# CON BARRA

import pandas as pd
try:
    fossil = pd.read_excel("fossil.xlsx")

    def be(x):
        return round(x * 0.7)

    fossil["Variant Price"] = fossil["Variant Price"].astype("float64")

    fossil[["Variant Price", "Variant Compare At Price"]] = fossil[["Variant Price", "Variant Compare At Price"]].fillna(0)

    fossil["Variant Price"] = fossil["Variant Compare At Price"].apply(be)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    fossil["Variant Price"] = fossil["Variant Price"].apply(arrotondamento)

    # Template Suffix
    fossil["Template Suffix"] = "Default product"
    #fossil["Template Suffix"] = fossil["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    fossil["Tags"] = fossil["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'fossil_ok.xlsx'

    file = fossil.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Fossil aggiornato correttamente")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito fossil.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")