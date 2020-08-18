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

y = config.SnapStart 


def clear():

        _ = system('clear')

while y <= config.SnapshotBlock:

	for x in config.block.find( {"number": y} ):

		if x[ "transaction_count" ] != 0:
			goodNum = x[ "number" ]

	
			for x in config.transaction.find({"block_number" : goodNum }):

				if x["to_address"] not in toAddress:
					
					try:
						address = Web3.toChecksumAddress(x["to_address"])
						pass
					except:
						pass

					try:
						balance = Web3.fromWei(web3.eth.getBalance(address), config.perspective)
						#balance = 1
						pass
					except:
						balance = 0
						pass
					
					try:
						if balance != 0:
							if config.suppress != True:
								clear()
								print(f'Address: {x["to_address"]} Block: {y}  Total Found: {len( toAddress )}')
							#print(balance)
							toAddress.append(x["to_address"])
					except:
						if config.suppress != True:
							print("ERROR")
					
					
					

				else:
					pass

	y = y +1


for wallets in toAddress:

	try:
		address = Web3.toChecksumAddress( wallets )
		balance = Web3.fromWei( web3.eth.getBalance( address, config.SnapshotBlock ), config.perspective )

		if balance == 0:
			toAddress.remove(wallets)
			pass
		else:
			masterList[address] = balance
	except:
		pass
		#print("NFG ADDRESS")


masterList = sorted(masterList.items(), key=lambda x: x[1], reverse=True)
print(len(toAddress))
print(f'Address, {config.perspective}')				#HASH FOR RANK
#print(f'Address, {config.perspective}, Rank') 			#UNHASH FOR RANK
for x in masterList:
	if x in masterList:
		print(x)					#HASH FOR RANK
		#print(f'{x}, {list(masterList).index(x)}')	#UNHASH FOR RANK
		
