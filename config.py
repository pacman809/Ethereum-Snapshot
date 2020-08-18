#!/usr/bin/env python3
#Garth Madden 2019 Garthmadden809@gmail.com

import pymongo
from web3 import Web3

def geth():
	#geth_url = "http://192.168.0.58:8545" #HALO # INSERT YOUR GETH URL HERE
	geth_url = "http://192.168.0.58:8645" #EGEM
	web3 = Web3(Web3.HTTPProvider(geth_url))
	return web3
	

#---CONFIG
db              = "egem-explorer-mainnet"							#Database Name
myclient        = pymongo.MongoClient("mongodb://localhost:27017/") #Database Location
mydb            = myclient[db]
block           = mydb["blocks"]									#DB "Block" Collection Name
transaction 	= mydb["transactions"]								#DB "Transactions" Collection Name
SnapshotBlock	= 5900000
perspective		= 'ETHER'											#Choose What Value To Display eg.) Ether, Wei, Gwei etc
suppress		= True												#"Boolean" Suppress the output. For deferring output to Linux file eg. python findaddress.py > output.txt