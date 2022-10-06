import unittest

from Unit_testing_lab.list.integerList import IntegerList


class IntegerListTest(unittest.TestCase):

    def setUp(self):
        self.integerList = IntegerList(1, 2, 3)

    def test_init(self):
        self.customizedIntegerList = IntegerList(1, 'x', 2)

        self.assertEqual(len(self.customizedIntegerList.get_data()), 2)
        self.assertEqual(self.customizedIntegerList.get(0), 1)
        self.assertTrue(isinstance(self.customizedIntegerList.get(0), int))
        self.assertEqual(self.customizedIntegerList.get(1), 2)
        self.assertTrue(isinstance(self.customizedIntegerList.get(1), int))

    def test_get_data_returns_success(self):
        expected_result = [1, 2, 3]
        actual_result = self.integerList.get_data()
        self.assertEqual(expected_result, actual_result)

    def test_add_method_adds_element_and_returns_list(self):
        element = 5
        expected_result = [1, 2, 3, 5]
        actual_result = self.integerList.add(element)
        self.assertEqual(actual_result, expected_result)

    def test_add_method_throws_error_when_input_not_integer(self):
        element = 'x'
        with self.assertRaises(ValueError) as ex:
            self.integerList.add(element)
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_remove_index_deletes_successfully_element_at_given_index_and_returns_it(self):
        index = len(self.integerList.get_data()) - 1
        removed_element = self.integerList.remove_index(index)
        self.assertEqual(removed_element, 3)
        self.assertTrue(self.integerList.get_data(), [1, 2])

    def test_remove_index_method_throws_out_of_range_error(self):
        index = len(self.integerList.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integerList.remove_index(index)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_method_throws_out_of_range_error(self):
        index = len(self.integerList.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integerList.get(index)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_method_returns_element_at_given_index(self):
        index = len(self.integerList.get_data()) - 1
        returned_element = self.integerList.get(index)
        self.assertEqual(returned_element, 3)

    def test_insert_method_throws_out_of_range_error(self):
        index = len(self.integerList.get_data())
        element = 100
        with self.assertRaises(IndexError) as ex:
            self.integerList.insert(index, element)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_method_throws_value_error(self):
        index = 1
        element = "xyz"
        with self.assertRaises(ValueError) as ex:
            self.integerList.insert(index, element)
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_insert_successfully_adds_element_at_given_index(self):
        index = 1
        element = 100
        self.integerList.insert(index, element)
        self.assertEqual(self.integerList.get_data(), [1, 100, 2, 3])

    def test_get_biggest_successfully_returns_biggest_element(self):
        expected_result = 3
        actual_result = self.integerList.get_biggest()
        self.assertEqual(actual_result, expected_result)

    def test_get_index_returns_index_of_given_element(self):
        element = 2
        returned_index = self.integerList.get_index(element)
        self.assertEqual(returned_index, 1)

    if __name__ == '__main__':
        unittest.main()
