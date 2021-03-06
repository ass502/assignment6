"""unittest for functions in merge module"""

from merge import *
from unittest import TestCase

class MergeIntervalsTest(TestCase):

	def test_merge_adjacent_intervals(self):
		int1=interval("[-1,5)")
		int2=interval("[5,8]")
		int3=interval("[-1,8]")
		self.assertEqual(mergeIntervals(int1,int2),int3)

	def test_merge_overlapping_intervals(self):
		int1=interval("[-1,5)")
		int2=interval("[3,9]")
		int3=interval("[-1,9]")
		self.assertEqual(mergeIntervals(int1,int2),int3)
		
		int4=interval("(1,3]")
		int5=interval("[1,3)")
		int6=interval("[1,3]")
		self.assertEqual(mergeIntervals(int4,int5),int6)
		
	def test_merge_nonoverlapping_intervals(self):
		int1=interval("[-1,5)")
		int2=interval("[6,9]")
		self.assertRaises(MergeException,mergeIntervals,int1,int2)
		
class MergeOverlappingIntervalsTest(TestCase):
	
	def test_mergeoverlapping(self):
		int1=interval("[-5,-3]")
		int2=interval("[-2,1)")
		int3=interval("[3,7]")
		int4=interval("(5,9]")
		int5=interval("[13,15]")
		
		merge1=interval("[-5,0]")
		merge2=interval("[3,9]")
		
		self.assertEqual(mergeOverlappingIntervals([int1,int2,int3,int4,int5]),[merge1,merge2,int5])
		
class InsertTest(TestCase):

	def test_valid_insert(self):
		int1=interval("[-7,-4)")
		int2=interval("[0,5)")
		int3=interval("[8,10]")
		newint=interval("[-4,-1]")
		
		inserted=interval("[-7,4]")
		
		self.assertEqual(insert([int1,int2,int3],newint),[inserted,int3])
		
	def test_overlapping_insert(self):
		int1=interval("[-7,-4)")
		int2=interval("[0,5)")
		int3=interval("[5,10]")
		newint=interval("[-4,-1]")
		
		self.assertRaises(OverlapException,insert,[int1,int2,int3],newint)
