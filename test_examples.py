def check_bracket(_str):
    list_brackets = []
    for s in _str:
        if s == '(':
            list_brackets.append(s)
        if s == '{':
            list_brackets.append(s)
        if s == ')':
            if len(list_brackets) > 0:
                if list_brackets[-1] == '{':
                    return False
                else:
                    list_brackets.pop()
            else:
                return False
        if s == '}':
            if len(list_brackets) > 0:
                if list_brackets[-1] == '(':
                    return False
                else:
                    list_brackets.pop()
            else:
                return False

    return len(list_brackets) == 0


class Stack_max:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, data):
        if len(self.main) == 0:
            self.max.append(data)
        elif data >= self.max[-1]:
            self.max.append(data)
        else:
            self.max.append(self.max[-1])
        self.main.append(data)

    def pop(self):
        pop_data = self.main.pop()
        return pop_data

    def max_n(self):
        max_data = self.max.pop()
        return max_data

    def is_empty(self):
        return len(self.max) != 0


class My_Queue:
    def __init__(self):
        self.st_1 = []
        self.st_2 = []
        self._size = 0

    def enqueue(self, data):
        self._size += 1
        self.st_1.append(data)

    def dequeue(self):
        if len(self.st_1) == 0:
            raise IndexError('My_Queue is empty')
        self._size -= 1
        while len(self.st_1) != 0:
            self.st_2.append(self.st_1.pop())
        temp = self.st_2.pop()
        while len(self.st_2) != 0:
            self.st_1.append(self.st_2.pop())
        return temp

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __repr__(self):
        return str(self.st_1)


def is_min_heap(root):
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
                if node.val > node.left.val:
                    return False
            if node.right:
                next_list.append(node.right)
                if node.val > node.right.val:
                    return False
        current_list = next_list
        next_list = []
    return True
