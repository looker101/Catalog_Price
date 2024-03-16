import pandas as pd
import math

# leggi il file Excel
df = pd.read_excel('sl.xlsx')

# definisci una funzione che applica lo sconto
def apply_discount(x):
    return x * 0.65

# crea la colonna "price ok" con i prezzi scontati
df['Variant Price'] = df['Variant Compare At Price'].apply(apply_discount)

# sostituisci i valori NaN nella colonna "Variant Price" con 0
df['Variant Price'] = df['Variant Price'].fillna(0)

#arronda i valori presenti nella colonna "variant price"
df['Variant Price'] = df['Variant Price'].apply(lambda x: math.ceil(x) if x != 0 else 0)

# valori template suffix NaN sostituiti con 'Default product'
df['Template Suffix'] = df['Template Suffix'].fillna('Default product')

# salva il DataFrame in un nuovo file Excel
df.to_excel("sl_ok.xlsx", index=False)

# visualizza il DataFrame risultante
print(df)
