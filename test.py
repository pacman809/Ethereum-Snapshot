#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com

#ITERATES THROUGH OUTPUT OF TRANSACTION TO GATHER BALANCES AND CREATE A SNAPSHOT/RICHLIST FOR THE GIVEN CONFIG BLOCK "CONFIG.PY"

import pymongo
from web3 import Web3
import config
from os import system
import json

web3            = config.geth()

toAddress 		= []

y = config.SnapStart 



def clear():

        _ = system('clear')

def main(y, toAddress):

	tokenContracts = config.tokenContracts 			#HASH FOR AUTO
	#print("Gathering unique Token Contracts") 		#UNHASH FOR AUTO TOKEN FIND
	#tokenContracts = tokenContractsAvailable()
	#input("Program Will Gather Balances For All Above Contracts")

	while config.SnapStart <= config.SnapshotBlock:

		for x in config.block.find( {"number": y} ):

			if x[ "transaction_count" ] != 0:
				goodNum = x[ "number" ]

		
				for x in config.transaction.find({"block_number" : goodNum }):

					if x["to_address"] not in toAddress:
								toAddress.append(x["to_address"])
                print(x["to_address"])

		y = y +1

	
main(y, toAddress, richlist, masterList)
