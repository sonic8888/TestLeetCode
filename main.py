import math
import random
from TestLinkedList import Node
from test_examples import My_Stack_Array, Stack_min
from LeetCode import *

LIST_NUMS = [2, 774, 647, 905, 906, 143, 400, 406, 672, 168, 680, 44, 304, 307, 692, 571, 830,
             63, 62, 322, 199, 584, 717, 208, 848, 214, 88, 473, 483, 611, 357, 745, 880, 114, 254, 891, 766, 895]

LIST_NODES = [5, 4, 8, 11, None, 13, 6, 7, 2, None, None, None, 1]

COUNT_ITER = 0
GRAPH = {'A': {'B': 2, 'C': 6},
         'B': {'D': 5},
         'C': {'D': 8},
         'D': {}}


# def merge_sort(a_list):
#     if len(a_list) > 1:
#         mid = len(a_list) // 2
#         left_half = a_list[:mid]
#         right_half = a_list[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         left_ind = 0
#         right_ind = 0
#         alist_index = 0
#         while left_ind < len(left_half) and right_ind < len(right_half):
#             if left_half[left_ind] < right_half[right_ind]:
#                 a_list[alist_index] = left_half[left_ind]
#                 left_ind += 1
#             else:
#                 a_list[alist_index] = right_half[right_ind]
#                 right_ind += 1
#             alist_index += 1
#         while left_ind < len(left_half):
#             a_list[alist_index] = left_half[left_ind]
#             left_ind += 1
#             alist_index += 1
#         while right_ind < len(right_half):
#             a_list[alist_index] = right_half[right_ind]
#             right_ind += 1
#             alist_index += 1


def move_zeros(a_list):
    zero_ind = 0
    for i, n in enumerate(a_list):
        if n != 0:
            a_list[zero_ind] = n
            if i != zero_ind:
                a_list[i] = 0
            zero_ind += 1
    print(a_list)


def sorted_array(a_list):
    index = 0
    temp_n = 0

    print(a_list)
    for i, n in enumerate(a_list):
        if not n & 1:
            print(n, end=' ')
            temp_n = a_list[index]
            a_list[index] = n
            a_list[i] = temp_n
            index += 1
    print()
    print(a_list)


def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index


def delete_duplicate(a_str):
    _dict = {}
    a_str = a_str[::-1]
    list_words = [w.lstrip(',.;:?!"') for w in a_str.split(' ')]
    # print(list_words)
    for word in list_words:
        if len(word) > 1:
            if word not in _dict:
                _dict[word] = 1
            else:
                _dict[word] = _dict[word] + 1
    # print(_dict)
    for key, value in _dict.items():
        if value > 1:
            a_str = a_str.replace(key + ' ', '', value - 1)

    a_str = a_str[::-1]
    print(a_str)


def merge_sort(_list):
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


def find_missing(A, n):
    result = 0

    # XOR of all the values from 1 to n
    for value in range(n + 1):
        result ^= value
    print(result)

    # XOR of all values in the given array
    for value in A:
        result ^= value

    return result


def move_zero_2(_list):
    zero_ind = 0
    for i, n in enumerate(_list):
        if n != 0:
            if i != zero_ind:
                _list[zero_ind] = n
                _list[i] = 0
            zero_ind += 1
    print(_list)


def display_linked_list(r):
    while r:
        print(r, end=', ')
        r = r.next
    print()


if __name__ == '__main__':
    res = 1
    # for i in range(10000):
    #     res = i * i
    #     print(f"{i:8} {res:>11}")
    # print(math.sqrt(2 ** 31))
    # 46340
    s = Solution()
    print(s.guessNumber(500))
