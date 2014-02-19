#!/usr/bin/python -tt

import csv
import sys
from collections import OrderedDict, namedtuple
from optparse import OptionParser

def generateSharePriceDict(filepath):
	'''Generates a dictionary containing companys' highest share prices with time from input file.
	Args:
		filepath: Input CSV file
		
	Returns:
		sharePriceDict 
	'''
	sharePriceDict = OrderedDict()
	try:
		fileObj = open(filepath, 'r')
	except IOError as e:
		print e
		raise IOError
		sys.exit(1)
	else:
		with fileObj:
			fileReader = csv.reader(fileObj)
			if not fileReader:
				print '[Error] Input csv file is empty.'
				sys.exit(1)
				
			sharePriceToDurationTuple = namedtuple('sharePriceToDurationTuple', ['price', 'year', 'month'])
			companyNames = next(fileReader)[2:]
			
			# Initialization of sharedPriceDict
			for name in companyNames:
				sharePriceDict[name] = sharePriceToDurationTuple(0, 'year', 'month')
			
			# Filling values in the dictionary from input file
			# TODO(vishal.yadav): Input file contents need to be checked in detail for consistency.
			try: 	
				for row in fileReader:
					year, month = row[:2]
					for name, price in zip(companyNames, map(int, row[2:])):
						if sharePriceDict[name].price < price:
							sharePriceDict[name] = sharePriceToDurationTuple(price, year, month)
			except ValueError as e:
				print 'Content of input file is not consistent.'
				raise ValueError
				sys.exit(1) 
					
	return sharePriceDict
	
def showMaxSharePriceHistory(filepath):
	'''Displays the companys'maximum share price along with time 
	Args:
		filepath: Input CSV file
	'''
	maxSharePriceToDurationDict = generateSharePriceDict(filepath)
	msgList = []
	if len(maxSharePriceToDurationDict.keys()) > 0:
		for companyName in maxSharePriceToDurationDict.keys():
			unused_price, year, month = maxSharePriceToDurationDict[companyName]
			msgList.append('Share Price of %s was maximum in month %s of year %s' %(companyName, month, year))
		return '\n'.join(msgList)

def main():
	usage = "usage: %prog [options] filepath"
	parser = OptionParser(usage=usage)
	parser.add_option("-f", "--filepath", dest="filepath", help="Absolute path of Input file")
	(options, unused_args) = parser.parse_args()
	inputFile = options.filepath
	
	if not inputFile:
		parser.error('No input file passed as argument.')
		
	outputMsg = showMaxSharePriceHistory(inputFile)
	print outputMsg
	
if __name__ == '__main__':
	main()
