"""unittest for interval class and user-defined exceptions in the interval module"""

from interval import *
from unittest import TestCase

class IntervalTest(TestCase):
	
	def test_valid_interval_init(self):
		int1=interval("(-2,5]")
		self.assertFalse(int1.lowerInclusive)
		self.assertTrue(int1.upperInclusive)
		self.assertEqual(int1.lowerInteger,-2)
		self.assertEqual(int1.upperInteger,5)

	def test_invalid_format_init(self):
		self.assertRaises(ValueError,interval,"foo")
		self.assertRaises(ValueError,interval,"[123]")
		self.assertRaises(ValueError,interval,"[12,]")
		self.assertRaises(ValueError,interval,"[12")
		self.assertRaises(ValueError,interval,"12]")
		
	def test_invalid_interval_init(self):
		self.assertRaises(IntervalException,interval,"(1,1]")
		self.assertRaises(IntervalException,interval,"(2,2)")
		self.assertRaises(IntervalException,interval,"[2,-2]")

