# CON BARRA

import pandas as pd
try:
    tom_ford = pd.read_excel("ft.xlsx")

    def tom(x):
        return round(x * 0.65)

    tom_ford["Variant Price"] = tom_ford["Variant Price"].astype("float64")

    tom_ford[["Variant Price", "Variant Compare At Price"]] = tom_ford[["Variant Price", "Variant Compare At Price"]].fillna(0)

    tom_ford["Variant Price"] = tom_ford["Variant Compare At Price"].apply(tom)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    tom_ford["Variant Price"] = tom_ford["Variant Price"].apply(arrotondamento)

    # Template Suffix
    tom_ford["Template Suffix"] = "Default product"
    #tom_ford["Template Suffix"] = tom_ford["Template Suffix"].fillna("Default product")

    #tolgo il tag "available now,"
    tom_ford["Tags"] = tom_ford["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'ft_ok.xlsx'

    file = tom_ford.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito ft.xlsx (Tom Ford)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")