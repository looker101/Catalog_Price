# CON BARRA
import pandas as pd
try:

    # leggo il file
    bottega = pd.read_excel("bottega.xlsx")

    # definisco la funzione per lo sconto
    def bott(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    bottega["Variant Price"] = bottega["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    bottega[["Variant Price", "Variant Compare At Price"]] = bottega[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    bottega["Variant Price"] = bottega["Variant Compare At Price"].apply(bott)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    bottega["Variant Price"] = bottega["Variant Price"].apply(arrotondamento)

    # Template Suffix
    bottega["Template Suffix"] = "Default product"
    #bottega["Template Suffix"] = bottega["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    bottega["Tags"] = bottega["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'bottega_ok.xlsx'

    file = bottega.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito bottega.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")