sorted_list = [31, 40, 22, 50, 53, 68, 97, 12, 15]
print(sorted_list)


def comb_sort(list_of_numbers):
    gap = len(list_of_numbers)
    print('gap = ', gap)
    is_swapped = True
    print('is_swapped = ', is_swapped)
    while gap > 1 or is_swapped:
        print('gap > 1 - вірно')
        gap = max(1, int(gap / 1.25))
        print('gap = ', gap)
        is_swapped = False
        for i in range(len(list_of_numbers) - gap):
            print('i = ', i)
            j = i + gap
            print('j = ', i, '+', 'gap')
            print('j = ', j)
            if list_of_numbers[i] > list_of_numbers[j]:
                print(list_of_numbers[i], '>', list_of_numbers[j], '- вірно')
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                print('Swap', list_of_numbers[i], list_of_numbers[j])
                is_swapped = True
                print('is_swapped -', is_swapped)
            else:
                print(list_of_numbers[i], '>', list_of_numbers[j], '- невірно')
                print('Елементи не міняються місцями')
                print('is_swapped = false')
            print(sorted_list)
            print('-------------------')
    print('=====================')
    print('gap > 1 - невірно')
    return list_of_numbers


comb_sort(sorted_list)
print(sorted_list)