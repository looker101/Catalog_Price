import pandas as pd
try:
    emporio_armani = pd.read_excel("emporio.xlsx")

    def empo(x):
        return round(x * 0.7)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    emporio_armani["Variant Price"] = emporio_armani["Variant Price"].astype("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    emporio_armani[["Variant Price", "Variant Compare At Price"]] = emporio_armani[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    emporio_armani["Variant Price"] = emporio_armani["Variant Compare At Price"].apply(empo)

    # Template Suffix
    emporio_armani["Template Suffix"] = "Default product"
    #emporio_armani["Template Suffix"] = emporio_armani["Template Suffix"].fillna("Default product")

    # Tolgo il tag "available now,"
    emporio_armani["Tags"] = emporio_armani["Tags"].str.replace("available now,", "")

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    emporio_armani["Variant Price"] = emporio_armani["Variant Price"].apply(arrotondamento)

    #salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + "emporio_armani_ok.xlsx"

    file = emporio_armani.to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Emporio Armani salvato correttamente")
    else:
        print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito emporio_armani.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")