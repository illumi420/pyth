from statistics import mean
"""
print('======================================= Exercise 1 =======================================')
story = 'On a fresh sunny day, I went to the beach, to enjoy fresh air'
words = story.split(' ')
print(words)
print(words[5:10])
print('The word', '"' + words[6] + '"', 'is in position', words.index("went"))
"""
"""
print(
    '======================================= Exercise 2 ======================================='
)
temperatureGuessValue = print('Guessing tomorrow temperature')
thresholdMin = 5
thresholdMax = 35
temperatureGuessList = [2, -9, 18, 12, 35, 36, 19, 50, 41, 12, 16]
validValues = []
for elements in temperatureGuessList:
    # complete here, checking if the value is within the valid threshold.
    # if yes, print "`value` is valid" and add it into `validValues` list
    # if not, when value is not in the valid range, we only print "`value` is outside of the valid range."
    if (elements <= 35) and (elements >= 5):
        validValues.append(elements)
# Here we expect to see: [18, 12, 35, 19, 12, 16]
print('Valid values are:', validValues)
countDiscardedValues = len(temperatureGuessList) - len(validValues)
# Here we expect to see: 'Count discarded values: 5'
print('Count discarded values:', countDiscardedValues)
# We can finally calculate the average using only the valid values.
averageTemperatureExpected = mean(validValues)
# Expected output: 'Average temperature guess for tomorrow is:  18.75'
print('Average temperature expected: ', round(averageTemperatureExpected, 2))
"""

print(
    '======================================= Exercise 3 ======================================='
)

minLimit = 5
maxLimit = 35
maxTimesInput = 20
onlyValidTemperatures = []


def input_temperature():
    while len(onlyValidTemperatures) <= maxTimesInput:
        try:
            temperature = input(">> Insert a temperature: ").lower()
            #print("Temperature: " + temperature)
            if temperature == 'end':
                listResults(onlyValidTemperatures)
                break

            if valid_temperature(temperature, minLimit, maxLimit):
                onlyValidTemperatures.append(int(temperature))

                if len(onlyValidTemperatures) == maxTimesInput:
                    listResults(onlyValidTemperatures)
                    break
            else:
                print("<<", temperature,
                      "is not a valid temperature. Ignoring it.")
        except:
            print(
                "Invalid input - You can insert a temperature (integer) or the word 'end', to get the results."
            )
    return onlyValidTemperatures


def listResults(a_list):
    print()
    print("<< Data received, thanks! Results:")
    print("<< Count valid values:", len(a_list))
    print("<< Average temperature from valid values:", round(mean(a_list), 2))
    print("<< Min value:", min(a_list))
    print("<< Max value:", max(a_list))


def valid_temperature(temperature, min_limit, max_limit):
    if int(temperature) <= max_limit and int(temperature) >= min_limit:
        return True
    else:
        return False


input_temperature()

print("<< Entered Valid Values: ", *onlyValidTemperatures)
