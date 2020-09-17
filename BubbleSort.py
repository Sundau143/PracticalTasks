listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]

print("List before BubbleSort: ")
print(listOfNumbers)

listLength = len(listOfNumbers)
for i in range(0, listLength):
    for j in range(0, listLength - 1):
        if listOfNumbers[j] > listOfNumbers[j + 1]:
            tempElement = listOfNumbers[j]
            listOfNumbers[j] = listOfNumbers[j + 1]
            listOfNumbers[j + 1] = tempElement

print("List after BubbleSSort:")
print(listOfNumbers)
