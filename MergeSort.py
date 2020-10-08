
# list initialization with with values
# values are taken from training book (11-th) variant
list_to_sort = [31, 40, 22, 50, 53, 68, 97, 12, 15]
left = 0
right = len(list_to_sort)

# list is printed in console without any changes
print("List before MergeSort:\n", list_to_sort, sep='')


# defining the function, which merges two sub-lists by a criteria:
def merge_sort(sorting_list, left, right):
    # in case, if the list consists of one element, the loop stops
    if (left + 1) >= right:
        return
    # in other case:
    else:
        # index of middle element is found by dividing the sum of side indexes by 2
        mid = (left + right) // 2
        # the first half of list is being sorted (starts with left, ends by mid)
        merge_sort(sorting_list, left, mid)
        # second half of list is being sorted (starts with mid, ends by right)
        merge_sort(sorting_list, mid, right)
        # the two parts of list are being merged into one
        merge(sorting_list, left, mid, right)
        # the function returns the sorted-out list
        return sorting_list


# this function merges 2 parts of the list by certain criterias:
def merge(sorting_list, left, mid, right):
    it1 = 0
    it2 = 0
    # the sorted part of list will be stored in this list
    result = []

    # if the sorted part of list is tightened into 1 element, the loop stops
    while left + it1 < mid and mid + it2 < right:
        # at this part, the elements from different sides are being compared with ach other
        if sorting_list[left + it1] < sorting_list[mid + it2]:
            # the element bigger then the element from left side is inserted into result list
            result.insert(it1 + it2, sorting_list[left + it1])
            it1 += 1
        # in other case, the element is inserted into list, too:
        else:
            result.insert(it1 + it2, sorting_list[mid + it2])
            it2 += 1
    # in this loop, the found bigger elements are inserted into first half of result list
    while left + it1 < mid:
        result.insert(it1 + it2, sorting_list[left + it1])
        it1 += 1
    # in this loop, the found bigger elements are inserted into second half of result list
    while mid + it2 < right:
        result.insert(it1 + it2, sorting_list[mid + it2])
        it2 += 1

    # the sorted list is being replaced by elements from a temporary list
    for i in range(0, (it1 + it2)):
        sorting_list[left + i] = result[i]
        print(sorting_list)


# the function is called to sort the list
merge_sort(list_to_sort, left, right)
# list is printed in console after being sorted
print("List after MergeSort:\n", list_to_sort, sep='')




