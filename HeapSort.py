# list initialization with with values
# values are taken from training book (11-th) variant
listOfNumbers = [31, 40, 22, 50, 53, 68, 97, 12, 15]
print("List before HeapSort: \n", listOfNumbers, sep='')


# function, which transforms the list into the the heap
def heap_transform(sorting_list, k, i):
    # function searches for the biggest element among child elements and a root
    child_element = 2 * i + 1
    print('child_element = 2 *', i, '+ 1')
    print('child_element = ', child_element)
    root_element = 2 * i + 2
    print('root_element = 2 *', i, '+ 2')
    print('root_element = ', root_element)
    largest_element = i
    print('largest_element = i = ', i)

    # in case, if the found element is bigger than the root
    if child_element < k and sorting_list[i] < sorting_list[child_element]:
        print('child_element < k and sorting_list[i] < sorting_list[child_element]', child_element, '<', k, 'and', sorting_list[i], '<', sorting_list[child_element], '- вірно')
        print('largest_element = i = ', i)
        # the root gets replaced by found element
        largest_element = child_element
        print('largest_element = child_element, largest_element = ', child_element)

    # in case, if the found element is bigger than the largest element
    if root_element < k and sorting_list[largest_element] < sorting_list[root_element]:
        print('root_element < k and sorting_list[largest_element] < sorting_list[root_element]', root_element, '<',
              k, 'and', sorting_list[largest_element], '<', sorting_list[root_element], '- вірно')
        # the largest element gets replaced by found element
        largest_element = root_element
        print('largest_element = root_element', 'largest_element =', root_element)

    # function checks, if the root of the heap is the biggest element
    # if not, the process of heap transform continues
    if largest_element != i:
        print('largest_element != i, largest_element !=', i, '- вірно')
        sorting_list[i], sorting_list[largest_element] = sorting_list[largest_element], sorting_list[i]
        print('largest_element = ', largest_element)
        print('i = ', i)
        print('swap(sorting_list[i], sorting_list[largest_element] = sorting_list[largest_element], sorting_list[i])')
        heap_transform(sorting_list, k, largest_element)


# function, which is used to heap sort the list
def heap_sort(sorting_list):
    length = len(sorting_list)
    print('length =', length)
    # Build max heap
    for i in range(length // 2, -1, -1):
        print('i =', i)
        heap_transform(sorting_list, length, i)
        print('heap_transform(sorting_list', + length, i)
        print('----------------')

    for i in range(length - 1, 0, -1):
        print('i =', i)
        # Swap
        sorting_list[i], sorting_list[0] = sorting_list[0], sorting_list[i]
        print('swap(sorting_list[i], sorting_list[0] = sorting_list[0], sorting_list[i])')
        # Heapify root element
        heap_transform(sorting_list, i, 0)
        print('heap_transform(sorting_list', + i, 0)
        print('========================')


# the created function is called to sort the list
heap_sort(listOfNumbers)
# list is printed in console after it being sorted
print("List after HeapSort: \n", listOfNumbers, sep='')