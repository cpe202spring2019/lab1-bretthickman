import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #Test cases for max_list
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3, 45, 7]), 45)
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([1]),[1])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        self.assertEqual(bin_search(100, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(-10, 0, len(list_val)-1, list_val), None)
        self.assertRaises(ValueError, bin_search, 10, 0, len(list_val)-1, None)

if __name__ == "__main__":
        unittest.main()

    
