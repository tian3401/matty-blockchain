"""Provides verification helper methods"""

# importing my own functions
from utility.hash_util import hash_string_256, hash_block

# This class is a helper class
class Verification: 
  # Can use static method because valid_proof does not get anything from the class
  @staticmethod
  def valid_proof(transactions, last_hash, proof):
    guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
    print(guess)
    # Hash the string
    # IMPORTANT: This is NOT the same hash as will be stored in the previous_hash. It's a not a block's hash. It's only used for the proof-of-work algorithm.
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    # Our requirement for a valid hash 
    return guess_hash[0:2] == '00'

  # Since verify_chain uses valid_proof method we should use class method
  @classmethod
  def verify_chain(cls, blockchain):
    """ Verify the current blockchain and return True if it's valid, otherwise return """
    for (index, block) in enumerate(blockchain): 
      if index == 0:
        continue
      if block.previous_hash != hash_block(blockchain[index - 1]): 
        return False
      # In the same class as valid_proof so we need self before it
      if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
        print('Proof of work is invalid')
        return False 
    return True 

  @staticmethod
  # Checking to see if senders balance is adequate to send the amount stated in transaction 
  def verify_transaction(transaction, get_balance): 
    sender_balance = get_balance()
    # Do not if else statement b/c already boolean value 
    return sender_balance >= transaction.amount

  @classmethod
  def verify_transactions(cls, open_transactions, get_balance):
    return all([cls.verify_transaction(tx, get_balance) for tx in open_transactions])