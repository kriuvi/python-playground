class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return '| {0} |'.format(self.data)

    def __repr__(self):
        if isinstance(self.data, int) or isinstance(self.data, float):
            return "Node({0})".format(self.data)
        else:
            return "Node('{0}')".format(self.data)


class OutOfRangeError(Exception):
    pass


class LinkedList:

    def __init__(self, list_of_values):
        if not list_of_values:
            self.first_node = None
            return
        self.first_node = node = Node(list_of_values[0])
        for val in list_of_values[1:]:
            new_node = Node(val)
            node.next, node = new_node, new_node

    def __str__(self):
        if self.is_empty():
            return '| None | -> None'
        node, i = self.first_node, 0
        repres = list()
        while node:
            repres.append(str(node))
            repres.append(' -> ')
            node, i = node.next, i+1
        repres.append('None')
        return ''.join(repres)

    def __repr__(self):
        node = self.first_node
        values = list()
        while node:
            values.append(node.data)
            node = node.next
        return "LinkedList({0})".format(values)

    def __contains__(self, item):
        return True if self.find_index(item) else False

    def __iter__(self):
        node = self.first_node
        while node:
            yield node
            node = node.next

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented

        for node_self, node_other in zip(self, other):
            if node_self.data != node_other.data:
                return False
            elif not node_self.next and not node_other.next:
                return True
            elif not node_self.next or not node_other.next:
                return False
        return True

    def get_node_at_index(self, index):
        node, i = self.first_node, 0
        while i <= index:
            if i != index and not node:
                raise OutOfRangeError
            elif i == index:
                return node
            node, i = node.next, i+1

    def get_node_with_value(self, value):
        node = self.first_node
        while node:
            if node.data == value:
                return node
            node = node.next
        return None

    def find_index(self, value):
        node, i = self.first_node, 0
        while node:
            if node.data == value:
                return i
            node, i = node.next, i+1
        return None

    def insert_to_the_top(self, value):
        new_node = Node(value)
        new_node.next = self.first_node
        self.first_node = new_node

    def insert_to_the_bottom(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.first_node = new_node
            return True

        node = self.first_node
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            self.insert_to_the_top(value)
            return True
        else:
            node, i = self.first_node, 0
            while i <= index and node:
                if index-1 == i:
                    node.next, new_node.next = new_node, node.next
                    return True
                node, i = node.next, i+1
        raise OutOfRangeError

    def delete_from_top(self):
        if self.is_empty():
            raise IndexError
        self.first_node = self.first_node.next

    def delete_from_bottom(self):
        node = prev = self.first_node

        if self.is_empty():
            raise IndexError
        elif not node.next:
            self.first_node = None
        else:
            while node.next:
                prev, node = node, node.next
            prev.next = None

    def delete_at_index(self, index):
        node = prev = self.first_node

        if self.is_empty():
            raise OutOfRangeError
        elif index == 0:
            self.delete_from_top()
            return True
        else:
            i = 0
            while node.next:
                if i == index-1:
                    node.next = node.next.next
                    return True
                prev, node = node, node.next
                i += 1
            raise OutOfRangeError

    def is_empty(self):
        return True if not self.first_node else False
