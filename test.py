#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com

#ITERATES THROUGH OUTPUT OF TRANSACTION TO GATHER BALANCES AND CREATE A SNAPSHOT/RICHLIST FOR THE GIVEN CONFIG BLOCK "CONFIG.PY"
import cProfile
import pstats
import pymongo
from web3 import Web3
import config
from os import system
import json

web3            = config.geth()

toAddress 		= {}
toAddress = set()

y = 1 
profile = cProfile.Profile()


#def clear():
#
 #       _ = system('clear')

def main():
	y = 1
	toAddress = {}
	toAddress = set()

	#tokenContracts = config.tokenContracts 			

	while y <= config.SnapshotBlock:

		for x in config.block.find_one( {"number": y} ):

			if x[ "transaction_count" ] != 0:		
				for x in config.transaction.find_one({"block_number" : y }):
					toAddress.add(x["to_address"])
#					clear()
					print(len(toAddress))
					print(y)
		y = y +1

	
#main(y, toAddress)
profile.runcall(main)
ps = pstats.Stats(profile)
ps.print_stats()
