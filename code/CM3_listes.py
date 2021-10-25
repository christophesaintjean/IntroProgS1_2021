## sélection des noms qui contiennent une voyelle en début ou en fin


noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

# version 1
select = []
for nom in noms:
    for voyelle in voyelles:
        if nom[0] == voyelle or nom[-1] == voyelle:
            select.append(nom)
            break
        
print(select)
# for s in select:
#    print(s)

# version 2
select = []
for nom in noms:
    if nom[0] in voyelles or nom[-1] in voyelles:
        select.append(nom)
        
print(select)


