MAX_OUT = 10**8
MIN_Q = 4_000
MAX_Q = 8_000

abonnes = int(input("Abonnes ? "))

if abonnes * MAX_Q <= MAX_OUT:
    # Scenario 1
    print('Scenario 1')
    new = (MAX_OUT - abonnes * MAX_Q) // MAX_Q
    print(f'Je peux fournir {new} abo. en Scen. 1')

elif abonnes * MIN_Q <= MAX_OUT:
    # Scenario 2
    print('Scenario 2')
    debit_moyen = MAX_OUT / abonnes
    print(f'Debit moyen : {debit_moyen:.2f}')

else:
    # Scenario 3
    print('Scenario 3')
    trop = (abonnes * MIN_Q - MAX_OUT) // MIN_Q 
    print(f'A couper : {trop}')