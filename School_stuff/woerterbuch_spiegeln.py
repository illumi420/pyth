def spiegeln(dictionary):
    updated_dictionary = {}
    for i in dictionary:
        updated_dictionary[dictionary[i]] = i
    return updated_dictionary


vokabeln = {"I": "Ich", "Cake": "Kuchen", "You": "Du", "Sun": "Sonne",
            "Like": "mögen", "Apple": "Apfel", "Hate": "hassen", "Tree": "Baum"}

new_dict = spiegeln(vokabeln)
print(new_dict)
