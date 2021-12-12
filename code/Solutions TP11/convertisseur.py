import math

def deCversF(tc):
    return tc * 9 /5 + 32

def deFversC(tf):
    return (tf - 32) * 5 / 9

print(f"convertisseur : {__name__}")

if __name__ == "__main__":
    tc = float(input("Temperature en Celsius ? "))
    tf = deCversF(tc)
    print(f"Temperature en Farenheit : {tf}")
    if not math.isclose(tc, deFversC(tf)):
        print("Erreur de conversion")
