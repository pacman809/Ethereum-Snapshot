#!/usr/bin/env python3
#Garth Madden 2019 Garthmadden809@gmail.com

import pymongo
from web3 import Web3

def geth():

<<<<<<< HEAD
	geth_url = "http://192.168.0.58:8545" #HALO # INSERT YOUR GETH URL HERE
	#geth_url = "http://192.168.0.58:8645" #EGEM
	#geth_url	= "http://192.168.0.58:8585" #ETHER1
=======
	geth_url 	= "http://192.168.0.58:8545"  # INSERT YOUR GETH URL HERE
	#geth_url 	= "http://192.168.0.58:8645" 
	#geth_url	= "http://192.168.0.58:8585" 
>>>>>>> 8277b1065b61135f2f7de82759e37276ffde3b42
	web3 = Web3(Web3.HTTPProvider(geth_url))
	return web3
	

<<<<<<< HEAD
#---CONFIG
db              = "egem-explorer-mainnet"							#Database Name
myclient        = pymongo.MongoClient("mongodb://localhost:27017/") #Database Location
mydb            = myclient[db]
block           = mydb["blocks"]									#DB "Block" Collection Name
transaction 	= mydb["transactions"]								#DB "Transactions" Collection Name

SnapshotBlock	= 5901553											#Choose Snapshot Block Here
=======
db              	= "****-explorer-mainnet"									#Database Name
myclient        	= pymongo.MongoClient("mongodb://localhost:27017/") #Database Location
mydb            	= myclient[db]
block           	= mydb["blocks"]										#DB "Block" Collection Name
transaction 		= mydb["transactions"]										#DB "Transactions" Collection Name
SnapshotBlock		= 5901553											#Choose Snapshot Block Here
>>>>>>> 8277b1065b61135f2f7de82759e37276ffde3b42
SnapStart		= 1
#SnapStart		= 5250008											#UNHASH FOR TESTING ONLY!!! CHOOSE START BLOCK HERE HASHED DEFAULTS TO 1
perspective		= 'ETHER'											#Choose What Value To Display eg.) Ether, Wei, Gwei etc
suppress		= True												#"Boolean" Suppress the output. For deferring output to Linux file eg. python findaddress.py > output.txt
