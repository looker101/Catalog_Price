import pandas as pd
try:

    dolce_gabbana = pd.read_excel("dg.xlsx")

    def dolce(x):
        return round(x * 0.65)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    dolce_gabbana["Variant Price"] = dolce_gabbana["Variant Price"].astype("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    dolce_gabbana[["Variant Price", "Variant Compare At Price"]] = dolce_gabbana[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    dolce_gabbana["Variant Price"] = dolce_gabbana["Variant Compare At Price"].apply(dolce)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    dolce_gabbana["Variant Price"] = dolce_gabbana["Variant Price"].apply(arrotondamento)

    #Template Suffix
    dolce_gabbana["Template Suffix"] = "Default product"
    #dolce_gabbana["Template Suffix"] = dolce_gabbana["Template Suffix"].fillna("Default product")

    #Tolgo il tag "available now,"
    dolce_gabbana["Tags"] = dolce_gabbana["Tags"].str.replace("available now,", "")

    # salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'dolce_gabbana_ok.xlsx'

    file = dolce_gabbana.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito dg.xlsx (Dolce & Gabbana)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")