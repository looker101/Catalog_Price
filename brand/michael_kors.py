import pandas as pd

try:
    michael_kors = pd.read_excel("mk.xlsx")

    def mic(x):
        return round(x * 0.65)

    michael_kors["Variant Price"] = michael_kors["Variant Price"].astype("float64")

    michael_kors[["Variant Price", "Variant Compare At Price"]] = michael_kors[["Variant Price", "Variant Compare At Price"]].fillna(0)

    michael_kors["Variant Price"] = michael_kors["Variant Compare At Price"].apply(mic)

    michael_kors["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    michael_kors["Variant Price"] = michael_kors["Variant Price"].apply(arrotondamento)

    #Template suffix
    michael_kors["Template Suffix"] = "Default product"
    #michael_kors["Template Suffix"] = michael_kors["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    michael_kors["Tags"] = michael_kors["Tags"].str.replace("available now,", "")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "mk_ok.xlsx"

    file = michael_kors.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito mk.xlsx (Michael Kors)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")