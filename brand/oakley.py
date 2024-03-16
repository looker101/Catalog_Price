import pandas as pd
try:
    oakley = pd.read_excel("oakley.xlsx")

    def oak(x):
        return round(x * 0.80)

    oakley["Variant Price"] = oakley["Variant Price"].astype("float64")

    oakley[["Variant Price", "Variant Compare At Price"]] = oakley[["Variant Price", "Variant Compare At Price"]].fillna(0)

    oakley["Variant Price"] = oakley["Variant Compare At Price"].apply(oak)

    oakley["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    oakley["Variant Price"] = oakley["Variant Price"].apply(arrotondamento)

    # Template Suffix
    oakley["Template Suffix"] = "Default product"
    #oakley["Template Suffix"] = oakley["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    oakley["Tags"] = oakley["Tags"].str.replace("available now,", "")

    # salvataggio

    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "oakley_ok.xlsx"

    file = oakley.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Catalogo Oakley aggiornato correttamente!")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito oakley.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")