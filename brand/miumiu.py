# CON BARRA
import pandas as pd
try:
    # leggo il file
    miumiu = pd.read_excel("miumiu.xlsx")

    # definisco la funzione per lo sconto
    def miu(x):
        return round(x * 0.65)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    miumiu["Variant Price"] = miumiu  ["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    miumiu[["Variant Price", "Variant Compare At Price"]] = miumiu[["Variant Price", "Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    miumiu["Variant Price"] = miumiu["Variant Compare At Price"].apply(miu)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '7')

    miumiu["Variant Price"] = miumiu["Variant Price"].apply(arrotondamento)

    # Template Suffix
    #miumiu["Template Suffix"] = miumiu["Template Suffix"].fillna("Default product")
    miumiu["Template Suffix"] = "Default product"

    # Tolgo il tag "available now"
    miumiu["Tags"] = miumiu["Tags"].str.replace("available now,", "")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\.py\catalog_price\ok\\"

    salva = directory + 'miumiu_ok.xlsx'

    file = miumiu .to_excel(salva, index=False)

    if __name__ == "__main__":
        print("Miu Miu salvato correttamente!")
    else:
        print(__name__)   

except FileNotFoundError as err:
    print("Non hai inserito miumiu.xlsx (Miu Miu)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")