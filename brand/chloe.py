# CON BARRA

import pandas as pd
try:
    chloe = pd.read_excel("chloe.xlsx")

    def ch(x):
        return round(x * 0.7)

    chloe["Variant Price"].astype("float64")

    chloe[["Variant Price", "Variant Compare At Price"]] = chloe[["Variant Price", "Variant Compare At Price"]].fillna(0)

    chloe["Variant Price"] = chloe["Variant Compare At Price"].apply(ch)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    chloe["Variant Price"] = chloe["Variant Price"].apply(arrotondamento)

    # Template Suffix
    chloe["Template Suffix"] = "Default product"
    #chloe["Template Suffix"] = chloe["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    chloe["Tags"] = chloe["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'chloe_ok.xlsx'

    file = chloe.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito chloe.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")