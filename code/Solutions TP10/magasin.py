def verification(d1, d2):
    for k1 in d1.keys():
        if k1 not in d2.keys():
            return False
    for k2 in d2.keys():
        if k2 not in d1.keys():
            return False
    return True

def achat_possible(k ,v, d):
    if k in d:
        return d[k] >= v
    return None

def achats_possibles(d_achats, d):
    for k, v in d_achats.items():
        r = achat_possible(k ,v, d)
        if not r:
            return r
    return True

def achats(d_achats, d_pu, d_stocks, facture=True):
    total = 0
    for k, v in d_achats.items():
        r = achat_possible(k ,v, d_stocks)
        if r:
            d_stocks[k] = d_stocks[k] - v
            if facture:
                total = total + v * d_pu[k]
                print(f"{k}: {v} x {d_pu[k]} = {v * d_pu[k]}")
    if facture:
        print("-"*20)
        print(f"Prix total: {total}")        


if __name__ == "__main__":
    d_pu = {
        "Épée en mousse": 5,
        "Masque Dark Vador": 30,
        "Hand spinner 3d": 10,
        "Console Minux": 150,
        "Lego Footix": 15
    }
    d_stock = {
        "Épée en mousse": 10,
        "Masque Dark Vador": 4,
        "Hand spinner 3d": 10,
        "Console Minux": 2,
        "Lego Footix": 5
    }
    print(verification(d_pu, d_stock))
    print(achat_possible("Hand spinner 3d", 2, d_stock))
    print(achat_possible("Console Minux", 5, d_stock))
    print(achats_possibles({"Hand spinner 3d": 2}, d_stock))
    d_achats = {"Hand spinner 3d": 2, "Console Minux": 5}
    print(achats_possibles(d_achats, d_stock))
    achats({"Hand spinner 3d": 2, "Lego Footix": 1}, d_pu, d_stock, True)
    print(d_stock)