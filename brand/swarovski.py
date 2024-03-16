# CON BARRA
import pandas as pd

try:
    # leggo il file
    swarovski = pd.read_excel("sk.xlsx")

    # definisco la funzione per lo sconto
    def swaro(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    swarovski["Variant Price"] = swarovski["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    swarovski[["Variant Price", "Variant Compare At Price"]] = swarovski[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    swarovski["Variant Price"] = swarovski["Variant Compare At Price"].apply(swaro)

    # tolgo la barra eliminando i valori sotto la colonna "Variant compare at price"
    #swarovski["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    # Template Suffix
    swarovski["Template Suffix"] = "Default product"
    #swarovski["Template Suffix"] = swarovski["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    swarovski["Tags"]  = swarovski["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'sk_ok.xlsx'

    file = swarovski.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito Swarovski")