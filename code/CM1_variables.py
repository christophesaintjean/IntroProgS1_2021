i = 5
f = 2.17
b = True
s = "chaine"
f1 = i / 2
i1 = i // 2
i0 = i // 6
i2 = i / int(f)
f2 = i / 2.0
f3 = float(i) / 2
s1 = str(f)
s2 = str(b)
print(i)
print(i+f)
# observez les différences au niveau des espaces dans les deux lignes suivantes
print(s+" est une chaine (!) et " + s1 + " aussi")
print(s,"est une chaine (!) et" ,s1,"aussi")
# corrigez la ligne suivante
print(s+i+"(int) -- "+f+"(float)-- "+b+" (boolean)")
print(s+str(i)+"(int) -- "+str(f)+"(float)-- "+str(b)+" (boolean)")
print(s,i,"(int) -- ",f,"(float)-- ",b," (boolean)")
