import pandas as pd
try:

    alexander_mcqueen = pd.read_excel("amq.xlsx")

    def mcqueen(x):
        return round(x * 0.70)

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Price"].astype("float64")

    alexander_mcqueen[["Variant Price", "Variant Compare At Price"]] = alexander_mcqueen[["Variant Price", "Variant Compare At Price"]].fillna(0)

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Compare At Price"].apply(mcqueen)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Price"].apply(arrotondamento)

    # Tempalte suffix
    alexander_mcqueen["Template Suffix"] = "Default product"
    #alexander_mcqueen["Template Suffix"] = alexander_mcqueen["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    alexander_mcqueen["Tags"] = alexander_mcqueen["Tags"].str.replace("available now,", "")

    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'amq_ok.xlsx'

    file = alexander_mcqueen.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Catalogo Alexander McQueen aggiornato correttamente!")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito amq.xlsx (Alexander McQueen)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")