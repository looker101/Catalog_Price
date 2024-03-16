# CON BARRA

import pandas as pd
try:
    underAmor = pd.read_excel("under_armor.xlsx")

    def under(x):
        return round(x * 0.65)

    underAmor["Variant Price"] = underAmor["Variant Price"].astype("float64")

    underAmor[["Variant Price", "Variant Compare At Price"]] = underAmor[["Variant Price", "Variant Compare At Price"]].fillna(0)

    underAmor["Variant Price"] = underAmor["Variant Compare At Price"].apply(under)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    underAmor["Variant Price"] = underAmor["Variant Price"].apply(arrotondamento)

    # Template Suffix
    underAmor["Template Suffix"] = "Default product"
    #underAmor["Template Suffix"] = underAmor["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    underAmor["Tags"] = underAmor["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'underAmor_ok.xlsx'

    file = underAmor.to_excel(salva, index=False)

    if __name__ == "__main__":
        print(f"underArmor aggiornato correttamente nella directory {directory}")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito underAmor.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")