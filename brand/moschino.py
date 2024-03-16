import pandas as pd
try:
    moschino = pd.read_excel("moschino.xlsx")

    def mos(x):
        return round(x * 0.7)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    moschino["Variant Price"] = moschino["Variant Price"].astype("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    moschino[["Variant Price", "Variant Compare At Price"]] = moschino[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    moschino["Variant Price"] = moschino["Variant Compare At Price"].apply(mos)

    # Template Suffix
    moschino["Template Suffix"] = "Default product"
    #moschino["Template Suffix"] = moschino["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    moschino["Tags"] = moschino["Tags"].str.replace("available now,", "")

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    moschino["Variant Price"] = moschino["Variant Price"].apply(arrotondamento)

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "moschino_ok.xlsx"

    file = moschino.to_excel(salva, index=False)

    if __name__ == "__main__":
        print(f"Catalogo Moschino aggiornato correttamente nella directory {directory}")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito moschino.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")