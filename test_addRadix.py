import unittest
from addRadix import add
from addRadix import addList


class Test(unittest.TestCase):

	def test_add(self):
		a = '110'
		b = '110'
		res = add(a, b, 2)
		self.assertEqual('1100', res)

	def test_add_1(self):
		a = '999'
		b = '1'
		res = add(a, b, 10)
		self.assertEqual('1000', res)

	def test_add_1(self):
		a = '999'
		b = '1'
		res = add(a, b, 10)
		self.assertEqual('1000', res)

	def test_add_2(self):
		a = '7'
		b = '2'
		res = add(a, b, 8)
		self.assertEqual('11', res)

	def test_add_list(self):
		res = addList(['1', '1', '110'],  2)
		self.assertEqual('1000',res)

unittest.main()