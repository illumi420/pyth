import random as r
lotto_zahlen = []

# To make sure that no random number is duplicated in the list


def pruefeZahl(liste, zahl):
    if zahl not in liste:
        return False


def lottoZahlen(liste):
    counter = 0
    while counter < 6:
        random_zahl = r.randint(1, 49)
        if pruefeZahl(liste, random_zahl) is False:
            liste.append(random_zahl)
            counter = counter + 1
        else:
            random_zahl = r.randint(1, 49)
    return liste

# To sort the list


def sortiereListe(liste):
    for i in range(len(liste)):  # defines the indexes
        for j in range(len(liste)-1):  # j will be the value saved in the indexes
            if liste[j] > liste[j+1]:  # if first bigger than second
                # exchanges the position
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste


lottoZahlen(lotto_zahlen)
sortiereListe(lotto_zahlen)
for random_zahl in lotto_zahlen:
    index = lotto_zahlen.index(random_zahl)
    print(f'Zahl {index +1}: {random_zahl}')
