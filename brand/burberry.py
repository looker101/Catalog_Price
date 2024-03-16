# CON BARRA

import pandas as pd
try:
    burberry = pd.read_excel("burberry.xlsx")
    def be(x):
        return round(x * 0.65)

    burberry["Variant Price"] = burberry["Variant Price"].astype("float64")

    burberry[["Variant Price", "Variant Compare At Price"]] = burberry[["Variant Price", "Variant Compare At Price"]].fillna(0)

    burberry["Variant Price"] = burberry["Variant Compare At Price"].apply(be)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    burberry["Variant Price"] = burberry["Variant Price"].apply(arrotondamento)

    # Template Suffix
    burberry["Template Suffix"] = "Default product"
    #burberry["Template Suffix"] = burberry["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    burberry["Tags"] = burberry["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'burberry_ok.xlsx'

    file = burberry.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("burberry salvato correttamente")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito burberry.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")