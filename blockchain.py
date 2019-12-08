# 15th blockchain version adding classes to the blocks 
from functools import reduce
import hashlib as hl 

import json 
# Need to work on pickle
import pickle 

from utility.hash_util import hash_block
# importing Block class 
from block import Block
from transaction import Transaction
from utility.verification import Verification

MINING_REWARD = 10

print(__name__)

class Blockchain:
  def __init__(self, hosting_node_id):
    genesis_block = Block(0, '', [], 100, 0)
    # Initializing our empty blockchain list 
    self.__chain = [genesis_block]
    # Adding a list to track our transactions 
    self.__open_transactions = []
    # Runs load data as soon as the script is read 
    self.load_data()
    self.hosting_node = hosting_node_id
  

  # controls when other classes get private chain
  @property
  def chain(self):
    return self.__chain[:]
  
  # controls when other classes wants to set new value to chain
  @chain.setter
  def chain(self, val):
    self.__chain = val

  # Methods below is to access the private variable open_transaction
  def get_open_transactions(self):
    return self.__open_transactions[:]

# participants = {'Matthew Chen'}

  def load_data(self):
    try:
      with open('blockchain.txt', mode = 'r') as f:
        # returns a list of str
        file_content = f.readlines()

        # json.loads takes a json str and converts to python object 
        # we have the range function to get rid of the \n 
        blockchain = json.loads(file_content[0][:-1])
        updated_blockchain = []
        # Recreating the blockchain with OrderedDict transactions so they match how we stored them
        for block in blockchain: 
          converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
          updated_block = Block(block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
          
          updated_blockchain.append(updated_block)
        self.chain = updated_blockchain
        # Need to load open transactions first before updating it to Ordered Dict
        open_transactions = json.loads(file_content[1]) 
        updated_transactions = []
        #Updating the open_transactions before they are added to blockchain
        # Open transactions lose their OrderedDict notation with saving data
        for tx in open_transactions:
          updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
          updated_transactions.append(updated_transaction)
        self.__open_transactions = updated_transactions
    # This code runs when we get an IOError b/c blockchain.txt is not found. This will allow our blockchain to run even without an blockchain.txt
    except (IOError, IndexError): 
      # Use pass to make the program not do anything when we get these errors
      pass
    finally: 
      print('Cleanup')

  
  def save_data(self):
    try:
      with open('blockchain.txt', mode = 'w') as f: 
        # .copy() not needed b/c not manipulating dict 
        saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash,[tx.__dict__ for tx in block_el.transactions] ,block_el.proof, block_el.timestamp) for block_el in self.__chain]]
        f.write(json.dumps(saveable_chain))
        f.write('\n')
        # converted open_transactions back into a dictionary since we changed open_transactions to an object during load_data()
        saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
        #json dumps converts our list of transactions into a json str 
        f.write(json.dumps(saveable_tx))
    except IOError:
      print('Saving failed!')


  def proof_of_work(self):
    last_block = self.__chain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
      proof += 1 
    return proof 


  def get_balance(self):
    participant = self.hosting_node
    # Using a list comprehension to check tx's amount value in each block's transactions if the sender is the participant in every block in the blockchain 
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.__chain]
    # Need to check open tx to ensure we are getting full list of tx. This will restrict what tx can be sent once we check processed + open tx.
    open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    # Replacing for loop w/ lambda function to sum our senders tx amount
    # 1st arg = lambda function, 2nd arg = reference var, 3rd arg = initial amount
    # tx_sum is the last value & tx_amt is the current amount 
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender ,0)

    # previous code that we are replacing w/ lambda function 
    # amount_sent = 0
    # for tx in tx_sender:
    #   if len(tx) > 0:
    #     amount_sent += tx[0]
    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.__chain]

    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,tx_recipient,0)

    # previous code that we are replacing w/ lambda function
    # amount_received = 0
    # for tx in tx_recipient:
    #   if len(tx) > 0:
    #     amount_received += tx[0]

    return amount_received - amount_sent


  def get_last_block_value(self):
    """ Returns the value of the current blockchain. """
    if len(self.__chain) < 1:
      return None 
    # This is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
    return self.__chain[-1]


  def add_transaction(self, recipient, sender, amount = 1.0): 
    """ Append a new value as well as the last blockchain value to the blockchain """

    transaction = Transaction(sender, recipient, amount)
  
    # Passes the get_balance function to verifier 
    if Verification.verify_transaction(transaction, self.get_balance):
      # No longer appending directly to the blockchain, but instead appending to the open_transaction list 
      self.__open_transactions.append(transaction)
      self.save_data()
      return True
    return False 

 
  def mine_block(self):
    """Creates a new block and adds open transactions to it"""
    last_block = self.__chain[-1]
    hashed_block = hash_block(last_block)
    proof = self.proof_of_work()

    # reward_transaction = {
    #   'sender': 'MINING',
    #   'recipient': owner,
    #   'amount': MINING_REWARD
    # }
    reward_transaction = Transaction('MINING', self.hosting_node, MINING_REWARD)

    copied_transactions = self.__open_transactions[:]
    copied_transactions.append(reward_transaction)
    # uses default timestamp
    block = Block(len(self.__chain), hashed_block, copied_transactions, proof)
    self.__chain.append(block)
    
    # resetting the open transactions after every mining of block. Open transactions need to cleared because previous transactions have already been processed 
    self.__open_transactions = []
    #save_data needs a string not a list
    self.save_data()
    # used to clear out open transactions after every mined block
    return True 










