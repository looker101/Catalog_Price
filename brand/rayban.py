# SENZA BARRA
import pandas as pd
try:
    rayban = pd.read_excel("rb.xlsx")

    def ray(x):
        return round(x * 0.80)

    rayban["Variant Price"] = rayban["Variant Price"].astype("float64")

    rayban[["Variant Price", "Variant Compare At Price"]] = rayban[["Variant Price", "Variant Compare At Price"]].fillna(0)

    rayban["Variant Price"] = rayban["Variant Compare At Price"].apply(ray)

    rayban["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    rayban["Variant Price"] = rayban["Variant Price"].apply(arrotondamento)

    # Template Suffix
    rayban["Template Suffix"] = "Default product"
    #rayban["Template Suffix"] = rayban["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    rayban["Tags"] = rayban["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "rayban_ok.xlsx"

    file = rayban.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Catalogo Ray-Ban aggiornato")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito rb.xlsx (Ray-Ban)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")