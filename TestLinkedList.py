class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        if self.head is None:
            return str(None)
        current = self.head
        _str = f'[{current}'
        while current.next:
            current = current.next
            _str += f', {current}'
        return _str + ']'

    def remove(self, data):
        if self.head is None:
            raise ValueError('value not found')
        if self.head.val == data:
            self.head = self.head.next
            return
        current = self.head.next
        previous = self.head
        try:
            while current.val != data:
                previous = current
                current = current.next
            previous.next = current.next
        except AttributeError:
            raise ValueError('value not found')
        return current

    def is_contains(self, data):
        is_contains = False
        if self.head is None:
            return is_contains
        current = self.head
        while current:
            if current.val == data:
                is_contains = True
                return is_contains
            current = current.next
        return is_contains

    def revers(self):
        if self.head is None:
            return
        current = self.head
        previous = None
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
        self.head = previous

    def get_node(self, data):
        node = None
        if self.head is None:
            return node
        current = self.head
        while current:
            if current.val == data:
                node = current
                return node
            current = current.next
        return node

    def is_cycle(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                print(f'slow:{slow} fast{fast}')
                if slow is fast:
                    print(f'slow:{slow} = fast{fast}')
                    return True
        except:
            return False


def create_linked_list(a_list):
    head = None
    current_node = None
    for n in a_list:
        if head is None:
            head = Node(n)
            current_node = head
        else:
            current_node.next = Node(n)
            current_node = current_node.next
    return head
