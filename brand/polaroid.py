import pandas as pd
try:
    polaroid = pd.read_excel("pld.xlsx")

    def pola(x):
        return round(x * 0.65)

    polaroid["Variant Price"] = polaroid["Variant Price"].astype("float64")

    polaroid[["Variant Price", "Variant Compare At Price"]] = polaroid[["Variant Price", "Variant Compare At Price"]].fillna(0)

    polaroid["Variant Price"] = polaroid["Variant Compare At Price"].apply(pola)

    polaroid["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    polaroid["Variant Price"] = polaroid["Variant Price"].apply(arrotondamento)

    # Template Suffix
    polaroid["Template Suffix"] = "Default product"
    #polaroid["Template Suffix"] = polaroid["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    polaroid["Tags"] = polaroid["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'pld_ok.xlsx'

    file = polaroid.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito pld.xlsx (Polaroid)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")