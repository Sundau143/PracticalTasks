listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]

print("List before InsertionSort: ")
print(listOfNumbers)

listLength = len(listOfNumbers)

for i in range(1, listLength):
    insertedElement = listOfNumbers[i]
    j = i - 1
    while j >= 0 and insertedElement < listOfNumbers[j]:
        listOfNumbers[j + 1] = listOfNumbers[j]
        j -= 1
        listOfNumbers[j + 1] = insertedElement

print("List after InsertionSort: ")
print(listOfNumbers)
