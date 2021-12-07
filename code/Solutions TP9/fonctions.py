def aire_carre(cote):
    aire = cote * cote
    return aire

a = aire_carre(14)
print(a)

def aire_rectangle(h, l):
    return l * h

def aire_carre2(cote):
    return aire_rectangle(cote, cote)

def aire_rectangle2(h, l=None):
    if l is None:
        l = h # ou return aire_carre(h)
    if h == l:
        return aire_carre(h)
    else:
        return aire_rectangle(h, l)

def aire_rectangle2bis(h, l=None):
    if l is None or h == l:
        return aire_carre(h)
    else:
        return aire_rectangle(h, l)
                                          
print(aire_rectangle2bis(4, 5))
print(aire_rectangle2bis(4, 4))
print(aire_rectangle2bis(4))