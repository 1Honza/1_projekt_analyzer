TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

# REGISTROVANI UYIVATELE

#print('Registrováni jsou tito uživatelé:')

#| USER |   PASSWORD  |
#-----------------------
#| bob  |     123     |
#| ann  |   pass123   |
#| mike | password123 |
#| liz  |   pass123   |


# PRIHLASENI UYIVATELE

odelovac = '=' * 50

print(odelovac)
print('Pro vstup je nutno zadat prihlasovaci udaje.')
print(odelovac)
jmeno = input('zadej sve jmeno: ')
heslo = input('zadej sve heslo: ')
print(odelovac)
jmena_hesla = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

if jmena_hesla.get(jmeno) != heslo:
    print('prihlaseni se nezdarilo')
    exit()

print('prihlaseni je v poradku')
print(odelovac)

# VYBER TEXTU

text = int(input('zvol si cislo textu: 1, 2, 3: '))
print(odelovac)

if text == 1:
    print(TEXTS[0])
    print(odelovac)
    text_1 = TEXTS[0]
elif text == 2:
    print(TEXTS[1])
    print(odelovac)
    text_1 = TEXTS[1]
elif text == 3:
    print(TEXTS[2])
    print(odelovac)
    text_1 = TEXTS[2]
elif text > 3:
    print('SPATNY VYBER TEXTU')
    exit()

# ROZDELENI TEXTU A SPOCITANI SLOV

text_3 = text_1.split()
pocet_slov = len(text_3)
print('V textu je: ',pocet_slov,'slov')

# OCISTENI ROZDELENYCH SLOV OD ZNAKU

text_2 = []
while text_3:
    slovo = text_3.pop()
    slovo = slovo.strip('.,:/;')
    if slovo:
        text_2.append(slovo)

velke_pismeno = 0
mala = 0
velka = 0
cisla = 0
soucet = 0
graf = {}

i = 0

# SPOCITANI KOLIKRAT JE VYSKYT SLOV: PRVNI VELKE PISMENO, VELKE PISMO, MALE PISMO, CISEL, SOUCET CISEL

while i < len(text_2):
    if text_2[i].istitle():
        velke_pismeno = velke_pismeno + 1
    elif text_2[i].isupper():
        velka = velka + 1
    elif text_2[i].islower():
        mala = mala + 1
    elif text_2[i].isnumeric():
        cisla = cisla + 1
        soucet = soucet + float(text_2[i])

    d = len(text_2[i])
    graf[d] = graf.get(d,0) + 1

    i = i + 1

print('Pocet slov: ', velke_pismeno,' zacinajicim velkym pismenem')
print('Pocet slov: ', velka,' velkym pismem')
print('Pocet slov: ', mala, ' malym pismem')
print('Pocet cisel: ',cisla)
print(odelovac)

# ZOBRAZENI GRAFU

delka = sorted(graf)

i = 0
while i < len(delka):
    delka_1 = delka[i]
    kolik = graf[delka_1]

    if len(str(delka_1)) == 1:
        delky = ' ' + str(delka_1)
    else:
        delky = delka_1
    print(delky, '*' * kolik, kolik)
    i = i + 1

# CELKOVY SOUCET

print(odelovac)
print('celkovy soucet cisel v textu je: ',soucet)
print(odelovac)





