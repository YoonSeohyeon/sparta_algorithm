finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    start = 0
    end = len(array) -1
    middle = (start + end)//2
    find_count = 0

    while start <= end:
        find_count +=1
        if array[middle] == target:
            print(find_count)
            return True
        elif array[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

        middle = (start+end)//2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)