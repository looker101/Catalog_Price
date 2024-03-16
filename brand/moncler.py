import pandas as pd
try:
    moncler = pd.read_excel("moncler.xlsx")

    def mon(x):
        return round(x * 0.64)

    moncler["Variant Price"] = moncler["Variant Price"].astype("float64")

    moncler[["Variant Price", "Variant Compare At Price"]] = moncler[["Variant Price", "Variant Compare At Price"]].fillna(0)

    moncler["Variant Price"] = moncler["Variant Compare At Price"].apply(mon)

    def get_price(price):
        if price == 9:
            return 0
            pass
        
    #moncler["Inventory Available: +39 05649689443"] = moncler["Variant Price"].apply(get_price).fillna(5)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    moncler["Variant Price"] = moncler["Variant Price"].apply(arrotondamento)

    #Template suffix
    moncler["Template Suffix"] = "Default product"
    #moncler["Template Suffix"] = moncler["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    moncler["Tags"] = moncler["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "monlcer_ok.xlsx"

    file = moncler.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito moncler.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")