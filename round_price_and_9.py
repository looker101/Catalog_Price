# funzione > o < di 200
def arrotondamento(x):
    if x > 200:
        return round(x, -1)
    else:
        return int(str(x)[:-1] + '9')

brand_name["Variant Price"] = brand_name["Variant Price"].apply(arrotondamento)
