import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.wallet.transaction import Transaction

from backend.blockchain.block import Block

pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-189ab62e-80d1-4c44-b706-eb989c4e8f34'
pnconfig.subscribe_key = 'sub-c-8cb83d39-fa7e-4b97-aa46-432c9f373ec6'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}
class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                    self.blockchain
                )
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')
        
        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)
            print('\n -- Set the new transaction in the transaction pool')




class PubSub():
    """
    Handles the publish/subscribe layer of the applicatiosPn.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):
        """
        Publish the message objecpt to the channel.
        """  
        # self.pubnub.unsubscribe().channels(channel).execute()
        self.pubnub.publish().channel(channel).message(message).sync()
        # self.pubnub.subscribe().channels(channel).execute()

    
    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())
    
    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})

if __name__ == '__main__':
    main()