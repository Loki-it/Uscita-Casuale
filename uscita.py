import random

# apre la lista degli amici
with open('amici.txt', 'r') as f:
    amici = f.read().splitlines()

# apre la lista dei locali
with open('locali.txt', 'r') as f:
    locali = f.read().splitlines()

try:
    # qui scegli il numero di amici
    numero_amici = int(input('Con quanti amici vuoi uscire? '))

    # sceglie casualmente il numero di amici specificato da te
    amici_scelti = random.sample(amici, numero_amici)

    # sceglie un locale casuale
    locale_scelto = random.choice(locali)
    if numero_amici == 0: # se vuoi uscire da solo
        print(f'Questa sera uscirai da solo al locale: {locale_scelto}')        
    else: # in caso contrario
        print(f'Questa sera uscirai con: {", ".join(amici_scelti)} al locale: {locale_scelto}')

except ValueError: print("Devi inserire un numero valido di amici!")
except: print("Hey, qualcosa non va!")
