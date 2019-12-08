from time import time 
from utility.printable import Printable

class Block(Printable):
  # constructor function for my block. First argument is "self", a ref to the object. Exactly the same as "this" in JS
  def __init__(self, index, previous_hash, transactions, proof, timestamp=0): 
    self.index = index
    self.previous_hash = previous_hash
    self.timestamp = time() if timestamp is None else timestamp
    self.transactions = transactions
    self.proof = proof
  
