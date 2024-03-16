# CON BARRA
import pandas as pd
try:

    # leggo il file
    arnette = pd.read_excel("arnette.xlsx")

    # definisco la funzione per lo sconto
    def ant(x):
        return round(x * 0.7)
 
    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    arnette["Variant Price"] = arnette["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    arnette[["Variant Price", "Variant Compare At Price"]] = arnette[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    arnette["Variant Price"] = arnette["Variant Compare At Price"].apply(ant)

    arnette["Variant Compare At Price"] = ''

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    arnette["Variant Price"] = arnette["Variant Price"].apply(arrotondamento)

    # Template Suffix
    arnette["Template Suffix"] = "Default product"
    #arnette["Template Suffix"] = arnette["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    arnette["Tags"] = arnette["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'arnette_ok.xlsx'

    file = arnette.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito arnette.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")
