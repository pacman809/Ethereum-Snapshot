#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com

#ITERATES THROUGH OUTPUT OF TRANSACTION TO GATHER BALANCES AND CREATE A SNAPSHOT/RICHLIST FOR THE GIVEN CONFIG BLOCK "CONFIG.PY"

import pymongo
from web3 import Web3
import config
from os import system

web3            = config.geth()

toAddress 		= []
richlist		= []
masterList		= {}

y = 1 


def clear():

        _ = system('clear')

while y <= config.SnapshotBlock:

	for x in config.block.find( {"number": y} ):

		if x[ "transaction_count" ] != 0:
			goodNum = x[ "number" ]

	
			for x in config.transaction.find({"block_number" : goodNum }):

				if x["to_address"] not in toAddress:
					
					try:
						#address = Web3.toChecksumAddress(x["to_address"])
						pass
					except:
						pass

					try:
						#balance = Web3.fromWei(web3.eth.getBalance(address),'Ether')
						balance = 1
						pass
					except:
						balance = 0
						pass
					
					try:
						if balance != 0:
							clear()
							print(f'Address: {x["to_address"]} Block: {y}  Total Found: {len( toAddress )}')
							#print(balance)
							toAddress.append(x["to_address"])
					except:
						print("ERROR")
					
					
					

				else:
					pass

	y = y +1

print("TO ADDRESS'")		
print(len(toAddress))

for wallets in toAddress:

	try:
		address = Web3.toChecksumAddress( wallets )
		balance = Web3.fromWei( web3.eth.getBalance( address, config.SnapshotBlock ), config.perspective )

		if balance == 0:
			pass
		else:
			masterList[ address ] = balance
	except:
		#print("NFG ADDRESS")

masterList = sorted(masterList.items(), key=lambda x: x[1], reverse=True)
#print(masterList)
for x in masterList:
	print(x)