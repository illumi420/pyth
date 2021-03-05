jahrumsatz = int(input("jahrumsatz "))
jahrdauer = int(input("jahrdauer "))

etc_provision = jahrumsatz * 0.01
if jahrumsatz <= 10000:
    provision = (jahrumsatz * 0.05)

elif jahrumsatz > 10000 and jahrumsatz <= 20000:
    provision = (jahrumsatz * 0.15)

elif jahrumsatz > 20000:
    provision = (jahrumsatz * 0.20)

if jahrdauer >= 5:
    provision = (provision + etc_provision)
print(provision)
