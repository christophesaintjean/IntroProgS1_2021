Sam = {'age':43, 'affiliation':'Toronto', 'active': False}

for cle, valeur in Sam.items():
    print(f"'{cle}'={valeur}", end=" -- ")

print()

for cle in Sam.keys():
    print(f"'{cle}'={Sam[cle]}", end=" -- ")
    
print()

for cle in Sam:
    print(f"'{cle}'={Sam[cle]}", end=" -- ")
    
print()

for valeur in Sam.values():
    print(f"{valeur}", end=" -- ")