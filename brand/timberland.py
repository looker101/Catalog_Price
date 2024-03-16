# CON BARRA
import pandas as pd
try:
    # leggo il file
    timberland = pd.read_excel("tb.xlsx")

    # definisco la funzione per lo sconto
    def timbi(x):
        return round(x * 0.65)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    timberland["Variant Price"] = timberland["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    timberland[["Variant Price", "Variant Compare At Price"]] = timberland[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    timberland["Variant Price"] = timberland["Variant Compare At Price"].apply(timbi)

    # tolgo la barra eliminando i valori sotto la colonna "Variant compare at price"
    timberland["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    timberland["Variant Price"] = timberland["Variant Price"].apply(arrotondamento)

    # Template Suffix
    timberland["Template Suffix"] = "Default product"
    #timberland["Template Suffix"] = timberland["Template Suffix"].fillna("Default product")

    #tolgo il tag "available now,"
    timberland["Tags"] = timberland["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'tb_ok.xlsx'

    file = timberland.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito tb.xlsx (Timberland)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")