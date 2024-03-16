# CON BARRA
import pandas as pd
try:
    # leggo il file
    vogue = pd.read_excel("vogue.xlsx")

    # definisco la funzione per lo sconto
    def vo(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    vogue["Variant Price"] = vogue["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    vogue[["Variant Price", "Variant Compare At Price"]] = vogue[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    vogue["Variant Price"] = vogue["Variant Compare At Price"].apply(vo)

    # tolgo la barra eliminando i valori sotto la colonna "Variant compare at price"
    vogue["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    vogue["Variant Price"] = vogue["Variant Price"].apply(arrotondamento)

    # Template Suffix
    vogue["Template Suffix"] = "Default product"
    #vogue["Template Suffix"] = vogue["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    vogue["Tags"] = vogue["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'vogue_ok.xlsx'

    file = vogue.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito vogue.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")