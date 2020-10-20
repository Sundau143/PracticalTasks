
# list initialization with with values
# values are taken from training book (11-th) variant
listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]

# list is printed in console without any changes
print("List before InsertionSort: \n", listOfNumbers, sep='')

# variable "listLength" equals the length of a previously created list
listLength = len(listOfNumbers)
print('listLength =', listLength)

# variable "i" stores an element index of a list
for i in range(1, listLength):
    print('i = ', i)
    # initialization of an element, which has to be inserted
    # at start of every iteration it has an [i] index
    insertedElement = listOfNumbers[i]
    print('insertedElement = ', listOfNumbers[i])
    # the sorted part of an array starts with a [j] index
    # the size of an unsorted part decreases by 1
    j = i - 1
    print('j = i  - 1, j = ', i, ' - 1')
    print('j = ', j)
    # finding the smallest element in the unsorted part
    while j >= 0 and insertedElement < listOfNumbers[j]:
        print('j >= 0 and insertedElement < listOfNumbers[j], j >= 0 and', insertedElement, '<', listOfNumbers[j],
              '- вірно')
        # creating a "blank place" for inserted element
        listOfNumbers[j + 1] = listOfNumbers[j]
        print('j = ', j)
        print('listOfNumbers[j + 1] = listOfNumbers[j], listOfNumbers[j + 1] = ', listOfNumbers[j])
        # all indexes of an unsorted part of a list decrease by 1
        j -= 1
        print('j -= 1, j = ', j)
        # the element gets inserted at a "blank place"
        listOfNumbers[j + 1] = insertedElement
        print('listOfNumbers[j + 1] = insertedElement, listOfNumbers[j + 1] = ', insertedElement)
        print('=========================================')
    print('j >= 0 and insertedElement < listOfNumbers[j], j >= 0 and', insertedElement, '<', listOfNumbers[j],
          '- невірно')

# list is printed in console after it being sorted
print("List after InsertionSort: \n", listOfNumbers, sep='')
