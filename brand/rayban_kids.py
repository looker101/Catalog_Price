# SENZA BARRA
import pandas as pd
try:
    rayban_kids = pd.read_excel("rb_kids.xlsx")

    def ray_kid(x):
        return round(x * 0.80)

    rayban_kids["Variant Price"] = rayban_kids["Variant Price"].astype("float64")

    rayban_kids[["Variant Price", "Variant Compare At Price"]] = rayban_kids[["Variant Price", "Variant Compare At Price"]].fillna(0)

    rayban_kids["Variant Price"] = rayban_kids["Variant Compare At Price"].apply(ray_kid)

    rayban_kids["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    rayban_kids["Variant Price"] = rayban_kids["Variant Price"].apply(arrotondamento)

    # Template Suffix
    rayban_kids["Template Suffix"] = "Default product"
    #rayban_kids["Template Suffix"] = rayban_kids["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    rayban_kids["Tags"] = rayban_kids["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "rayban_kids_ok.xlsx"

    file = rayban_kids.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito rb_kids.xlsx (Ray-Ban Kids)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")