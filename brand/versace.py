# CON BARRA

import pandas as pd
try:
    versace = pd.read_excel("versace.xlsx")

    def ver(x):
        return round(x * 0.65)

    versace["Variant Price"] = versace["Variant Price"].astype("float64")

    versace[["Variant Price", "Variant Compare At Price"]] = versace[["Variant Price", "Variant Compare At Price"]].fillna(0)

    versace["Variant Price"] = versace["Variant Compare At Price"].apply(ver)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    versace["Variant Price"] = versace["Variant Price"].apply(arrotondamento)

    # Template Suffix
    versace["Template Suffix"] = "Default product"
    #versace["Template Suffix"] = versace["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    versace["Tags"] = versace["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"
    
    salva = directory + 'versace_ok.xlsx'

    file = versace.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito versace.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")