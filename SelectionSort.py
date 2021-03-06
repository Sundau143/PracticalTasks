# list initialization with with values
# values are taken from training book (11-th) variant
listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]

# list is printed in console without any changes
print("List before SelectionSort: \n", listOfNumbers, sep='')

# variable "listLength" equals the length of a previously created list
listLength = len(listOfNumbers)
print('listLength = ', listLength)

# variable "i" stores an element index of a list
# variable "smallestElement" equals an index of a smallest element
for i in range(listLength):
    print('i = ', i)
    # at the start of a loop it's initialized as a first element of an unsorted sequence
    # the sorted sequence decreases with every loop iteration
    smallestElement = i
    print('smallestElement =', i)
    # second loop searches for the smallest element in the unsorted sequence
    # with every iteration, start point of second loop increases by 1
    for j in range(i + 1, listLength):
        print('i = ', i)
        # if the found element is bigger than the element with [smallestElement] index
        # the element with this index gets replaced by a found one
        if listOfNumbers[j] < listOfNumbers[smallestElement]:
            print('listOfNumbers[j] < listOfNumbers[smallestElement]', listOfNumbers[j], '<',
                  listOfNumbers[smallestElement], '- вірно')
            smallestElement = j
            print('smallestElement =', j)
        else:
            print('listOfNumbers[j] < listOfNumbers[smallestElement]', listOfNumbers[j], '<',
                  listOfNumbers[smallestElement], '- невірно')

    listOfNumbers[i], listOfNumbers[smallestElement] = listOfNumbers[smallestElement], listOfNumbers[i]
    print('swap(listOfNumbers[i], listOfNumbers[smallestElement])')
    print(listOfNumbers)
    print('=========================')

# list is printed in console after it being sorted
print("List after SelectionSort: \n", listOfNumbers, sep='cock')
