# SENZA BARRA
import pandas as pd
try:
    # leggi il file
    tommy_hilfiger = pd.read_excel("tommy.xlsx")

    # definisco la funzione per lo sconto
    def tomhilf(x):
        return round(x * 0.65)

    #conversione interi in flot
    tommy_hilfiger["Variant Price"] = tommy_hilfiger["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    tommy_hilfiger[["Variant Price" ,"Variant Compare At Price"]] = tommy_hilfiger[["Variant Price" ,"Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    tommy_hilfiger["Variant Price"] = tommy_hilfiger["Variant Compare At Price"].apply(tomhilf)

    # tutte le celle della colonna "Compare at price" saranno vuote (in modo da non mostrare la barra)
    tommy_hilfiger["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    tommy_hilfiger["Variant Price"] = tommy_hilfiger["Variant Price"].apply(arrotondamento)

    # template suffix
    tommy_hilfiger["Template Suffix"] = "Default product"
    #tommy_hilfiger["Template Suffix"] = tommy_hilfiger["Template Suffix"].fillna("Default product")

    #tolgo il tag "available now,"
    tommy_hilfiger["Tags"] = tommy_hilfiger["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'tommy_hilfiger_ok.xlsx'

    file = tommy_hilfiger.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Tommy Hilfiger salvato correttamente")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito or.xlsx (Tommy Hilfiger)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")