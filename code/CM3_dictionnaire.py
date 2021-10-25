alphabet ='abcdefghijklmnopqrstuvwxyz'
texte = 'le chat est mort, les souris dansent'

# Compter les occurrences de chaque lettre dans le texte
dico_cpt = {}
for lettre in texte:
    if not lettre in alphabet:
        pass       
    elif lettre in dico_cpt:
        dico_cpt[lettre] = dico_cpt[lettre] + 1
    else:
        dico_cpt[lettre] = 1
    
print(dico_cpt)

print("Dans l'ordre alphabétique")
print("{")
for lettre in alphabet:
    if lettre in dico_cpt:
        print(f"'{lettre}': {dico_cpt[lettre]}", end=", ")
print("}")
    



