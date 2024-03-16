# SENZA BARRA
import pandas as pd
try:
    carrera = pd.read_excel("carrera.xlsx")

    def ca(x):
        return round(x * 0.7)

    carrera["Variant Price"] = carrera["Variant Price"].astype("float64")

    carrera[["Variant Price", "Variant Compare At Price"]] = carrera[["Variant Price", "Variant Compare At Price"]].fillna(0)

    carrera["Variant Price"] = carrera["Variant Compare At Price"].apply(ca)

    carrera["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    carrera["Variant Price"] = carrera["Variant Price"].apply(arrotondamento)

    #Template Suffix
    carrera["Template Suffix"] = "Default product"
    #carrera["Template Suffix"] = carrera["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    carrera["Tags"] = carrera["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "carrera_ok.xlsx"

    file = carrera.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito carrera.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")
