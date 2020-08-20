# Ethereum-Snapshot Takes a snapshot of all known wallets with balances and tokens on a given block. Also checks MongoDB for missing blocks prior to snapshot. Also used as a richlist. Works for any Geth/ETH Based BlockChain.

Pre-Requisites

- MongoDB populated with block, token and transaction data
```ethereumetl``` works great for this
- Fully Indexed Collections (Blocks + Transactions)
- Geth node (Archived)
- Python 3
- pip installed for packages

INSTALL

check Requirements.txt
Enter commands

```pip install -r requirements.txt```

```pip freeze > requirements.txt```

edit config.py accordingly

-run python FindMissing.py (Optional) 
Finds missing blocks in Chain. Gather all missing blocks and add to DB before continuing.
Takes A long time depending on block height. approx 1 hr for 5M blocks

-run python snapIt.py


Garth Madden
TheNorthWatch.com
Garthmadden809@gmail.com 
 
 Use at own risk.
