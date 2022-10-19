from ctypes import addressof


import uuid 


class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of the miner's balance.
    Allows a miner to authorize transactions.
    """

    def __init__(self):
        self.address = str(uuid.uuid4())[0:8]
