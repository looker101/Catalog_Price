import pandas as pd

# Shopify si riferisce al file estrpolato dal Shopify
# negozi si rifersce al file estrapolato da Focus (quantità di pezzi nei negozi)

try:
    class Off_White:
        def __init__(self, file_negozi, file_shopify):
            self.file_negozi = file_negozi
            self.file_shopify = file_shopify
            
        # creo il modulo bottega e assemblo il file relativo ai prodotto nei negozi    
        def bottega(self):
            negozi = pd.read_excel("Negozi.xlsx", index_col="Marchio")
            negozi.drop(columns=["Codice magazzino", "Tipo prodotto", "Fornitore", "Linea", "Sfera", "Cilindro", 
                        "Diametro", "Rb", "Tipo lenti", "Materiale", "Trattamento", "Descrizione", "Colore 2",
                        "Utente", "Ponte", "Calibro", "Asta", "Codice filiale", "Prezzo acquisto", "Valore magazzino",
                        "Data ult. acq", "Prezzo saldo", "Magazzino", "Filiale2", "Colore"
                        ], inplace = True)
            negozi.rename(columns = {"Codice a barre":"Barcode"}, inplace = True)
            return negozi
        
        # creo il modulo bottega e assemblo il file relativo ai prodotto nei negozi
        def online(self):
            shopify = pd.read_excel("Shopify.xlsx", index_col="Vendor")
            shopify.drop(columns=[
                "ID", "Handle", "Command", "Body HTML", "Type", "Tags", "Tags Command", "Created At", "Updated At",
                "Status", "Published", "Published At", "Template Suffix", "Variant ID", "Variant Inventory Qty", "Variant Inventory Adjust",
                "Variant Price", "Variant Compare At Price", "URL"], inplace = True)
            shopify.rename(columns = {"Variant Barcode" : "Barcode", "Inventory Available: +39 05649689443" : "Q.ty_Looker"}, inplace = True)
            return shopify
        
        def confronto(self):
            negozi = neg.bottega()
            shopify = neg.online()
            compare = shopify.merge(negozi, how = "inner", on = "Barcode", suffixes = ("_Looker", "_Negozi"))
            compare.set_index("Title", inplace = True)
            compare = compare[["Barcode", "Filiale", "Variant SKU", "Q.ty_Looker", "Quantità magazzino"]]
            # aggiungo colonna. Se i valori sono uguali ottengo TRUE altrimenti FALSE
            compare["Check"] = compare["Q.ty_Looker"] == compare["Quantità magazzino"]
            return compare
        
    # crezione della variabile "path" a cui assegno il percordo per aprire il file
    path_negozi = r"C:\Users\miche\Desktop\py\Progetti\off_white\Negozi.xlsx"
    path_shopify = r"C:\Users\miche\Desktop\py\Progetti\off_white\Shopify.xlsx"

    neg = Off_White(path_negozi, path_shopify)

    #neg.bottega()
    #neg.online()
    compare_at = neg.confronto()

    compare_at.to_excel("offWhite_compare.xlsx")
    print("File salvato nella directory!")
except Exception as e: 
    print(f"Si è verificato un errore {e}")
