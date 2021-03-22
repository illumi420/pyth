stations = [
    "Südkreuz", "Schöneberg", "Innsbrucker Platz", "Bundesplatz",
    "Heidelberger Platz", "Halensee", "Westkreuz", "Messe Nord/ICC", "Westend",
    "Jungfernheide", "Beusselstraße", "Westhafen", "Wedding", "Gesundbrunnen",
    "Schönhauser Alle", "Prenzlauer Alle", "Greifswalder Straße",
    "Landsberger Alle", "Storkower Straße", "Frankfurter Alle", "Ostkreuz",
    "Treptower Park", "Sonnenallee", "Neukölln", "Hermannsstraße", "Tempelhof",
    "Südkreuz"
]

minuets_till_next_station = [
    2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 3, 3, 2, 3, 2, 3, 2, 2, 2, 6, 2, 3, 2, 1, 4,
    2
]
minuets_long = sum(minuets_till_next_station)  #59
km_long = 37, 0

station_duration = {}

for i in stations:
    for j in minuets_till_next_station:
        station_duration[i] = j

print(station_duration)
# print(sum(minuets_till_next_station))

# r_41 = print("r41:", stations)
# print()
# stations.reverse()
# r_42 = print("r42:", stations)
