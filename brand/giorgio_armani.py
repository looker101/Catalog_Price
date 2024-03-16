import pandas as pd
try:
    giorgio_armani = pd.read_excel("giorgio.xlsx")

    def ga(x):
        return round(x * 0.65)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    giorgio_armani["Variant Price"] = giorgio_armani["Variant Price"].astype("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    giorgio_armani[["Variant Price", "Variant Compare At Price"]] = giorgio_armani[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    giorgio_armani["Variant Price"] = giorgio_armani["Variant Compare At Price"].apply(ga)

    # Template Suffix
    giorgio_armani["Template Suffix"] = "Default product"
    #giorgio_armani["Template Suffix"] = giorgio_armani["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    giorgio_armani["Tags"] = giorgio_armani["Tags"].str.replace("available now," , "")

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    giorgio_armani["Variant Price"] = giorgio_armani["Variant Price"].apply(arrotondamento)

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "giorgio_armani_ok.xlsx"

    file = giorgio_armani.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Aggiornato il catalogo di Giorgio Armani")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito giorgio_armani.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")