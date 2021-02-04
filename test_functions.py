import unittest
from functions import *

#---------------------------------------------------------------calc
class TestCalcInputs(unittest.TestCase):
  def test_add_inputs(self): # test simple values
    self.assertEqual(calc(1,1,'+'), 2)
    self.assertEqual(calc(-1,1,'+'), 0)

  def test_sub_inputs(self): # test simple values
    self.assertEqual(calc(1,1,'-'), 0)
    self.assertEqual(calc(100,-100,'-'), 200)

  def test_mul_inputs(self): # test simple values
    self.assertEqual(calc(1,1,'*'), 1)
    self.assertEqual(calc(1.1,1,'*'), 1.1)

  def test_div_inputs(self): # test simple values
    self.assertEqual(calc(1,1,'/'), 1)
    self.assertEqual(calc(100,0,'/'), 0)

  def test_calc_inputType(self): # test non-numeric inputs
    self.assertRaises(TypeError, calc, True)

if(__name__ == '__main__'):
  unittest.main(verbosity=2)