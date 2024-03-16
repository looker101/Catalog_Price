import pandas as pd

try:
    marc_jacobs = pd.read_excel("mj.xlsx")

    def marc(x):
        return round(x * 0.65)

    marc_jacobs["Variant Price"] = marc_jacobs["Variant Price"].astype("float64")

    marc_jacobs[["Variant Price", "Variant Compare At Price"]] = marc_jacobs[["Variant Price", "Variant Compare At Price"]].fillna(0)

    marc_jacobs["Variant Price"] = marc_jacobs["Variant Compare At Price"].apply(marc)

    marc_jacobs["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    marc_jacobs["Variant Price"] = marc_jacobs["Variant Price"].apply(arrotondamento)

    #Template suffix
    marc_jacobs["Template Suffix"] = "Default product"
    #marc_jacobs["Template Suffix"] = marc_jacobs["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    marc_jacobs["Template Suffix"] = marc_jacobs["Template Suffix"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "mj_ok.xlsx"

    file = marc_jacobs.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito mj.xlsx (Marc Jacobs)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")