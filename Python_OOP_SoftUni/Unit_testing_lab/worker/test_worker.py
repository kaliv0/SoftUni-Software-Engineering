import unittest

from Unit_testing_lab.worker.worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Mincho", 1_000, 50)

    def test_init(self):
        self.assertEqual(self.worker.name, "Mincho")
        self.assertEqual(self.worker.salary, 1_000)
        self.assertEqual(self.worker.energy, 50)
        self.assertEqual(self.worker.money, 0)

    def test_energy_increases_when_rest_method_is_called(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_error_is_raised_when_energy_is_less_or_equal_to_zero(self):
        for e in (-1, 0):
            with self.subTest(e=e):
                self.worker.energy = e
                with self.assertRaises(Exception) as ex:
                    self.worker.work()
                self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_salary_increases_when_work_method_is_called(self):
        expected_amount = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(self.worker.money, expected_amount)

    def test_energy_decreases_when_work_method_is_called(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info_returns_proper_values(self):
        expected_info = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(self.worker.get_info(), expected_info)


if __name__ == '__main__':
    unittest.main()
