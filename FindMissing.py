#!/usr/bin/env python3


#FINDS MISSING BLOCKS IN DATABASE
#    Copyright (C) <2020>  <Garth Madden, Garthmadden809@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pymongo
from web3 import Web3
import config
import collections
from os import system

web3            	= config.geth()
blockHeight             = []
blockNumber     	= 0
missingBlocks   	= []
missingBlocksFinal      = []
jump                    = 0
mylist                  = 0
#BlockTestHeight 	= 250000 #UNHASH FOR TESTING
count 			= 0

for x in config.block.find().sort([('_id', -1)]).limit(1):
	BlockTestHeight = x["number"] #HASH FOR TESTING SETS BLOCK LIMIT

def clear():

        _ = system('clear')


def find_missing(blockHeight):
        return [x for x in range(blockHeight[0], blockHeight[-1]+1) if x not in blockHeight]

while blockNumber < BlockTestHeight:
	
	for x in config.block.find().skip(jump).limit(15000):
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
				if myCol.count_documents({"number": x}, limit=1) == 0:
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
	if myCol.count_documents({"number": x}, limit=1) == 0:
		missingBlocksFinal.append(x)

print()

if len(missingBlocksFinal) == 0:
        print("No Missing Blocks!")
else:
        print(f'MISSING BLOCKS! {missingBlocksFinal}')

print()
print("COMPLETE")

