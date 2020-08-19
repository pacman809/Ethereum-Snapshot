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
richlist		= []
masterList		= []

#y = config.SnapStart 

def checkForTokenActivity(address):

	if config.tokenTransfer.count_documents({ "to_address": address }, limit = 1) != 0:
		tokenActivity = True
	else:
		tokenActivity = False
	return tokenActivity	


def balanceInfo(personal_address, foundContracts):
    results = {}
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    account_checksum = Web3.toChecksumAddress(personal_address)

    for i in foundContracts:
        address = Web3.toChecksumAddress(i)
        user_clean = Web3.toChecksumAddress(personal_address)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(user_clean).call()
        balance = web3.fromWei(balance, config.perspective)

        if balance != 0:
            results.update( {symbol : balance} )


    return results


def tokenContractsAvailable():
	final = []

	for x in config.token.find():
			token = x["address"]
			if token not in final:
				final.append(token)
				print(f'"{x["address"]}" : "{x["symbol"]}",')			
	return final


def clear():

        _ = system('clear')

def main(config.SnapStart, toAddress, richlist, masterList):

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
						
						try:
							address = Web3.toChecksumAddress(x["to_address"])
							pass
						except:
							pass

						try:
							balance = Web3.fromWei(web3.eth.getBalance(address, config.SnapshotBlock), config.perspective)
							#balance = 1
							pass
						except:
							balance = 0
							pass
						
						try:
							if balance != 0 or checkForTokenActivity(address) == True:
								if config.suppress != True:
									clear()
									print(f'Address: {x["to_address"]} Block: {y}  Total Found: {len( toAddress )}')
								toAddress.append([x["to_address"]), balance])
						except:
							if config.suppress != True:
								print("ERROR")
						
						
						

					else:
						pass

		y = y +1

	counter = len(toAddress)
	percent = counter -1
	for wallets in toAddress:

		try:
			#address = Web3.toChecksumAddress( wallets )
			#balance = Web3.fromWei( web3.eth.getBalance( address, config.SnapshotBlock ), config.perspective )
			accountTokens = balanceInfo(wallets[0], tokenContracts)

			#if balance and accountTokens == 0:
			#	toAddress.remove(wallets)
			#	pass
			#else:
			masterList.extend([wallets, balance, accountTokens])
		except:
			pass
			#print("NFG ADDRESS")
		clear()
		percent = percent - 1
		print(percent / counter * 100)
		#clear()

	#masterList = sorted(masterList.items(), key=lambda x: x[1], reverse=True)
	print(len(toAddress))
	print(f'Address, {config.perspective}')				#HASH FOR RANK
	#print(f'Address, {config.perspective}, Rank') 			#UNHASH FOR RANK
	#print(masterList)
	for x in masterList:
		if x in masterList:
			print(x)					#HASH FOR RANK
			#print(f'{x}, {list(masterList).index(x)}')	#UNHASH FOR RANK
	#print(json.dumps(masterList))
	#print(masterList)
	#print(masterList["address"])
main(y, toAddress, richlist, masterList)
