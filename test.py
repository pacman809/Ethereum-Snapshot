#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com

#ITERATES THROUGH OUTPUT OF TRANSACTION TO GATHER BALANCES AND CREATE A SNAPSHOT/RICHLIST FOR THE GIVEN CONFIG BLOCK "CONFIG.PY"
import cProfile
import pymongo
from web3 import Web3
import config
from os import system
import json

web3            = config.geth()

toAddress 		= []

y = config.SnapStart 
profile = cProfile.Profile()


def clear():

        _ = system('clear')

def main(y, toAddress):

	tokenContracts = config.tokenContracts 			

	while config.SnapStart <= config.SnapshotBlock:

		for x in config.block.find( {"number": y} ):

			if x[ "transaction_count" ] != 0:		
				x =  config.transaction.find({"block_number" : y }):
					if x["to_address"] not in toAddress:
						toAddress.append(x["to_address"])
						clear()
						print(len(toAddress))
						print(y)
		y = y +1

	
main(y, toAddress)
profile.runcall(main)
