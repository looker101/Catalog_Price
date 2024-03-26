
import pandas as pd
try:
    web = pd.read_excel("web.xlsx")

    def webEyewear(x):
        return round(x * 0.65)

    web["Variant Price"] = web["Variant Price"].astype("float64")

    web[["Variant Price", "Variant Compare At Price"]] = web[["Variant Price", "Variant Compare At Price"]].fillna(0)

    web["Variant Price"] = web["Variant Compare At Price"].apply(webEyewear)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    web["Variant Price"] = web["Variant Price"].apply(arrotondamento)

    # Template Suffix
    web["Template Suffix"] = "Default product"
    #web["Template Suffix"] = web["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    web["Tags"] = web["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'web_ok.xlsx'

    file = web.to_excel(salva, index=False)

    if __name__ == "__main__":
        print(f"web aggiornato correttamente nella directory {directory}")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito web.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")