print("Beantworten Sie die Fragen mit ja oder nein.")

zerlegung_frage = "Ist das Projekt in Teilaufgaben und Arbeitspakete zerlegt? "
festlegung_frage = "Ist die Gliederungsstruktur festgelegt? "
zuordnung_frage = "Sind die Teilaufgaben und Arbeitspakete im Projektstrukturplan zugeordnet? "
codierung_frage = "Sind die Teilaufgaben und Arbeitspakete codiert? "
ueberpruefung_frage = "Wurde die Vollständigkeit überprüft? "

fragen_liste = {zerlegung_frage:input(zerlegung_frage).lower(), festlegung_frage:input(festlegung_frage).lower(), zuordnung_frage:input(zuordnung_frage).lower(), codierung_frage:input(codierung_frage).lower(), ueberpruefung_frage:input(ueberpruefung_frage).lower()}

if any("nein" in value for value in fragen_liste.items()):
    print("Für folgende Fragen stehen anscheinend noch Arbeitsschritte in der Planung aus:")
    for key, value in fragen_liste.items():
        if "nein" == value:
            print(key)

elif all("ja" in value for value in fragen_liste.items()):
    print("Sie haben gute Arbeit geleistet und können mit der zeitlichen Planung fortfahren.")
        

     
              

