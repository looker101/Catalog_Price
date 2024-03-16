import pandas as pd
try:
    gucci = pd.read_excel("gucci.xlsx")

    def gg(x):
        return round(x * 0.7)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    gucci["Variant Price"] = gucci["Variant Price"].astype("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    gucci[["Variant Price", "Variant Compare At Price"]] = gucci[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    gucci["Variant Price"] = gucci["Variant Compare At Price"].apply(gg)

    # Template Suffix
    gucci["Template Suffix"] = "Default product"
    #gucci["Template Suffix"] = gucci["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    gucci["Tags"] = gucci["Tags"].str.replace("available now,", "")

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    gucci["Variant Price"] = gucci["Variant Price"].apply(arrotondamento)

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "gucci_ok.xlsx"

    file = gucci.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito gucci.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")