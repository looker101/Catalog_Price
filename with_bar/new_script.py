# CON BARRA
import pandas as pd

# leggo il file
chiara_ferragni = pd.read_excel("ferragni.xlsx")

# definisco la funzione per lo sconto
def ferragni(x):
    return round(x * 0.6)

# tutti i valori della colonna "Variant Price" li trasfrormo in float64
chiara_ferragni["Variant Price"] = chiara_ferragni["Variant Price"].astype("float64")

# compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
chiara_ferragni[["Variant Price", "Variant Compare At Price"]] = chiara_ferragni[["Variant Price", "Variant Compare At Price"]].fillna(0)

# applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
chiara_ferragni["Variant Price"] = chiara_ferragni["Variant Compare At Price"].apply(ferragni)

# Template Suffix
chiara_ferragni["Template Suffix"] = chiara_ferragni["Template Suffix"].fillna("Default product") 

#Salvataggio
directory = "C:\\Users\\miche\\Desktop\\Test\\BrandScraping\\test_brand2\\ok\\"

salva = directory + 'chiara_ferragni_ok.xlsx'

file = chiara_ferragni.to_excel(salva, index=False)
