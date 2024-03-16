# CON BARRA
import pandas as pd
try:
    # leggo il file
    prada = pd.read_excel("prada.xlsx")

    # definisco la funzione per lo sconto
    def pr(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    prada["Variant Price"] = prada["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    prada[["Variant Price", "Variant Compare At Price"]] = prada[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    prada["Variant Price"] = prada["Variant Compare At Price"].apply(pr)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    prada["Variant Price"] = prada["Variant Price"].apply(arrotondamento)

    # Template Suffix
    prada["Template Suffix"] = "Default product"
    #prada["Template Suffix"] = prada["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    prada["Tags"] = prada["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'prada_ok.xlsx'

    file = prada.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito prada.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")