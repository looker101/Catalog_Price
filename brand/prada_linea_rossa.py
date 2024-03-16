import pandas as pd
try:
    prada_linea_rossa = pd.read_excel("plr.xlsx")

    def linea_rossa(x):
        return round(x * 0.70)

    prada_linea_rossa["Variant Price"] = prada_linea_rossa["Variant Price"].astype("float64")

    prada_linea_rossa[["Variant Price", "Variant Compare At Price"]] = prada_linea_rossa[["Variant Price", "Variant Compare At Price"]].fillna(0)

    prada_linea_rossa["Variant Price"] = prada_linea_rossa["Variant Compare At Price"].apply(linea_rossa)

    prada_linea_rossa["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    prada_linea_rossa["Variant Price"] = prada_linea_rossa["Variant Price"].apply(arrotondamento)

    # Template Suffix
    prada_linea_rossa["Template Suffix"] = "Default product"
    #prada_linea_rossa["Template Suffix"] = prada_linea_rossa["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    prada_linea_rossa["Tags"] = prada_linea_rossa["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'plr_ok.xlsx'

    file = prada_linea_rossa.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Tutto a posto")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito plr.xlsx (Prada Linea Rossa)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")
