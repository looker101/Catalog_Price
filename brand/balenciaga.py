# CON BARRA
import pandas as pd
try:

    # leggo il file
    balenciaga = pd.read_excel("balenciaga.xlsx")

    # definisco la funzione per lo sconto
    def bale(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    balenciaga["Variant Price"] = balenciaga["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    balenciaga[["Variant Price", "Variant Compare At Price"]] = balenciaga[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    balenciaga["Variant Price"] = balenciaga["Variant Compare At Price"].apply(bale)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    balenciaga["Variant Price"] = balenciaga["Variant Price"].apply(arrotondamento)

    # Template Suffix
    balenciaga["Template Suffix"] = "Default product"
    #balenciaga["Template Suffix"] = balenciaga["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    balenciaga["Tags"] = balenciaga["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'bale_ok.xlsx'

    file = balenciaga.to_excel(salva, index=False)

    print(__name__)
except FileNotFoundError as err:
    print("Non hai inserito balenciaga.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")