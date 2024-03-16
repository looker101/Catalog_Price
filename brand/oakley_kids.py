import pandas as pd
try:
    oak_kids = pd.read_excel("oakley_kids.xlsx")

    def oak_kid(x):
        return round(x * 0.80)

    oak_kids["Variant Price"] = oak_kids["Variant Price"].astype("float64")

    oak_kids[["Variant Price", "Variant Compare At Price"]] = oak_kids[["Variant Price", "Variant Compare At Price"]].fillna(0)

    oak_kids["Variant Price"] = oak_kids["Variant Compare At Price"].apply(oak_kid)

    oak_kids["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    oak_kids["Variant Price"] = oak_kids["Variant Price"].apply(arrotondamento)

    # Template Suffix
    oak_kids["Template Suffix"] = "Default product"
    #oak_kids["Template Suffix"] = oak_kids["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,":
    oak_kids["Tags"] = oak_kids["Tags"].str.replace("available now,", "")

    # salvataggio

    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "oak_kids_ok.xlsx"

    file = oak_kids.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito oakley_kids.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")