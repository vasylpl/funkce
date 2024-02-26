def scitani(a, b): 
    vysledek = a+b
    return vysledek


promena1 = input("zadejte proměnou 1: ")
promena2 = input("zadejte proměnou 2: ")

promena1 = int(promena1)
promena2 = int(promena2)

vysledek = scitani(promena1, promena2)

print("vysledek je: ",str(vysledek))