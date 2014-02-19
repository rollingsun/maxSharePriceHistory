#!/usr/bin/python -tt

import unittest
import maxSharePriceHistoryCalculator as calculator

class MaxSharePriceHistoryCalculatorTest(unittest.TestCase):
	def testInputFileDoesNotExist(self):
		self.assertRaises(IOError, calculator.generateSharePriceDict, 'dummyFileDoesNotExist')
		
	def testInputFileEmptyOrInconsistentContent(self):
		self.assertRaises(ValueError, calculator.generateSharePriceDict, 'emptyfile.txt')
		
	def testCorrectOutput(self):
		msg = "Share Price of Company A was maximum in month  Oct of year 2002\nShare Price of  Company B was maximum in month  Mar of year 2006\nShare Price of Company C was maximum in month  Oct of year 2002"
		self.assertEqual(calculator.showMaxSharePriceHistory('companySharePriceHistory.txt'), msg)


if __name__ == '__main__':
	unittest.main()
