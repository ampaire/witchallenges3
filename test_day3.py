import unittest
from challenges import challenge1


class DayThreeTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_sorted_list_works(self):
        response = challenge1.sorted_list([2, 0, 6, 5, 1, 7, 'z', 'a'])
        self.assertEqual(len(response),3)

    

if '__name__' == '__main__':
    unittest.main()