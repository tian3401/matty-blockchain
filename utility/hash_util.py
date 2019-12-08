import hashlib as hl 
import json

__all__ = ['hash_string_256', 'hash_block']

def hash_string_256(string):
  return hl.sha256(string).hexdigest()


def hash_block(block):
  """ Hashes a block and returns a string representation of it"""

  # this will convert our block into a dictionary before we use json
  # .copy() is important to create a new dict every time we pass a block. Else it will override the previous blocks everytime we redefine the hashable block 
  hashable_block = block.__dict__.copy()
  hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
  print(hashable_block)

  # example of a hash: fdcd010164e24fe2247e9c6b20e211ab96c0cb7b3ad2da9f3e5feaac47ecc4d1
  # json.dumps take dictionaries and transforms to str 
  # .encode() to encode to UTF-8 that yields binary str that sha256 can use 
  # .hexdigest() needed to convert byte hash into a normal character hash 64 bit 
  # Because dictionaries are unordered maps we have to ensure the order by using sort
  return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())