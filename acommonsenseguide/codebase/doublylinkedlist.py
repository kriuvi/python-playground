class DoublyNode:

    def __init__(self, data):
        self.data = data
        self.leftlink = None
        self.rightlink = None

    def __str__(self):
        return '| {0} |'.format(self.data)

    def __repr__(self):
        return "Node('{0}')".format(self.data)

    def getdata(self):
        return self.data


class DoublyLinkedList:

    def __init__(self, list_of_values):
        if not list_of_values:
            raise IndexError

        self.first_node = self.last_node = DoublyNode(list_of_values[0])
        for val in list_of_values[1:]:
            self.insert_to_the_bottom(val)

    def __str__(self):
        node, i = self.first_node, 0
        repres = list()
        repres.append('None <-> ')
        while node:
            repres.append(str(node))
            repres.append(' <-> ')
            node, i = node.rightlink, i+1
        repres.append('None')
        return ''.join(repres)

    def __repr__(self):
        node, i = self.first_node, 0
        values = list()
        while node:
            values.append(node.data)
            node, i = node.rightlink, i+1
        return "DoublyLinkedList({0})".format(values)

    def get_node_by_index_from_top(self, index):
        node, i = self.first_node, 0
        while i < index:
            node, i = node.rightlink, i+1
        return node

    def get_node_by_index_from_bottom(self, index):
        node, i = self.last_node, 0
        while i < index:
            node, i = node.leftlink, i+1
        return node

    def get_node_by_value_from_top(self, value):
        node = self.first_node
        while node:
            if node.data == value:
                return node
            node = node.rightlink
        return None

    def get_node_by_value_from_bottom(self, value):
        node = self.last_node
        while node:
            if node.getdata() == value:
                return node
            node = node.leftlink
        return None

    def get_index_by_value_from_top(self, value):
        node, i = self.first_node, 0
        while node:
            if node.data == value:
                return i
            node, i = node.rightlink, i+1
        return None

    def get_index_by_value_from_bottom(self, value):
        node, i = self.last_node, 0
        while node:
            if node.data == value:
                return i
            node, i = node.leftlink, i+1
        return None

    def insert_to_the_top(self, value):
        new_node = DoublyNode(value)
        new_node.rightlink = self.first_node
        self.first_node.leftlink = new_node
        self.first_node = new_node

    def insert_to_the_bottom(self, value):
        new_node = DoublyNode(value)
        new_node.leftlink = self.last_node
        self.last_node.rightlink = new_node
        self.last_node = new_node

    def insert_at_index(self, index, value):
        new_node = DoublyNode(value)

        if index == 0:
            self.insert_to_the_top(value)
            return index
        node, i = self.first_node, 0
        while node:
            if index == i+1 and node == self.last_node:
                self.insert_to_the_bottom(value)
                break
            if index == i:
                new_node.leftlink = node.leftlink
                new_node.rightlink = node
                node.leftlink.rightlink = new_node
                node.leftlink = new_node
                return index
            node, i = node.rightlink, i+1
        return None

    def delete_from_the_top(self):
        if self.last_node == self.first_node:
            raise IndexError
        self.first_node.rightlink.leftlink = None
        self.first_node = self.first_node.rightlink

    def delete_from_the_bottom(self):
        if self.last_node == self.first_node:
            raise IndexError
        self.last_node.leftlink.rightlink = None
        self.last_node = self.last_node.leftlink

    def delete_at_index(self, index):
        if index == 0:
            self.delete_from_the_top()

        node, i = self.first_node.rightlink, 1
        while i <= index:
            if not node:
                raise IndexError
            if i == index:
                if node == self.last_node:
                    self.delete_from_the_bottom()
                    break
                node.leftlink.rightlink, node.rightlink.leftlink = node.rightlink, node.leftlink
            node, i = node.rightlink, i+1
        return None
