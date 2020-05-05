import unittest

from acommonsenseguide.codebase.doublylinkedlist import DoublyLinkedList, DoublyNode


class LinkedTests(unittest.TestCase):
    def test_node_value(self):
        value = 'first'
        node = DoublyNode(value)
        self.assertEqual(node.data, value, 'Node Data field is incorrect')

    def test_node_rightleftlinks_none(self):
        node = DoublyNode('asd')
        self.assertEqual(node.rightlink, None, 'Node RightLink should be None')
        self.assertEqual(node.leftlink, None, 'Node LeftLink should be None')

    def test_node_repr(self):
        node_1 = DoublyNode('anynode')
        self.assertEqual(node_1.__repr__(), "Node('anynode')")

    def test_node_str(self):
        node_1 = DoublyNode('anynode')
        self.assertEqual(node_1.__str__(), '| anynode |')

    def test_doubly_str(self):
        doubly = DoublyLinkedList(['first', 'second', 'third'])

        self.assertEqual(doubly.__str__(), 'None <-> | first | <-> | second | <-> | third | <-> None')

    def test_doubly_repr(self):
        doubly = DoublyLinkedList(['first', 'second', 'third'])

        self.assertEqual(doubly.__repr__(), "DoublyLinkedList(['first', 'second', 'third'])")

    def test_empty_array_doublylist(self):
        with self.assertRaises(IndexError):
            DoublyLinkedList([])

    def test_one_element_doublylist(self):
        doubly = DoublyLinkedList(['one'])

        self.assertEqual(doubly.get_node_by_index_from_top(0).data, 'one')
        self.assertEqual("| one |", doubly.first_node.__str__())
        self.assertEqual("| one |", doubly.last_node.__str__())

    def test_two_element_doublylist(self):
        first, second = 'first', 'second'
        doubly = DoublyLinkedList([first, second])

        self.assertEqual(doubly.get_node_by_index_from_top(0).data, first)
        self.assertEqual(doubly.get_node_by_index_from_top(0).leftlink, None)
        self.assertEqual(doubly.get_node_by_value_from_top(first).rightlink.data, second)

        self.assertEqual(doubly.get_node_by_index_from_top(1).data, second)
        self.assertEqual(doubly.get_node_by_index_from_bottom(0).leftlink.data, first)
        self.assertEqual(doubly.get_node_by_value_from_bottom(second).rightlink, None)

        self.assertEqual("| first |", doubly.first_node.__str__())
        self.assertEqual("| second |", doubly.last_node.__str__())

    def test_get_index_by_value(self):
        doubly = DoublyLinkedList(['first', 'second', 'third'])

        self.assertEqual(doubly.get_index_by_value_from_top('second'), 1)
        self.assertEqual(doubly.get_index_by_value_from_bottom('third'), 0)

    def test_insert_to_the_top(self):
        doubly = DoublyLinkedList(['first', 'second', 'third'])

        self.assertEqual(doubly.get_node_by_index_from_top(0).data, 'first')

        doubly.insert_to_the_top('very first')

        self.assertEqual(doubly.__repr__(), "DoublyLinkedList(['very first', 'first', 'second', 'third'])")
        self.assertEqual(doubly.get_node_by_index_from_top(0).data, 'very first')
        self.assertEqual(doubly.get_node_by_index_from_top(1).data, 'first')
        self.assertEqual(doubly.get_node_by_index_from_top(1).leftlink.data, 'very first')
        self.assertEqual(doubly.get_node_by_index_from_top(0).rightlink.data, 'first')
        self.assertEqual(doubly.get_node_by_index_from_top(0).leftlink, None)
        self.assertEqual(doubly.first_node.data, 'very first')

    def test_insert_to_the_bottom(self):
        doubly = DoublyLinkedList(['first', 'second', 'third'])

        self.assertEqual(doubly.get_node_by_index_from_bottom(0).data, 'third')

        doubly.insert_to_the_bottom('fourth')

        self.assertEqual("DoublyLinkedList(['first', 'second', 'third', 'fourth'])", doubly.__repr__())
        self.assertEqual(doubly.get_node_by_index_from_bottom(0).data, 'fourth')
        self.assertEqual(doubly.get_node_by_index_from_bottom(1).data, 'third')
        self.assertEqual(doubly.get_node_by_index_from_bottom(1).rightlink.data, 'fourth')
        self.assertEqual(doubly.get_node_by_index_from_bottom(0).leftlink.data, 'third')
        self.assertEqual(doubly.get_node_by_index_from_bottom(0).rightlink, None)
        self.assertEqual(doubly.last_node.data, 'fourth')

    def test_insert_in_the_middle(self):
        doubly = DoublyLinkedList(['first', 'third', 'fourth'])

        self.assertEqual(doubly.get_node_by_index_from_top(1).data, 'third')

        doubly.insert_at_index(1, 'second')

        self.assertEqual("DoublyLinkedList(['first', 'second', 'third', 'fourth'])", doubly.__repr__())
        self.assertEqual(doubly.get_node_by_index_from_top(1).data, 'second')
        self.assertEqual(doubly.get_node_by_index_from_top(2).data, 'third')
        self.assertEqual(doubly.get_node_by_index_from_top(0).rightlink.data, 'second')
        self.assertEqual(doubly.get_node_by_index_from_top(1).leftlink.data, 'first')
        self.assertEqual(doubly.get_node_by_index_from_top(1).rightlink.data, 'third')
        self.assertEqual(doubly.get_node_by_index_from_top(2).leftlink.data, 'second')

        doubly.insert_at_index(0, 'very first')
        doubly.insert_at_index(5, 'very last')
        self.assertEqual(None, doubly.insert_at_index(7, 'out of range'))

        self.assertEqual('very first', doubly.first_node.data)
        self.assertEqual('very last', doubly.last_node.data)
        self.assertEqual("DoublyLinkedList(['very first', 'first', 'second', 'third', 'fourth', 'very last'])", doubly.__repr__())

    def test_delete_from_the_top(self):
        doubly = DoublyLinkedList(['very first', 'first', 'second', 'third', 'fourth', 'very last'])

        doubly.delete_from_the_top()
        self.assertEqual("DoublyLinkedList(['first', 'second', 'third', 'fourth', 'very last'])", doubly.__repr__())
        self.assertEqual('first', doubly.first_node.data)
        self.assertEqual(None, doubly.first_node.leftlink)
        self.assertEqual('second', doubly.first_node.rightlink.data)

    def test_delete_from_the_bottom(self):
        doubly = DoublyLinkedList(['very first', 'first', 'second', 'third', 'fourth', 'very last'])

        doubly.delete_from_the_bottom()
        self.assertEqual("DoublyLinkedList(['very first', 'first', 'second', 'third', 'fourth'])", doubly.__repr__())
        self.assertEqual('fourth', doubly.last_node.data)
        self.assertEqual(None, doubly.last_node.rightlink)
        self.assertEqual('third', doubly.last_node.leftlink.data)

    def test_delete_at_index(self):
        doubly = DoublyLinkedList(['very first', 'first', 'second', 'third', 'fourth', 'very last'])

        self.assertEqual('second', doubly.get_node_by_index_from_top(2).data)
        doubly.delete_at_index(2)
        self.assertEqual('third', doubly.get_node_by_index_from_top(2).data)
        self.assertEqual("DoublyLinkedList(['very first', 'first', 'third', 'fourth', 'very last'])", doubly.__repr__())
        self.assertEqual('first', doubly.get_node_by_index_from_top(2).leftlink.data)
        self.assertEqual('third', doubly.get_node_by_index_from_top(1).rightlink.data)

        doubly.delete_from_the_bottom()
        doubly.delete_from_the_top()
        self.assertEqual("DoublyLinkedList(['first', 'third', 'fourth'])", doubly.__repr__())

        self.assertEqual('fourth', doubly.last_node.data)
        self.assertEqual(None, doubly.last_node.rightlink)
        self.assertEqual('third', doubly.last_node.leftlink.data)

        self.assertEqual('first', doubly.first_node.data)
        self.assertEqual(None, doubly.first_node.leftlink)
        self.assertEqual('third', doubly.first_node.rightlink.data)

    def test_delete_from_one_element_list(self):
        doubly = DoublyLinkedList(['first'])

        with self.assertRaises(IndexError):
            doubly.delete_from_the_bottom()

        with self.assertRaises(IndexError):
            doubly.delete_from_the_top()

        with self.assertRaises(IndexError):
            doubly.delete_at_index(1)


if __name__ == "__main__":
    unittest.main(verbosity=2)