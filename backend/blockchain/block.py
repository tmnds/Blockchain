import time

from backend.utils.crypto_hash import crypto_hash
from backend.utils.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}


class Block:
    '''
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    '''
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
    
    @staticmethod 
    def genesis():
        '''
        Generate genesis Block.
        '''
        # return Block(
            # GENESIS_DATA['timestamp'],
            # GENESIS_DATA['last_hash'],
            # GENESIS_DATA['hash'],
            # GENESIS_DATA['data']
        # )
        return Block(**GENESIS_DATA)

    @staticmethod
    def mine_block(last_block, data):
        '''
        Mine a block based on the given last_block and data, until a block hash 
        is found that meets the leading 0's proof of work requirement.
        ''' 
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, difficulty, nonce)
        # print(hash[0:difficulty])
        
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)
    
    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        '''
        Calculate the adjusted difficulty according to the MINE_RATE.
        Increase the difficulty for quickly mined blocks.
        Decrease the difficulty for slowly mined blocks.
        '''

        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        
        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        
        return 1

    @staticmethod
    def is_valid_block(last_block, block):
        '''
        Validate block by enforcing the following rules:
         - the block must have the proper last_hash reference
         - the block must meet the proof of work requirement
         - the difficulty must only adjust by 1 
         - the block hash must be a valid combination of the block fields
        '''

        if block.hash != last_block.hash:
            raise Exception('The Block last_hash must be correct')
        
        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of requirement was not met')



    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'Difficulty: {self.difficulty}, '
            f'Nonce: {self.nonce})'
        )


def main():
    
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo_data')
    print(block)

if __name__ == '__main__':
    main()
