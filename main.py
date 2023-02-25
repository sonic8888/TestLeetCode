import random
import sys
from base64 import decode
from random import randint
from typing import List, Optional
from collections import deque
import string
from heapq import heappush, heappop, heapify
from LeetCode import *
from TestLinkedList import Node, LinkedList
from test_examples import *
from Heap import find_min_cost

LIST_NUMS = [2, 774, 647, 905, 906, 143, 400, 406, 672, 168, 680, 44, 304, 307, 692, 571, 830,
             63, 62, 322, 199, 584, 717, 208, 848, 214, 88, 473, 483, 611, 357, 745, 880, 114, 254, 891, 766, 895]

LIST_NODES = [5, 4, 8, 11, None, 13, 6, 7, 2, None, None, None, 1]

COUNT_ITER = 0
GRAPH = {'A': {'B': 2, 'C': 6},
         'B': {'D': 5},
         'C': {'D': 8},
         'D': {}}


def bubble_sort(sec):
    global COUNT_ITER
    count = len(sec) - 1
    is_swap = True
    for i in range(count):
        for j in range(count - i):
            if sec[j] > sec[j + 1]:
                sec[j + 1], sec[j] = sec[j], sec[j + 1],
                is_swap = False
                COUNT_ITER += 1
        if is_swap:
            return sec
    return sec


def insert_sort(sec):
    global COUNT_ITER
    for i in range(1, len(sec)):
        value = sec[i]
        while i > 0 and sec[i - 1] > value:
            sec[i] = sec[i - 1]
            i = i - 1
            COUNT_ITER += 1
        sec[i] = value


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        left_ind = 0
        right_ind = 0
        alist_index = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] < right_half[right_ind]:
                a_list[alist_index] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_index] = right_half[right_ind]
                right_ind += 1
            alist_index += 1
        while left_ind < len(left_half):
            a_list[alist_index] = left_half[left_ind]
            left_ind += 1
            alist_index += 1
        while right_ind < len(right_half):
            a_list[alist_index] = right_half[right_ind]
            right_ind += 1
            alist_index += 1


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


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        linked_list.append(i)
    head = linked_list.head
    print(head)
    s = Solution()
    s.reverseList(head)
