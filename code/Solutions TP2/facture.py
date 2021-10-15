desi = input("Désignation ? ")
pu = float(input("Prix unitaire ? "))
quant = int(input("Quantité ? "))

print("Facture :", quant, desi, "à", pu,"€ l'unité font", quant*pu, "€")
print(f"Facture : {quant} {desi} à {pu:.2f} € l'unité font {quant*pu:.2f} €")
