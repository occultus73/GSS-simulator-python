import unittest

from simulation.FertileSimulator import FertileSimulator
from data.American import American


class TestFertileSimulator(unittest.TestCase):
    def test_growth(self):
        eve = list([American(0, 0, 100, 1, 2, 2, 21, 7.0)])
        garden_of_eden = FertileSimulator(0, eve)
        # Eve is born
        for year in range(18):
            print("year:", year)
            self.assertEqual(0, len(garden_of_eden.next_year()))
        # Eve turns 18
        for year in range(18, 21):
            print("year:", year)
            self.assertEqual(1, len(garden_of_eden.next_year()))
        # Eve has first child
        for year in range(21, 23):
            print("year:", year)
            self.assertEqual(1, len(garden_of_eden.next_year()))
        # Eve has second child
        for year in range(21 + 2, 21 + 18):
            print("year:", year)
            self.assertEqual(1, len(garden_of_eden.next_year()))
        # Eve's first child turns 18.
        for year in range(21 + 18, 21 + 18 + 2):
            print("year:", year)
            self.assertEqual(2, len(garden_of_eden.next_year()))
        # Eve's second child turns 18.
        for year in range(21 + 18 + 2, 21 + 21):
            print("year:", year)
            self.assertEqual(3, len(garden_of_eden.next_year()))
        # Eve's first child has first child.
        for year in range(21 + 21, 21 + 21 + 2):
            print("year:", year)
            self.assertEqual(3, len(garden_of_eden.next_year()))
        # Eve's first child has second child, and second child has first child.
        for year in range(21 + 21 + 2, 21 + 21 + 18):
            print("year:", year)
            self.assertEqual(3, len(garden_of_eden.next_year()))
        # Eve's first child's first child turns 18
        for year in range(21 + 21 + 18, 21 + 21 + 18 + 2):
            print("year:", year)
            self.assertEqual(4, len(garden_of_eden.next_year()))
        # Eve's first child's second child, and eve's second child's first child, both turn 18.
        for year in range(21 + 21 + 18 + 2, 21 + 21 + 21):
            print("year:", year)
            self.assertEqual(6, len(garden_of_eden.next_year()))
        # Eve's first child's first child has first child.
        for year in range(21 + 21 + 21, 21 + 2 + 21 + 2 + 18):
            print("year:", year)
            self.assertEqual(6, len(garden_of_eden.next_year()))
        # Eve's second child's second child turns 18.
        for year in range(21 + 2 + 21 + 2 + 18, 67):
            print("year:", year)
            self.assertEqual(7, len(garden_of_eden.next_year()))
        # Eve retires.
        for year in range(67, 79):
            print("year:", year)
            self.assertEqual(6, len(garden_of_eden.next_year()))
        # Eve dies.
        for year in range(79, 21 + 21 + 21 + 18):
            print("year:", year)
            self.assertEqual(6, len(garden_of_eden.next_year()))
        # Eve's first child's first child's first child turns 18.
        for year in range(21 + 21 + 21 + 18, 21 + 21 + 21 + 18 + 2):
            print("year:", year)
            self.assertEqual(7, len(garden_of_eden.next_year()))


if __name__ == '__main__':
    unittest.main()
