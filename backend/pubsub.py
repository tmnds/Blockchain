from email import message
import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-189ab62e-80d1-4c44-b706-eb989c4e8f34'
pnconfig.subscribe_key = 'sub-c-8cb83d39-fa7e-4b97-aa46-432c9f373ec6'

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'/n-- Incoming channel: {message_object.channel} I Message {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """  
        self.pubnub.publish().channel(channel).message(message).sync()



def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})




if __name__ == '__main__':
    main()