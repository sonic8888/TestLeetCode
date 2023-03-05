def merge_sort(_list):  # O(n * Log n)
    if len(_list) > 1:
        mid = len(_list) // 2
        left_half = _list[:mid]
        right_half = _list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        left_ind = 0
        right_ind = 0
        index_list = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                _list[index_list] = left_half[left_ind]
                left_ind += 1
            else:
                _list[index_list] = right_half[right_ind]
                right_ind += 1
            index_list += 1
        while left_ind < len(left_half):
            _list[index_list] = left_half[left_ind]
            left_ind += 1
            index_list += 1
        while right_ind < len(right_half):
            _list[index_list] = right_half[right_ind]
            right_ind += 1
            index_list += 1


def bubble_sort(a_list): # O(n**)
    count = len(a_list) - 1
    for i in range(count):
        no_swap = True
        for j in range(count - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swap = False
        if no_swap:
            return a_list
    return a_list


def insert_sort(a_list): # O(n**)
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and value < a_list[i - 1]:
            a_list[i] = a_list[i - 1]
            i = i - 1
            a_list[i] = value
    return a_list
