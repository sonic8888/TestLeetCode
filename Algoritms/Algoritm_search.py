def binary_search(a_list, n):
    mid = -1
    while mid != 0:
        mid = len(a_list) // 2
        if a_list[mid] == n:
            return True
        elif a_list[mid] < n:
            a_list = a_list[mid + 1:]
        else:
            a_list = a_list[:mid]
    return False
