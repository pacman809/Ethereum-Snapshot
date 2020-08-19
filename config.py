#!/usr/bin/env python3
#Garth Madden 2019 Garthmadden809@gmail.com

import pymongo
from web3 import Web3

#---CONFIG GETH CONECTION
def geth():
	
	geth_url 	= "http://192.168.0.58:8545"  # INSERT YOUR GETH URL HERE
	#geth_url 	= "http://192.168.0.58:8645" 
	#geth_url	= "http://192.168.0.58:8585" 
	web3 = Web3(Web3.HTTPProvider(geth_url))
	return web3
#------------------	

#---CONFIG DATABASE
db              	= "halo-explorer-mainnet"									#Database Name
myclient        	= pymongo.MongoClient("mongodb://localhost:27017/") #Database Location
mydb            	= myclient[db]
block           	= mydb["blocks"]										#DB "Block" Collection Name
transaction 		= mydb["transactions"]										#DB "Transactions" Collection Name
token 		 		= mydb["tokens"]
tokenTransfer		= mydb["token_transfer"]								#DB 'token_transfer' Collection name
#------------------

#---CONFIG SNAPBLOCKS
SnapshotBlock		= 1000000									#Choose Snapshot Block Here
SnapStart		= 1
#SnapStart		= 33216666											#UNHASH FOR TESTING ONLY!!! CHOOSE START BLOCK HERE HASHED DEFAULTS TO 1
#------------------

#---CONFIG OTHER OPTIONS
perspective		= 'WEI'												#Choose What Value To Display eg.) Ether, Wei, Gwei etc
suppress		= False	
#------------------											#"Boolean" Suppress the output. For deferring output to Linux file eg. python findaddress.py > output.txt
#---CONFIG---------
tokenContracts = [
"0xd314d564c36c1b9fbbf6b440122f84da9a551029",
"0x59195ebd987bde65258547041e1baed5fbd18e8b",
"0xb8648f065205b9c31055653d668723f4b840e4c0" ,
"0x0343350a2b298370381cac03fe3c525c28600b21" ,
"0x280750ccb7554faec2079e8d8719515d6decdc84" ,
"0x32e31f27aaf3501a4f7139970477020baf9c8e1c" ,
"0xc8481effc60fa765ccf8286ba346233ed113b024" ,
"0x72649f2a739f2ed7454ca146fb9ba589747287f2" ,
"0x5f2786097350e9d0a0cbba233774631991dc5e40" ,
"0x978dc9ca2d75c9d187a9cb542c74c50c579a034a" ,
"0xdfd55110016251c7537d7645f35f92afcfc468ed" ,
"0xa6002d6df526683b528f87f95b4903f3c76cb7de" ,
"0x4734e87fbd52516ff729345bbf910557f630477c" 
]