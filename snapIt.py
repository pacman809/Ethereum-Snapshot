#!/usr/bin/env python3

#GARTH MADDEN 2019 Garthmadden809@gmail.com

#ITERATES THROUGH OUTPUT OF TRANSACTION TO GATHER BALANCES AND CREATE A SNAPSHOT/RICHLIST FOR THE GIVEN CONFIG BLOCK "CONFIG.PY OUTPUT TO CSV"
#python test.py > FILENAME.csv For Linux
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


import cProfile
import pstats
import pymongo
from web3 import Web3
import config
from os import system
import json
from datetime import datetime

startTime = datetime.now()
web3            = config.geth()
wallets = []

y = 1 

def balanceInfo(personal_address, foundContracts):

    results = {}
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')


    for i in foundContracts:
        address = Web3.toChecksumAddress(i)
        user_clean = Web3.toChecksumAddress(personal_address)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(user_clean).call()
        balance = web3.fromWei(balance, config.perspective)
        results.update( {symbol : balance} )



    return results

def main():
    toAddress = {}
    toAddress = set() 			

    for y in range(1, config.SnapshotBlock + 1):
        try:
        		SB = config.block.find_one( {"number": y} )

        		if SB["transaction_count"] != 0:		
        				TB = config.transaction.find_one({"block_number" : y })
        				toAddress.add(TB["to_address"])
        except:
        	print("Error")

    for x in toAddress:

        if x != '':

            tokenContracts = config.tokenContracts 	
            address = Web3.toChecksumAddress(x)
            balance = Web3.fromWei(web3.eth.getBalance(address, config.SnapshotBlock), config.perspective)
            accountTokens = balanceInfo(x, tokenContracts)
            wallets.extend([[address, balance, accountTokens]])
    print(f'ADDRESS, HALO, VET, DBET, VTHO, HXRO, HST, EVED, ZRX, PEG, OMG, USDC, BAT, BTC, FLASH, HETH, FCT, uDOO')
    for x in wallets:

    	print(f'{x[0]}, {x[1]}, {x[2]["VET"]}, {x[2]["DBET"]}, {x[2]["VTHO"]}, {x[2]["HXRO"]}, {x[2]["HST"]}, {x[2]["EVED"]}, {x[2]["ZRX"]}, {x[2]["PEG"]}, {x[2]["OMG"]}, {x[2]["USDC"]}, {x[2]["BAT"]}, {x[2]["BTC"]}, {x[2]["FLASH"]}, {x[2]["HETH"]}, {x[2]["FCT"]}, {x[2]["uDOO"]}')
    print(len(wallets))
main()

print(datetime.now() - startTime)

