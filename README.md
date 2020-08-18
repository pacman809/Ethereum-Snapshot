# Ethereum-SnapshotTakes a snapshot of all know positive balances and tokens on a given block. Also checks MongoDB for missing blocks prior to snapshot. Also used as a richlist.

Pre-Requisites

- MongoDB populated with block and transaction data
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

-run python findAddress.py


Garth Madden
Garthmadden809@gmail.com 
