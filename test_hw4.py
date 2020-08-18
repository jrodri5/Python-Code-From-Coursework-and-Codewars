'''
Created on Sep 30, 2017

@author: Justin Rodriguez

I pledge my honor that I have abided by the Stevens Honor System @jrodri5
'''
import unittest
import hw4

class Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(hw4.pascal_row(0),[1])
        self.assertEqual(hw4.pascal_row(1),[1,1])
        self.assertEqual(hw4.pascal_row(2),[1,2,1])
        self.assertEqual(hw4.pascal_row(4),[1,4,6,4,1])
        self.assertEqual(hw4.pascal_row(5),[1,5,10,10,5,1])
    
    def test02(self):
        self.assertEqual(hw4.pascal_triangle(0),[[1]])
        self.assertEqual(hw4.pascal_triangle(1),[[1],[1,1]])
        self.assertEqual(hw4.pascal_triangle(3),[[1],[1,1],[1,2,1],[1,3,3,1]])
        self.assertEqual(hw4.pascal_triangle(4),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        self.assertEqual(hw4.pascal_triangle(7),[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1]])


if __name__ == "__main__":
    unittest.main()        