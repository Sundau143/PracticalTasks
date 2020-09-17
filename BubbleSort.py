
# list initialization with with values
# values are taken from training book (11-th) variant
listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]

# list is printed in console without any changes
print("List before BubbleSort: ")
print(listOfNumbers)

# variable "listLength" equals the length of a previously created list
listLength = len(listOfNumbers)

# variable "i" stores an element index of a list
# there are two cycles, which are checking the list at the same time
for i in range(0, listLength):
    for j in range(0, listLength - 1):
        # if a previous element is bigger than the next
        if listOfNumbers[j] > listOfNumbers[j + 1]:
            # a temp variable is equaled to the previous element
            tempElement = listOfNumbers[j]
            # a previous element is replaced by next one
            listOfNumbers[j] = listOfNumbers[j + 1]
            # the next element is equaled to temp variable
            listOfNumbers[j + 1] = tempElement
            # so, the previous and next elements get replaced

# list is printed in console after it being sorted
print("List after BubbleSSort:")
print(listOfNumbers)
