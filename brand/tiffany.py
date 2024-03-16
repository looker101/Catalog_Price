# CON BARRA
import pandas as pd
try:
    # leggo il file
    tiffany = pd.read_excel("tiffany.xlsx")

    # definisco la funzione per lo sconto
    def tif(x):
        return round(x * 0.65)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    tiffany["Variant Price"] = tiffany  ["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    tiffany[["Variant Price", "Variant Compare At Price"]] = tiffany[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    tiffany["Variant Price"] = tiffany["Variant Compare At Price"].apply(tif)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    tiffany["Variant Price"] = tiffany  ["Variant Price"].apply(arrotondamento)

    # Template Suffix
    tiffany["Template Suffix"] = "Default product"
    #tiffany["Template Suffix"] = tiffany["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    tiffany["Tags"] = tiffany["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'tiffany_ok.xlsx'

    file = tiffany .to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito tiffany.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")