# SENZA BARRA
import pandas as pd
try:
    # leggi il file
    kate_spade = pd.read_excel("spade.xlsx")

    # definisco la funzione per lo sconto
    def kateSpade(x):
        return round(x * 0.65)

    #conversione interi in flot
    kate_spade["Variant Price"] = kate_spade["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    kate_spade[["Variant Price" ,"Variant Compare At Price"]] = kate_spade[["Variant Price" ,"Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    kate_spade["Variant Price"] = kate_spade["Variant Compare At Price"].apply(kateSpade)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    kate_spade["Variant Price"] = kate_spade["Variant Price"].apply(arrotondamento)

    #Template Suffix
    kate_spade["Template Suffix"] = "Default product"
    #kate_spade["Template Suffix"] = kate_spade["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    kate_spade["Tags"] = kate_spade["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'kate_spade_ok.xlsx'

    file = kate_spade.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Kate Spade salvato correttamente")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito or.xlsx (Kate Spade)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")
