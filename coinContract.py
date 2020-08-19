import pymongo
import config



def tokenContractsAvailable():
	final = []

	for x in config.token.find():
			token = x["address"]
			if token not in final:
				final.append(token)
				print(f'"{x["address"]}" : "{x["symbol"]}",')			
	#print(len(final))
	#print(final)
	return final

tokenContractsAvailable()