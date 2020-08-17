#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com
#FINDS MISSING BLOCKS IN DATABASE

import pymongo
from web3 import Web3
import config
import collections
from os import system

#---CONFIG
db              = "halo-explorer-mainnet"	#Database Name
myclient        = pymongo.MongoClient("mongodb://localhost:27017/")
mydb            = myclient[db]
web3            = search.connect_geth()
myCol           = mydb["blocks"]
blockHeight             = []
blockNumber     = 0
missingBlocks   = []
missingBlocksFinal      = []
jump                    = 0
mylist                  = 0
#BlockTestHeight = 250000
count 			= 0

for x in myCol.find().sort([('_id', -1)]).limit(1):
	BlockTestHeight = x["number"]

def clear():

        _ = system('clear')


def find_missing(blockHeight):
        return [x for x in range(blockHeight[0], blockHeight[-1]+1) if x not in blockHeight]

while blockNumber < BlockTestHeight:
	
	for x in myCol.find().skip(jump).limit(15000):
		blockHeight.append(x["number"])
		count = count + 1
	
	clear()
	mylist = '{:.2f}%'.format(blockNumber / BlockTestHeight * 100)
	print (f'Gathering {mylist} Complete  {blockNumber} of {BlockTestHeight}')
	print(f'Possible Missing Blocks {len(missingBlocks)}')
	print(f'Confirmed Missing Blocks {len(missingBlocksFinal)}')
	print(f'Total Blocks Accounted For {count}')
	maybemissed = find_missing(blockHeight)

	if maybemissed != 0:
		missingBlocks.extend(maybemissed)

		if len(missingBlocks) > 1000:
			print("Flagged Blocks Exceed 1K, Checking Manually To Clear Cache")

			for x in missingBlocks:
				if myCol.count_documents({ "number": x }, limit = 1) != 0:
					pass
				else:
					missingBlocksFinal.append(x)
					print("NOT FOUND")

				missingBlocks = []

	#missingBlocks = []
	blockHeight = []
	blockNumber = blockNumber + 15000
	jump = jump + 15000

print()
print("Testing for Flagged Blocks")

for x in missingBlocks:
        if myCol.count_documents({ "number": x }, limit = 1) != 0:
                pass
        else:
                missingBlocksFinal.append(x)

print()

if len(missingBlocksFinal) == 0:
        print("No Missing Blocks!")
else:
        print(f'MISSING BLOCKS! {missingBlocksFinal}')

print()
print("COMPLETE")

