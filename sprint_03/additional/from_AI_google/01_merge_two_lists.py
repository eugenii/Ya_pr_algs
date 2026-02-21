# 01_merge_two_lists.py

def merge_two_lists(list1, list2):
    merged_list = []
    if not list1:
        return merged_list + list2
    if not list2:
        return merged_list + list1
    if list1[0] < list2[0]:
        merged_list.append(list1[0])
        return merged_list + merge_two_lists(list1[1:], list2)
    else:
        merged_list.append(list2[0])
        return merged_list + merge_two_lists(list1, list2[1:])


print(merge_two_lists([1, 3, 5], [2, 4, 6]))