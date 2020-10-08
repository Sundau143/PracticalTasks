
# list initialization with with values
# values are taken from training book (11-th) variant
list_to_sort = [31, 40, 22, 50, 53, 68, 97, 12, 15]
length = len(list_to_sort)

# list is printed in console without any changes
print("List before QuickSort:\n", list_to_sort, sep='')


# this function is used to compare elements with the pivot
def partition(sorted_list, lowest, highest):
    # i equals to the index of the lowest element
    i = (lowest - 1)
    # the pivot is set as the highest element of the list
    pivot = sorted_list[highest]
    for j in range(lowest, highest):
        # comparing the current element with the pivot
        if sorted_list[j] <= pivot:
            # if the current element is smaller or equals to pivot
            # the index of smallest element increases by 1
            i += 1
            # two elements are getting replaced
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    # after the end of the loop, the lowest and highest elements are replaced by indexes
    sorted_list[i + 1], sorted_list[highest] = sorted_list[highest], sorted_list[i + 1]
    # the function returns the i + 1 index of the lowest element
    return i + 1


# the function which is used directly for quick sort
def quick_sort(sorted_list, lowest, highest):
    # in case, if list consists of 1 element, the list is not changed
    if len(sorted_list) <= 1:
        return sorted_list
    # if the lowest element is bigger than the highest
    if lowest < highest:
        # pivot index is set to the index of i + 1 og the smallest list element
        pivot = partition(sorted_list, lowest, highest)
        # quick sort relatively the smallest element
        quick_sort(sorted_list, lowest, pivot - 1)
        quick_sort(sorted_list, pivot + 1, highest)
        # quick sort relatively the biggest element
        quick_sort(sorted_list, pivot + 1, highest)


# the function is called to sort the list
quick_sort(list_to_sort, 0, length - 1)
# list is printed in console after being sorted
print("List after QuickSort:\n", list_to_sort, sep='')

