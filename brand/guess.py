# SENZA BARRA
import pandas as pd
try:
    guess = pd.read_excel("guess.xlsx")

    def gu(x):
        return round(x * 0.65)

    guess["Variant Price"] = guess["Variant Price"].astype("float64")

    guess[["Variant Price", "Variant Compare At Price"]] = guess[["Variant Price", "Variant Compare At Price"]].fillna(0)

    guess["Variant Price"] = guess["Variant Compare At Price"].apply(gu)

    guess["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    guess["Variant Price"] = guess["Variant Price"].apply(arrotondamento)

    #Template Suffix
    guess["Template Suffix"] = "Default product"
    #guess["Template Suffix"] = guess["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    guess["Tags"] = guess["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "guess_ok.xlsx"

    file = guess.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito guess.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")