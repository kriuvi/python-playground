import unittest

from acommonsenseguide.codebase.linkedlist import LinkedList, Node, OutOfRangeError


class NodeTests(unittest.TestCase):
    def test_node_value(self):
        value = 'first'
        node = Node(value)
        self.assertEqual(value, node.data)
        self.assertEqual(None, node.next)

    def test_node_next(self):
        node_1 = Node('first')
        node_2 = Node('second')
        node_1.next = node_2

        self.assertEqual('first', node_1.data)
        self.assertEqual('second', node_1.next.data)
        self.assertEqual('second', node_2.data)
        self.assertEqual(None, node_2.next)

    def test_node_repr(self):
        node_1 = Node('anynode')
        self.assertEqual(node_1.__repr__(), "Node('anynode')")

    def test_node_str(self):
        node_1 = Node('anynode')
        self.assertEqual(node_1.__str__(), '| anynode |')


class LinkedTests(unittest.TestCase):

    def test_init_empty_list(self):
        self.assertEqual(None, LinkedList([]).first_node)

    def test_generator(self):
        linked = LinkedList(['one'])

        for node in linked:
            self.assertEqual(node.data, 'one')

    def test_equality_empty(self):
        self.assertEqual(LinkedList([]), LinkedList([]))

    def test_equality_one(self):
        self.assertEqual(LinkedList(['one']), LinkedList(['one']))

    def test_equality_two(self):
        self.assertNotEqual(LinkedList(['one']), LinkedList(['two']))

    def test_equality_not_equal(self):
        self.assertNotEqual(LinkedList(['one']), LinkedList(['one', 'two']))

    def test_equality_to_list(self):
        self.assertNotEqual(LinkedList(['one']), ['one'])

    def test_init_one_element_list(self):
        linked = LinkedList(['one'])

        self.assertEqual('one', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_init_many_element_list(self):
        linked = LinkedList(['pear', 'apple', 'banana'])

        self.assertEqual('pear', linked.first_node.data)
        self.assertEqual('apple', linked.first_node.next.data)
        self.assertEqual('banana', linked.first_node.next.next.data)
        self.assertEqual(None, linked.first_node.next.next.next)

    def test_str_empty_list(self):
        self.assertEqual(LinkedList([]).__str__(), '| None | -> None')

    def test_str_one_element(self):
        self.assertEqual(LinkedList(['one']).__str__(), '| one | -> None')

    def test_str_many_elements(self):
        self.assertEqual(LinkedList(['first', 'second', 'third']).__str__(),
                         '| first | -> | second | -> | third | -> None')

    def test_repr_empty_list(self):
        self.assertEqual(LinkedList([]).__repr__(), 'LinkedList([])')

    def test_repr_one_element(self):
        self.assertEqual(LinkedList([3456]).__repr__(), 'LinkedList([3456])')

    def test_repr_many_elements(self):
        self.assertEqual(LinkedList([1, 2, 3, 4]).__repr__(), 'LinkedList([1, 2, 3, 4])')

    def test_is_empty_true(self):
        self.assertTrue(LinkedList([]).is_empty())

    def test_is_empty_false(self):
        self.assertFalse(LinkedList([4.5]).is_empty())

    def test_find_index_empty_list(self):
        linked = LinkedList([])
        self.assertEqual(None, linked.find_index(2))

    def test_find_index_value_exist_0(self):
        linked = LinkedList(['one', 'two'])
        self.assertEqual(0, linked.find_index('one'))

    def test_find_index_value_exist_1(self):
        linked = LinkedList(['one', 'two'])
        self.assertEqual(1, linked.find_index('two'))

    def test_find_index_multiple_values_exist(self):
        linked = LinkedList(['one', 'two', 'third', 4, 6, 'pear', 4])
        self.assertEqual(3, linked.find_index(4))

    def test_find_index_value_doesnot_exist(self):
        linked = LinkedList(['one', 'two', 'third', 4, 6, 'pear', 4])
        self.assertEqual(None, linked.find_index('four'))

    def test_get_node_index_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(OutOfRangeError):
            linked.get_node_at_index(2)

    def test_get_node_index_exists_0(self):
        linked = LinkedList(['one', 'two'])
        self.assertEqual('one', linked.get_node_at_index(0).data)

    def test_get_node_index_exists_1(self):
        linked = LinkedList(['one', 'two'])
        self.assertEqual('two', linked.get_node_at_index(1).data)

    def test_get_node_index_doesnot_exist(self):
        linked = LinkedList(['one', 'two', 3, 4, 5])
        with self.assertRaises(OutOfRangeError):
            linked.get_node_at_index(6)

    def test_get_node_value_empty_list(self):
        linked = LinkedList([])
        self.assertEqual(None, linked.get_node_with_value('one'))

    def test_get_node_value_exists_0(self):
        linked = LinkedList(['one', 'two'])
        self.assertEqual('one', linked.get_node_with_value('one').data)

    def test_get_node_value_exists_1(self):
        linked = LinkedList(['one', 'two', 3])
        self.assertEqual(3, linked.get_node_with_value(3).data)

    def test_get_node_value_doesnot_exist(self):
        linked = LinkedList(['one', 'two', 3, 4, 5])
        self.assertEqual(None, linked.get_node_with_value(6.7))

    def test_insert_top_empty_list(self):
        linked = LinkedList([])
        linked.insert_to_the_top('first')
        self.assertEqual('first', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_insert_top(self):
        linked = LinkedList(['two', 3])
        linked.insert_to_the_top(1)
        self.assertEqual(1, linked.first_node.data)
        self.assertEqual('two', linked.first_node.next.data)

    def test_insert_bottom_empty_list(self):
        linked = LinkedList([])
        linked.insert_to_the_bottom('first')
        self.assertEqual('first', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_insert_bottom_one_element_list(self):
        linked = LinkedList(['one'])
        linked.insert_to_the_bottom(2)
        self.assertEqual('one', linked.first_node.data)
        self.assertEqual(2, linked.first_node.next.data)

    def test_insert_bottom_many_element_list(self):
        linked = LinkedList(['one', 'two', 3])
        linked.insert_to_the_bottom(4.34)
        self.assertEqual(4.34, linked.get_node_with_value(4.34).data)
        self.assertEqual(None, linked.get_node_with_value(4.34).next)
        self.assertEqual("| one | -> | two | -> | 3 | -> | 4.34 | -> None", str(linked))

    def test_insert_index_0_empty_list(self):
        linked = LinkedList([])
        linked.insert_at_index(0, 'first')
        self.assertEqual('first', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_insert_index_1_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(OutOfRangeError):
            linked.insert_at_index(1, 'first')

    def test_insert_index_0_one_element_list(self):
        linked = LinkedList([2])
        linked.insert_at_index(0, 'first')
        self.assertEqual('first', linked.first_node.data)
        self.assertEqual(2, linked.first_node.next.data)

    def test_insert_index_1_one_element_list(self):
        linked = LinkedList(['one'])
        linked.insert_at_index(1, 2)
        self.assertEqual('one', linked.first_node.data)
        self.assertEqual(2, linked.first_node.next.data)

    def test_insert_index_2_one_element_list(self):
        linked = LinkedList(['one'])
        with self.assertRaises(OutOfRangeError):
            linked.insert_at_index(2, 'second')

    def test_insert_index_2_many_element_list(self):
        linked = LinkedList(['one', 'two', 4])
        linked.insert_at_index(2, '3')
        self.assertEqual('3', linked.get_node_with_value('3').data)
        self.assertEqual(4, linked.get_node_with_value('3').next.data)
        self.assertEqual("| one | -> | two | -> | 3 | -> | 4 | -> None", str(linked))

    def test_delete_top_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(IndexError):
            linked.delete_from_top()

    def test_delete_top_one_element_list(self):
        linked = LinkedList(['two'])
        linked.delete_from_top()
        self.assertEqual(None, linked.first_node)

    def test_delete_top_two_element_list(self):
        linked = LinkedList(['one', 'two'])
        linked.delete_from_top()
        self.assertEqual('two', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_delete_bottom_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(IndexError):
            linked.delete_from_bottom()

    def test_delete_bottom_one_element_list(self):
        linked = LinkedList(['one'])
        linked.delete_from_bottom()
        self.assertEqual(None, linked.first_node)

    def test_delete_bottom_two_element_list(self):
        linked = LinkedList(['one', 'two'])
        linked.delete_from_bottom()
        self.assertEqual('one', linked.first_node.data)
        self.assertEqual(None, linked.first_node.next)

    def test_delete_bottom_many_element_list(self):
        linked = LinkedList(['one', 'two', 3, 4, 5, 6])
        linked.delete_from_bottom()
        self.assertEqual("| one | -> | two | -> | 3 | -> | 4 | -> | 5 | -> None", str(linked))

    def test_delete_index_0_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(OutOfRangeError):
            linked.delete_at_index(0)

    def test_delete_index_1_empty_list(self):
        linked = LinkedList([])
        with self.assertRaises(OutOfRangeError):
            linked.delete_at_index(1)

    def test_delete_index_0_one_element_list(self):
        linked = LinkedList(['one'])
        linked.delete_at_index(0)
        self.assertEqual(None, linked.first_node)

    def test_delete_index_1_one_element_list(self):
        linked = LinkedList(['one'])
        with self.assertRaises(OutOfRangeError):
            linked.delete_at_index(1)

    def test_delete_index_0_many_element_list(self):
        linked = LinkedList(['one', 'two', 3, 4])
        linked.delete_at_index(0)
        self.assertEqual("| two | -> | 3 | -> | 4 | -> None", str(linked))

    def test_delete_index_2_many_element_list(self):
        linked = LinkedList(['one', 'two', 3, 4])
        linked.delete_at_index(2)
        self.assertEqual("| one | -> | two | -> | 4 | -> None", str(linked))

    def test_delete_index_3_many_element_list(self):
        linked = LinkedList(['one', 'two', 3, 4])
        linked.delete_at_index(3)
        self.assertEqual("| one | -> | two | -> | 3 | -> None", str(linked))

    def test_delete_index_5_many_element_list(self):
        linked = LinkedList(['one', 'two', 3, 4])
        with self.assertRaises(OutOfRangeError):
            linked.delete_at_index(5)


if __name__ == "__main__":
    unittest.main(verbosity=2)