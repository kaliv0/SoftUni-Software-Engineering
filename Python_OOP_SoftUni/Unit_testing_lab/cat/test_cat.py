import unittest

from Unit_testing_lab.cat.cat import Cat


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Mike")

    def test_init(self):
        self.assertEqual(self.cat.name, "Mike")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_fed_equals_true_when_eat_method_is_called(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_sleepy_equals_true_when_eat_method_is_called(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_size_increases_when_eat_method_is_called(self):
        expected_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(self.cat.size, expected_size)

    def test_eat_method_raises_error_when_cat_is_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_sleep_method_raises_error_when_cat_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_sleepy_equals_false_when_sleep_method_is_called(self):
        self.cat.eat()  # throws error when hungry
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
