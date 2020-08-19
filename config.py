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
SnapshotBlock		= 37137900									#Choose Snapshot Block Here
SnapStart		= 1
#SnapStart		= 33216666											#UNHASH FOR TESTING ONLY!!! CHOOSE START BLOCK HERE HASHED DEFAULTS TO 1
#------------------

#---CONFIG OTHER OPTIONS
perspective		= 'WEI'												#Choose What Value To Display eg.) Ether, Wei, Gwei etc
suppress		= False	
#------------------											#"Boolean" Suppress the output. For deferring output to Linux file eg. python findaddress.py > output.txt
#---CONFIG---------
tokenContracts = [	
"0x280750ccb7554faec2079e8d8719515d6decdc84",	#	VET
"0x59195ebd987bde65258547041e1baed5fbd18e8b",	#	DBET
"0x0343350a2b298370381cac03fe3c525c28600b21",	#	VTHO
"0xdfd55110016251c7537d7645f35f92afcfc468ed",	#	HXRO
"0x14d01e64f0573925e28d69dc3846b2f0986ab8b8",	#	HST
"0x5f2786097350e9d0a0cbba233774631991dc5e40",	#	EVED
"0xb70b02222c53abf4e9ccac8fb701425db2ec4de1",	#	ZRX
"0x4734e87fbd52516ff729345bbf910557f630477c",	#	PEG
"0x0792fe820e7f65da788ac002ce88c74816b59142",	#	OMG
"0xdc14c317abf4fca7ac2255f0da73b39f63598c76",	#	USDC
"0xc8481effc60fa765ccf8286ba346233ed113b024",	#	BAT
"0xb8648f065205b9c31055653d668723f4b840e4c0",	#	BTC
"0x200941b46e8cbb645fe85cdd526e48826acfd8fa",	#	FLASH
"0xd314d564c36c1b9fbbf6b440122f84da9a551029",	#	ETH
"0xa6002d6df526683b528f87f95b4903f3c76cb7de",	#	FCT
"0x092fb07d2171b3bc7a9581d7349c57bc0332a87f",	#	USDCO
"0x72649f2a739f2ed7454ca146fb9ba589747287f2"	#	UDOO
]