import os
import random 

from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

pubsub = PubSub()
app = Flask(__name__) 
blockchain = Blockchain()

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)


@app.route('/')
def route_default():
    return 'Welcome to my page'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'
    
    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())

print(os.environ.get('PEER'))
app.run(port=PORT) 