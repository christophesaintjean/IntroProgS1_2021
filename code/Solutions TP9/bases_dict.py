D = {"Nom": "Mbappe",
     "Prénom": "Killian"}
D["Age"] = 22

if len(D["Nom"] + D["Prénom"]) > D["Age"]:
    print("OK")
else:
    print("KO")
    
D2 = {"Club": "PSG", "Salaire": 1_500_000, "Age": 21}

D.update(D2)
print(D)

del D["Age"]
D["AgeLycée"] = 15
print(D)