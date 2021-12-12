from convertisseur import deCversF

print(f"principal : {__name__}")
if __name__ == "__main__":
    with open('celsius.txt', mode='r') as f:
        liste_tc_str = f.readlines()
        
    with open('farenheit.txt', mode='w') as f:
        for tc_str in liste_tc_str:
            print(deCversF(float(tc_str)), file=f)
    
