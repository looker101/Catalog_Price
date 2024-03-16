# SENZA BARRA
import pandas as pd
try:
    # leggi il file
    adidas_sport = pd.read_excel("sp.xlsx")

    # definisco la funzione per lo sconto
    def sport(x):
        return round(x * 0.7)

    #conversione integri in float
    adidas_sport["Variant Price"] = adidas_sport["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    adidas_sport[["Variant Price" ,"Variant Compare At Price"]] = adidas_sport[["Variant Price" ,"Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    adidas_sport["Variant Price"] = adidas_sport["Variant Compare At Price"].apply(sport)

    # tutte le celle della colonna "Compare at price" saranno vuote (in modo da non mostrare la barra)
    adidas_sport["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    adidas_sport["Variant Price"] = adidas_sport["Variant Price"].apply(arrotondamento)

    # Template suffix
    adidas_sport["Template Suffix"] = "Default product"
    #adidas_sport["Template Suffix"] = adidas_sport["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    adidas_sport["Tags"] = adidas_sport["Tags"].str.replace("available now,","")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'adidas_sport_ok.xlsx'

    file = adidas_sport.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Catalogo Adidas Sport aggiornato correttamente!")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito sp.xlsx (Adidas Sport)")

#except Exception as err:
#    print(f"C'è qualcosa che non va:{err}")