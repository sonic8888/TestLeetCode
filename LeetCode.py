from itertools import zip_longest
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # self.flag = True

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'{self.val}'


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     list_node = []
    #     steck = deque()
    #     current_node = root
    #     while current_node or len(steck) > 0:
    #         if current_node:
    #             steck.append(current_node)
    #             current_node = current_node.left
    #         else:
    #             current_node = steck.pop()
    #             list_node.append(current_node.val)
    #             current_node = current_node.right
    #     return list_node
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_node = []

        def inorder_recursion(root):
            if root:
                inorder_recursion(root.left)
                list_node.append(root.val)
                inorder_recursion(root.right)

        inorder_recursion(root)
        return list_node

    def traversal_deep(self, root):
        list_values = []
        _deep = 0
        _deep_recur = 0
        is_end = True

        def get_values(r, deep, _deep_recur):
            deep += 1
            nonlocal is_end
            if r:
                if deep == _deep_recur:
                    list_values.append(r.val)
                get_values(r.left, deep, _deep_recur)
                get_values(r.right, deep, _deep_recur)
            else:
                if deep == _deep_recur:
                    list_values.append(None)
                return
            if not is_end and deep == _deep_recur:
                is_end = r.left or r.right

        while is_end:
            is_end = False
            _deep_recur += 1
            get_values(root, _deep, _deep_recur)
        print(list_values)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        list_values = []
        _deep = 0
        _deep_recur = 0
        is_end = True
        start = 0
        end = _range = 1

        def get_values(r, deep, _deep_recur):
            deep += 1
            nonlocal is_end
            if r:
                if deep == _deep_recur:
                    list_values.append(r.val)
                get_values(r.left, deep, _deep_recur)
                get_values(r.right, deep, _deep_recur)
            else:
                if deep == _deep_recur:
                    list_values.append(None)
                return
            if not is_end and deep == _deep_recur:
                is_end = r.left or r.right

        while is_end:
            is_end = False
            _deep_recur += 1
            before_count = len(list_values)
            get_values(root, _deep, _deep_recur)
            mid = (len(list_values) - before_count) // 2
            left = list_values[before_count:before_count + mid]
            right = list_values[before_count + mid:]
            if _deep_recur == 1:
                continue
            right.reverse()
            if left != right:
                return False
        return True

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        deep_count = 0
        deep_value = 0
        if not root:
            return deep_value

        def max_depth_recursion(left, right, deep):
            nonlocal deep_value
            deep += 1
            if left:
                max_depth_recursion(left.left, left.right, deep)
            if right:
                max_depth_recursion(right.left, right.right, deep)
            if deep > deep_value:
                deep_value = deep

        max_depth_recursion(root.left, root.right, deep_count)
        return deep_value

    def hasCycle(self, head) -> bool:
        if head and getattr(head, 'next', None):
            one = head
            two = head.next
        else:
            return False
        while one != two:
            if getattr(one, 'next', None):
                one = one.next
            else:
                return False
            if getattr(two, 'next', None):
                two = two.next.next
            else:
                return False
        return one is two
        # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

    #     if len(nums) == 1:
    #         return TreeNode(nums[0])
    #     mid_index = len(nums) // 2
    #     mid = nums[mid_index]
    #     left_tree = nums[:mid_index]
    #     right_tree = nums[mid_index + 1:]
    #     root = TreeNode(mid)
    #
    #     def create_branch(r, list_half):
    #         if list_half:
    #             mi = len(list_half) // 2
    #             mv = list_half[mi]
    #             node = TreeNode(mv)
    #             if mv <= r.val:
    #                 r.left = node
    #                 r = r.left
    #             else:
    #                 r.right = node
    #                 r = r.right
    #             create_branch(r, list_half[:mi])
    #             create_branch(r, list_half[mi + 1:])
    #
    #     create_branch(root, left_tree)
    #     create_branch(root, right_tree)
    #     return root

    def sortedArrayToBST(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0])
        tree_root = None

        def create_tree(list_nums, root=None):
            nonlocal tree_root
            if list_nums:
                mid_index = len(list_nums) // 2
                mid = list_nums[mid_index]
                left_tree = list_nums[:mid_index]
                right_tree = list_nums[mid_index + 1:]
                if not root:
                    root = TreeNode(mid)
                    tree_root = root
                    create_tree(left_tree, root)
                    create_tree(right_tree, root)
                else:
                    node = TreeNode(mid)
                    if mid <= root.val:
                        root.left = node
                        root = root.left
                    else:
                        root.right = node
                        root = root.right
                    create_tree(left_tree, root)
                    create_tree(right_tree, root)

        create_tree(nums)
        return tree_root

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        _deep = 0
        _deep_recur = 0
        is_end = True

        def traversal(r, deep, _deep_recur):
            deep += 1
            nonlocal is_end
            nonlocal is_balanced
            if r:
                if deep == _deep_recur:
                    dl = find_deep(r.left)
                    dr = find_deep(r.right)
                    # print(r.val, dl, dr)
                    if abs(dl - dr) > 1:
                        is_balanced = False
                        is_end = False
                        return
                traversal(r.left, deep, _deep_recur)
                traversal(r.right, deep, _deep_recur)
            else:
                return
            if not is_end and deep == _deep_recur:
                is_end = r.left or r.right

        def find_deep(r, _deep=0):
            if r:
                _deep += 1
                if r.left and r.right:
                    return max(find_deep(r.left, _deep), find_deep(r.right, _deep))
                elif r.right:
                    return find_deep(r.right, _deep)
                elif r.left:
                    return find_deep(r.left, _deep)
                else:
                    return _deep
            else:
                return _deep

        while is_end:
            is_end = False
            _deep_recur += 1
            traversal(root, _deep, _deep_recur)
        return is_balanced
        # deep = find_deep(root.left, deep)
        # print(deep)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 0

        def getMinDepth(r, deep=0):
            nonlocal min_depth
            if r is None:
                return
            deep += 1
            if r.left:
                getMinDepth(r.left, deep)
            if r.right:
                getMinDepth(r.right, deep)
            if r.left is None and r.right is None:
                if min_depth == 0 or deep < min_depth:
                    min_depth = deep

        getMinDepth(root)
        return min_depth

    # def minDepth(self, root: Optional[TreeNode]) -> int:

    # def getMinDepth(r, deep=0):
    #     if r is None:
    #         return
    #     deep += 1
    #     left = right = 0
    #     if r.left:
    #         left = getMinDepth(r.left, deep)
    #     if r.right:
    #         right = getMinDepth(r.right, deep)
    #     if r.left is None and r.right is None:
    #         return deep
    #     if left == 0 or right == 0:
    #         return max(left, right)
    #     else:
    #         return min(left, right)
    #
    # return getMinDepth(root)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def generate(self, numRows: int) -> List[List[int]]:
        _list = []
        tryangle = [[1]]
        for i in range(numRows):
            _list.append([1] + [0] * numRows)

        for i in range(1, numRows):
            tryangle.append([1])
            for j in range(1, i + 1):
                _list[i][j] = _list[i - 1][j - 1] + _list[i - 1][j]
                tryangle[i].append(_list[i][j])
        return tryangle

    def getRow(self, rowIndex: int) -> List[int]:
        _list = []
        rowIndex += 1
        tryangle = [[1]]
        for i in range(rowIndex):
            _list.append([1] + [0] * rowIndex)

        for i in range(1, rowIndex):
            tryangle.append([1])
            for j in range(1, i + 1):
                _list[i][j] = _list[i - 1][j - 1] + _list[i - 1][j]
                tryangle[i].append(_list[i][j])
        return tryangle[-1]

    def bypass_in_breadth(self, root):
        """
        Обход дерева в ширину
        :param root:
        :return:
        """
        current_list = [root]
        next_list = []
        while current_list:
            for node in current_list:
                print(node)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            current_list = next_list
            next_list = []

    def invert_tree(self, root):
        current_list = [root]
        next_list = []
        while current_list:
            for node in current_list:
                print(node)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
            current_list = next_list
            next_list = []
        return root

    def preorder(self, root):
        """
        Прямой обход дерева.
        :param root:
        :return:
        """
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def invert_preorder(self, root):
        if root:
            left = root.left
            right = root.right
            root.right = left
            root.left = right
            self.invert_preorder(left)
            self.invert_preorder(right)

    def postorder(self, root):
        """
        Обратный обход дерева
        :param root:
        :return:
        """
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    def inorder(self, root):
        """
        Симметричный обход дерева
        :param root:
        :return:
        """
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def maxProfit(self, prices: List[int]) -> int:
        _min = _max = prices[0]
        prof_list = []
        count = len(prices)
        for i, p in enumerate(prices):
            if p < _min and i < count - 1:
                _min = p
                _max = p
            if p > _max:
                _max = p
            prof_list.append(_max - _min)
        print(f'min:{_min} max:{_max}')
        print(prof_list)
        print(max(prof_list))
        return max(prof_list)

    def isPalindrome(self, s: str) -> bool:
        front_str = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                front_str += s[i].lower()
        back_str = front_str[::-1]
        return front_str == back_str

    def singleNumber(self, nums: List[int]) -> int:
        _dict = {}
        for n in nums:
            if n not in _dict:
                _dict[n] = 1
            else:
                del _dict[n]

        _list = list(_dict.keys())
        return _list[0]

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next

            if not pB:
                pB = headA
            else:
                pB = pB.next

        return pA

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            if current.val == val:
                if previous:
                    previous.next = current.next
                    current = current.next
                    continue
                else:
                    head = current.next
                    current = current.next
                    continue
            previous = current
            current = current.next
        while head:
            print(head, end=" ")
            head = head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
        head = previous
        while head:
            print(head, end=' ')
            head = head.next

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        one_list = [root]
        two_list = []
        while one_list:
            node = one_list.pop(0)
            # print(node)
            left_node = None
            right_node = None
            if node.left:
                left_node = node.left
                two_list.append(left_node)
            if node.right:
                right_node = node.right
                two_list.append(right_node)
            node.left = right_node
            node.right = left_node
            if not one_list:
                one_list = two_list
                two_list = []
        return root

    def isPowerOfTwo(self, n: int) -> bool:
        return n and not n & n - 1

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _stack = []
        while head:
            _stack.append(head.val)
            head = head.next
        return _stack == _stack[::-1]

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            lit_s = s[i]
            lit_t = t[i]
            if lit_s in dict_s:
                dict_s[lit_s] = dict_s[lit_s] + 1
            else:
                dict_s[lit_s] = 1
            if lit_t in dict_t:
                dict_t[lit_t] = dict_t[lit_t] + 1
            else:
                dict_t[lit_t] = 1
        return dict_s == dict_t

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        list_str = []

        def recursive_traversal(r, _str=''):

            if r:
                _str += str(r.val) + '->'
                if not r.left and not r.right:
                    list_str.append(_str[:-2])
                    return
                recursive_traversal(r.left, _str)
                recursive_traversal(r.right, _str)

        recursive_traversal(root)
        print(list_str)
        return list_str

    def addDigits(self, num: int) -> int:

        def get_digits(n):
            if n > 0:
                rem = n % 10
                # _list.append(rem)
                n = n - rem
                n //= 10
                return rem + get_digits(n)
            else:
                return 0

        while num >= 10:
            num = get_digits(num)
        print(num)
        return num

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1

    def missingNumber(self, nums: List[int]) -> int:
        # initialize missing_num to n
        missing_num = len(nums)

        # loop through the array nums
        for i, num in enumerate(nums):
            # perform XOR operation with index and element
            ind = i ^ num
            missing_num ^= ind

        # return the missing number
        return missing_num

    def firstBadVersion(self, n: int) -> int:

        start = 0
        end = n
        while (end - start) > 1:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        return end

    def moveZeroes(self, nums: List[int]) -> None:

        index = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[index], nums[j] = nums[j], nums[index]
                index += 1
        print(nums)

    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split()
        # a = set(pattern)
        # b = set(s)
        # z = zip(a, b)
        # z = set(z)
        # print(z)
        # return len(a) == len(b) == len(z)
        s = s.split()
        a = set(pattern)
        b = set(s)
        z = set(zip_longest(pattern, s))
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern, s))))


class NumArray:
    def __init__(self, nums):
        self.list_summ = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.list_summ[i + 1] = self.list_summ[i] + nums[i]
        print(self.list_summ)
        print(nums)


def display_tree(root, display_none=False, width=80, factor=0.5, count_print=3):
    """
    Отображает в консоли 'двоичное дерево'.
    :param root: Дерево.
    :param display_none: True отображает None.
    :param width: Ширина отступа между узлами.
    :param factor: Множитель уменьшающий ширину отступа в зависимости от глубины дерева.
    :param count_print: Высота вертикального отступа между узлами
    :return:
    """
    if display_none:
        zero = 'None'
    else:
        zero = ' '
    current_list = [root]
    next_list = []
    while current_list:
        for node in current_list:
            if node:
                print(f'{node.val:^{width}}', end='')
                if node.left:
                    next_list.append(node.left)
                else:
                    next_list.append(None)
                if node.right:
                    next_list.append(node.right)
                else:
                    next_list.append(None)
            else:
                print(f'{zero:^{width}}', end='')
        print('', end='\n' * count_print)
        if next_list.count(None) == len(next_list):
            next_list = []
        current_list = next_list
        next_list = []
        width -= round(width * factor)
        print()


def create_tree_node(a_list):
    root = TreeNode(a_list.pop(0))
    current_list = [root]
    next_list = []
    while a_list:
        for node in current_list:
            if node:
                if a_list:
                    left = a_list.pop(0)
                    if left:
                        node.left = TreeNode(left)
                if a_list:
                    right = a_list.pop(0)
                    if right:
                        node.right = TreeNode(right)
                next_list.append(node.left)
                next_list.append(node.right)
        current_list = next_list
        next_list = []
    return root


def isBadVersion(n):
    if n >= 99:
        return True
    else:
        return False
