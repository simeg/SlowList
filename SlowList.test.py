#!/bin/python

import unittest

from SlowList import SlowList


class TestSlowList(unittest.TestCase):

    def test_constructor__no_arguments(self):
        slow_list = SlowList()
        self.assertTrue(isinstance(slow_list, SlowList))

    def test_add__when_single_string(self):
        slow_list = SlowList()
        slow_list.add("e1")
        expected = "'e1'"
        self.assertEqual(slow_list.get(0), expected)

    def test_add__when_multiple_string(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")

        expected_e1 = "'e1'"
        expected_e2 = "'e2'"
        actual_e1 = slow_list.get(0)
        actual_e2 = slow_list.get(1)

        self.assertEqual(actual_e1, expected_e1)
        self.assertEqual(actual_e2, expected_e2)

    def test_add__when_single_number(self):
        slow_list = SlowList()
        slow_list.add(1)
        expected = '1'
        self.assertEqual(slow_list.get(0), expected)

    def test_add__when_multiple_number(self):
        slow_list = SlowList()
        slow_list.add(1)
        slow_list.add(9)

        expected_e1 = '1'
        expected_e2 = '9'
        actual_e1 = slow_list.get(0)
        actual_e2 = slow_list.get(1)

        self.assertEqual(actual_e1, expected_e1)
        self.assertEqual(actual_e2, expected_e2)

    def test_add__when_string_then_number(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add(9)

        expected_e1 = "'e1'"
        expected_e2 = '9'
        actual_e1 = slow_list.get(0)
        actual_e2 = slow_list.get(1)

        self.assertEqual(actual_e1, expected_e1)
        self.assertEqual(actual_e2, expected_e2)

    def test_add_at__at_start_of_list(self):
        slow_list = SlowList()
        slow_list.addAt(0, "e1")

        expected = "'e1'"
        actual = slow_list.get(0)

        self.assertEqual(actual, expected)

    def test_add_at__in_middle_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e4")
        slow_list.addAt(2, "e3")

        expected = "'e3'"
        actual = slow_list.get(2)

        self.assertEqual(actual, expected)

    def test_add_at__at_end_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.addAt(2, "e3")

        expected = "'e3'"
        actual = slow_list.get(2)

        self.assertEqual(actual, expected)

    def test_add_at__if_index_too_big(self):
        slow_list = SlowList()
        slow_list.add("e1")

        with self.assertRaises(IndexError) as cm:
            slow_list.addAt(2, "e1")

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_add_at__if_index_too_small(self):
        slow_list = SlowList()

        with self.assertRaises(IndexError) as cm:
            slow_list.addAt(-1, "e1")

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_clear(self):
        slow_list = SlowList()
        slow_list.add(9)
        expected = '9'
        self.assertEqual(slow_list.get(0), expected)

        slow_list.clear()
        with self.assertRaises(IndexError):
            slow_list.get(0)

    def test_contains__when_true(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add(9)

        self.assertTrue(slow_list.contains("e1"))
        self.assertTrue(slow_list.contains(9))

    def test_contains__when_false(self):
        slow_list = SlowList()
        slow_list.add("e1")

        self.assertFalse(slow_list.contains("e2"))
        self.assertFalse(slow_list.contains(9))

    def test_get__when_empty_list(self):
        slow_list = SlowList()

        with self.assertRaises(IndexError) as cm:
            slow_list.get(0)

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_get__when_list_is_populated(self):
        slow_list = SlowList()
        slow_list.add(1)
        slow_list.add("e1")

        expected_e1 = '1'
        expected_e2 = "'e1'"
        actual_e1 = slow_list.get(0)
        actual_e2 = slow_list.get(1)
        self.assertEqual(actual_e1, expected_e1)
        self.assertEqual(actual_e2, expected_e2)

    def test_get__when_index_too_high(self):
        slow_list = SlowList()
        slow_list.add(1)

        with self.assertRaises(IndexError) as cm:
            slow_list.get(1)

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_get__when_index_too_low(self):
        slow_list = SlowList()
        slow_list.add("e1")

        with self.assertRaises(IndexError) as cm:
            slow_list.get(-1)

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_index_of__when_element_present(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        expected = 1
        actual = slow_list.index_of("e2")
        self.assertEqual(actual, expected)

    def test_index_of__when_multiple_elements_present(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e1")
        slow_list.add("e1")

        expected = 0
        actual = slow_list.index_of("e1")
        self.assertEqual(actual, expected)

    def test_index_of__when_element_missing(self):
        slow_list = SlowList()
        slow_list.add("e1")

        expected = -1
        actual = slow_list.index_of("e2")
        self.assertEqual(actual, expected)

    def test_index_of__when_empty_list(self):
        slow_list = SlowList()

        expected = -1
        actual = slow_list.index_of("e1")
        self.assertEqual(actual, expected)

    def test_is_empty(self):
        slow_list = SlowList()
        self.assertTrue(slow_list.is_empty())
        slow_list.add("e1")
        self.assertFalse(slow_list.is_empty())

    def test_last_index_of__when_element_present(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        expected = 1
        actual = slow_list.last_index_of("e2")
        self.assertEqual(actual, expected)

    def test_last_index_of__when_multiple_elements_present(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")
        slow_list.add("e1")
        slow_list.add("e4")

        expected = 3
        actual = slow_list.last_index_of("e1")
        self.assertEqual(actual, expected)

    def test_last_index_of__when_element_missing(self):
        slow_list = SlowList()
        slow_list.add("e1")

        expected = -1
        actual = slow_list.last_index_of("e2")
        self.assertEqual(actual, expected)

    def test_last_index_of__when_empty_list(self):
        slow_list = SlowList()

        expected = -1
        actual = slow_list.last_index_of("e1")
        self.assertEqual(actual, expected)

    def test_remove__when_empty_list(self):
        slow_list = SlowList()

        actual = slow_list.remove("e1")
        expected = False

        self.assertEqual(actual, expected)

    def test_remove__when_not_present(self):
        slow_list = SlowList()
        slow_list.add("e1")

        actual = slow_list.remove("e2")
        expected = False

        self.assertEqual(actual, expected)

    def test_remove__when_first_in_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual_rm = slow_list.remove("e1")
        expected_rm = True
        self.assertEqual(actual_rm, expected_rm)
        self.assertEqual(slow_list.size(), 2)

        actual_get = slow_list.get(0)
        expected_get = "'e2'"
        self.assertEqual(actual_get, expected_get)

    def test_remove__when_middle_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual_rm = slow_list.remove("e2")
        expected_rm = True
        self.assertEqual(actual_rm, expected_rm)
        self.assertEqual(slow_list.size(), 2)

        actual_get = slow_list.get(1)
        expected_get = "'e3'"
        self.assertEqual(actual_get, expected_get)

    def test_remove__when_last_in_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual_rm = slow_list.remove("e3")
        expected_rm = True
        self.assertEqual(actual_rm, expected_rm)
        self.assertEqual(slow_list.size(), 2)

    def test_remove_at__when_empty_list(self):
        slow_list = SlowList()

        with self.assertRaises(IndexError) as cm:
            slow_list.remove_at(0)

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_remove_at__when_index_too_high(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")

        with self.assertRaises(IndexError) as cm:
            slow_list.remove_at(2)

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_remove_at__when_only_one_element(self):
        slow_list = SlowList()
        slow_list.add("e1")

        actual = slow_list.remove_at(0)
        expected = "'e1'"
        self.assertEqual(actual, expected)
        self.assertTrue(slow_list.is_empty())

    def test_remove_at__when_first_element(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual = slow_list.remove_at(0)
        expected = "'e1'"
        self.assertEqual(actual, expected)
        self.assertEqual(slow_list.size(), 2)

        actual_get = slow_list.get(0)
        expected_get = "'e2'"
        self.assertEqual(actual_get, expected_get)

    def test_remove_at__when_middle_element(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual_remove = slow_list.remove_at(1)
        expected_remove = "'e2'"
        self.assertEqual(actual_remove, expected_remove)

        self.assertEqual(slow_list.size(), 2)

        actual_get = slow_list.get(1)
        expected_get = "'e3'"
        self.assertEqual(actual_get, expected_get)

    def test_remove_at__when_last_element(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        actual_remove = slow_list.remove_at(2)
        expected_remove = "'e3'"
        self.assertEqual(actual_remove, expected_remove)

        self.assertEqual(slow_list.size(), 2)

    def test_size__when_empty(self):
        slow_list = SlowList()
        expected = 0
        self.assertEqual(slow_list.size(), expected)

    def test_size__when_non_empty(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        expected = 2
        self.assertEqual(slow_list.size(), expected)

    def test_set__when_empty_list(self):
        slow_list = SlowList()

        with self.assertRaises(IndexError) as cm:
            slow_list.set(0, "e1")

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_set__when_index_too_high(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")

        with self.assertRaises(IndexError) as cm:
            slow_list.set(2, "e3")

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, IndexError)
        self.assertEqual(raised_exception.args, ('Index out of bounds',))

    def test_set__when_one_element_and_index_0(self):
        slow_list = SlowList()
        slow_list.add("e1")

        replaced_element = slow_list.set(0, "e2")
        expected_replaced = "'e1'"
        self.assertEqual(replaced_element, expected_replaced)

        actual_e2 = slow_list.get(0)
        expected_e2 = "'e2'"
        self.assertEqual(actual_e2, expected_e2)

    def test_set__when_start_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e3")
        slow_list.add("e4")

        replaced_element = slow_list.set(0, "e2")
        expected_replaced = "'e1'"
        self.assertEqual(replaced_element, expected_replaced)

        actual_e2 = slow_list.get(0)
        expected_e2 = "'e2'"
        self.assertEqual(actual_e2, expected_e2)

    def test_set__when_middle_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        replaced_element = slow_list.set(1, 99)
        expected_replaced = "'e2'"
        self.assertEqual(replaced_element, expected_replaced)

        actual_e2 = slow_list.get(1)
        expected_e2 = "99"
        self.assertEqual(actual_e2, expected_e2)

    def test_set__when_end_of_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add("e2")
        slow_list.add("e3")

        replaced_element = slow_list.set(2, 99)
        expected_replaced = "'e3'"
        self.assertEqual(replaced_element, expected_replaced)

        actual_e2 = slow_list.get(2)
        expected_e2 = "99"
        self.assertEqual(actual_e2, expected_e2)

    def test_to_string__when_empty_list(self):
        slow_list = SlowList()
        expected = ""
        self.assertEqual(slow_list.to_string(), expected)

    def test_to_string__when_non_empty_list(self):
        slow_list = SlowList()
        slow_list.add("e1")
        slow_list.add(10)
        expected = "['e1', 10]"
        self.assertEqual(slow_list.to_string(), expected)

    def test_type__when_unsupported_datatype(self):
        slow_list = SlowList()

        with self.assertRaises(TypeError) as cm:
            slow_list.add(["e1"])

        raised_exception = cm.exception
        self.assertEqual(raised_exception.__class__, TypeError)
        self.assertEqual(raised_exception.args, ('Datatype not supported',))


if __name__ == '__main__':
    unittest.main()
