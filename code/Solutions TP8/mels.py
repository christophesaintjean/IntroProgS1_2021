with open('emails.txt', encoding="utf-8") as f:
    M = f.read().splitlines()
    
print(M)

print(f"Le nombre d'adresses est {len(M)}")

lmax = -1
for m in M:
    if len(m) > lmax:
        lmax = len(m)

print(f"La plus longue adresse fait {lmax} caractères")
    
D = []
for m in M:
    domaine = m.split("@")[1]
    D.append(domaine)
print(D)

Du = []
for d in D:
    if d not in Du:
        Du.append(d)
print(Du)


# Avec liste
dtuple = []
dom = None
for d in D:
    if d != dom:
        if dom is not None:
            print(f"{cpt} adresses de {dom}")
        cpt = 1
        dom = d
    else:
        cpt = cpt + 1
else:
    print(f"{cpt} adresses de {dom}")

print("*"*50)

# Avec dictionnnaire
dict_cpt = {}
for d in D:
    if d in dict_cpt:
        dict_cpt[d] = dict_cpt[d] + 1
    else:
        dict_cpt[d] = 1

L_cpt = []
for k, v in dict_cpt.items():
    print(f"{v} adresses de {k}")

print("*"*50)

# Modification de la solutions Avec liste
dtuple = []
dom = None
for d in D:
    if d != dom:
        if dom is not None:
            dtuple.append((dom, cpt))
        cpt = 1
        dom = d
    else:
        cpt = cpt + 1
else:
    dtuple.append((dom, cpt))

print(dtuple)
