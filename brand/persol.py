import pandas as pd
try:
    persol = pd.read_excel("persol.xlsx")

    def po(x):
        return round(x * 0.80)

    persol["Variant Price"] = persol["Variant Price"].astype("float64")

    persol[["Variant Price", "Variant Compare At Price"]] = persol[["Variant Price", "Variant Compare At Price"]].fillna(0)

    persol["Variant Price"] = persol["Variant Compare At Price"].apply(po)

    persol["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    persol["Variant Price"] = persol["Variant Price"].apply(arrotondamento)

    # Template Suffix
    persol["Template Suffix"] = "Default product"
    #persol["Template Suffix"] = persol["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    persol["Tags"] = persol["Tags"].str.replace("available now,", "")

    # salvataggio

    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "persol_ok.xlsx"

    file = persol.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito persol.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")