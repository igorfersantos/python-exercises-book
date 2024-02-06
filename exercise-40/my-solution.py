def mergeTwoLists(list1: list, list2: list):
    merged_list = []

    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    removed_numbers_from_y = 0
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list1[x] > list2[y - removed_numbers_from_y]:
                merged_list.append(list2.pop(y - removed_numbers_from_y))
                removed_numbers_from_y += 1
        merged_list.append(list1[x])

    merged_list += list2

    return merged_list


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
