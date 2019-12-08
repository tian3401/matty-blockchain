# First blockchain model 

# blockchain = [[1]]

# def add_value():
#   blockchain.append([blockchain[-1], 5.3])
#   print(blockchain)

# add_value()
# add_value()


# Second blockchain model 

# blockchain = [[1]]

# def add_value(value): 
#   blockchain.append([blockchain[-1], value])
#   print(blockchain)

# add_value(10.92)
# add_value(92.10)


# Third blochain model with some cleanup 

# blockchain = [[1]]

# def get_last_block_value():
#   return blockchain[-1]


# def add_value(value): 
#   blockchain.append([get_last_block_value(), value])
#   print(blockchain)

# add_value(10.92)
# add_value(92.10)

# Fourth with default values upgrade 

# blockchain = []

# def get_last_block_value():
#   return blockchain[-1]


# def add_value(tx_value, last_tx_value = [1]): 
#   blockchain.append([last_tx_value, tx_value])
  

# add_value(10.92)
# add_value(92.10, get_last_block_value())
# add_value(last_tx_value = get_last_block_value(), tx_value = 100) # we switched around the order of the arguments

# print(blockchain)


# Fifth blockchain model with input 

# blockchain = []

# def get_last_block_value():
#   return blockchain[-1]


# def add_value(tx_value, last_tx_value = [1]): 
#   blockchain.append([last_tx_value, tx_value])
  
# input_value = float(input('please input your transaction value: '))
# add_value(input_value)

# input_value = float(input('please input your transaction value: '))
# add_value(input_value, get_last_block_value())

# input_value = float(input('please input your transaction value: '))
# add_value(last_tx_value = get_last_block_value(), tx_value = input_value) # we switched around the order of the arguments

# print(blockchain)


# Sixth blockchain model - leaner model 

# blockchain = []

# def get_last_block_value():
#   return blockchain[-1]


# def add_value(tx_value, last_tx_value = [1]): 
#   blockchain.append([last_tx_value, tx_value])


# def get_user_input(): 
#   return float(input('please input your transaction value: '))

  
# input_value = get_user_input()
# add_value(input_value)

# input_value = get_user_input()
# add_value(input_value, get_last_block_value())

# input_value = get_user_input()
# add_value(last_tx_value = get_last_block_value(), tx_value = input_value) # we switched around the order of the arguments

# print(blockchain)


# Seventh blockchain model with loops and conditionals 

# blockchain = []

# def get_last_block_value():
#   return blockchain[-1]


# def add_value(tx_value, last_tx_value = [1]): 
#   blockchain.append([last_tx_value, tx_value])


# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   user_input = float(input('please input your transaction value: '))
#   return user_input


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
  
# tx_value = get_transaction_value()
# add_value(tx_value)

# while True:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Output the blockchain blocks')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_amount = get_transaction_value()
#     add_value(tx_amount, get_last_block_value())
#   else:
#     print_blockchain_elements()

#   print('Done!')

# Eight blockchain w/ Adding elif statements & break & Validating our blockchain 

# blockchain = []

# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # this is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# # This function accepts two arguments.
# # One required one (transaction_amount) and one optional one (last_transaction)
# # The optional one is optional because it has a default value => [1]

# def add_transaction(tx_value, last_tx_value = [1]): 
#   """ Append a new value as well as the last blockchain value to the blockchain

#   # Arguments: 
#   #   : tx_amount: The amount that should be added. 
#   #   : last_tx_value: The last blockchain transaction (default [1]).
#   """
#   if last_tx_value == None:
#     last_tx_value = [1]
#   blockchain.append([last_tx_value, tx_value])


# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   user_input = float(input('please input your transaction value: '))
#   return user_input


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)


# def manipulate_blockchain(): 
#   blockchain[0] = [2]

# def verify_chain():
#   block_index = 0 
#   is_valid = True
#   for block in blockchain: 
#     # print('-----This is block[0]-----')
#     # print(block[0])
#     # print('----This is block-index-value ---')
#     # print(block_index)
#     # print('-----This is blockchain-----')
#     # print(blockchain)
#     if block_index == 0:
#       block_index += 1
#       continue
#     elif block[0] == blockchain[block_index - 1]:
#       is_valid = True 
#     else:
#       is_valid = False 
#       break
#     block_index += 1
#   return is_valid


# while True:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Output the blockchain blocks')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_amount = get_transaction_value()
#     add_transaction(tx_amount, get_last_block_value())
#   elif user_choice == '2':
#     print_blockchain_elements()
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     break 
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print('Invalid blockchain!')
#     break 

# print('Done!')


# Ninth blockchain version with smarter loops and conditionals 

# blockchain = []

# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # this is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# # This function accepts two arguments.
# # One required one (transaction_amount) and one optional one (last_transaction)
# # The optional one is optional because it has a default value => [1]

# def add_transaction(tx_value, last_tx_value = [1]): 
#   """ Append a new value as well as the last blockchain value to the blockchain

#   # Arguments: 
#   #   : tx_amount: The amount that should be added. 
#   #   : last_tx_value: The last blockchain transaction (default [1]).
#   """
#   if last_tx_value == None:
#     last_tx_value = [1]
#   blockchain.append([last_tx_value, tx_value])

# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   user_input = float(input('please input your transaction value: '))
#   return user_input


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)

# def manipulate_blockchain(): 
#   blockchain[0] = [2]

# def verify_chain():
#   block_index = 0 
#   is_valid = True
#   for block in blockchain: 
#     # print('-----This is block[0]-----')
#     # print(block[0])
#     # print('----This is block-index-value ---')
#     # print(block_index)
#     # print('-----This is blockchain-----')
#     # print(blockchain)
#     if block_index == 0:
#       block_index += 1
#       continue
#     elif block[0] == blockchain[block_index - 1]:
#       is_valid = True 
#     else:
#       is_valid = False 
#       break
#     block_index += 1
#   return is_valid

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Output the blockchain blocks')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_amount = get_transaction_value()
#     add_transaction(tx_amount, get_last_block_value())
#   elif user_choice == '2':
#     print_blockchain_elements()
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print('Invalid blockchain!')
#     break 
# else: 
#   print('User left!')


# print('Done!')


# Tenth blockchain version w/ range function for loops 

# blockchain = []

# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # this is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# # This function accepts two arguments.
# # One required one (transaction_amount) and one optional one (last_transaction)
# # The optional one is optional because it has a default value => [1]

# def add_transaction(tx_value, last_tx_value = [1]): 
#   """ Append a new value as well as the last blockchain value to the blockchain

#   # Arguments: 
#   #   : tx_amount: The amount that should be added. 
#   #   : last_tx_value: The last blockchain transaction (default [1]).
#   """
#   if last_tx_value == None:
#     last_tx_value = [1]
#   blockchain.append([last_tx_value, tx_value])

# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   user_input = float(input('please input your transaction value: '))
#   return user_input


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)

# def manipulate_blockchain(): 
#   blockchain[0] = [2]

# def verify_chain():
#   # block_index = 0 
#   is_valid = True
#   for block_index in range(len(blockchain))
    
#     # print('-----This is block[0]-----')
#     # print(block[0])
#     # print('----This is block-index-value ---')
#     # print(block_index)
#     # print('-----This is blockchain-----')
#     # print(blockchain)
#     if block_index == 0:
#       continue
#     elif blockchain[block_index][0] == blockchain[block_index - 1]:
#       is_valid = True 
#     else:
#       is_valid = False 
#       break
#   return is_valid

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Output the blockchain blocks')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_amount = get_transaction_value()
#     add_transaction(tx_amount, get_last_block_value())
#   elif user_choice == '2':
#     print_blockchain_elements()
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print('Invalid blockchain!')
#     break 
# else: 
#   print('User left!')


# print('Done!')

# # Eleventh blockchain version with more complex data structures & block mining 
# genesis_block = {
#   'previous_hash': '',
#   'index': 0,
#   'transactions': []
# }
# blockchain = [genesis_block]
# # Adding a list to track our transactions 
# open_transactions = []
# owner = 'Matthew Chen'

# def get_last_block_value():
#   """ Returns the value of the current blockchain.
  
#   This function accepts two arguments.
#   One required one (transaction_amount) and one optional one (last_transaction)
#   The optional one is optional because it has a default value => [1]
#   """
#   if len(blockchain) < 1:
#     return None 
#   # This is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# def mine_block():
#   # Pass allows us to tell the program not to execute any code because we will come back to it
#   # Pass this code and do not throw an err
#   # pass 
#   last_block = blockchain[-1]
#   hashed_block = ''
#   for key in last_block: 
#     value = last_block[key]
#     hashed_block += str(value)

#   block = {
#     'previous_hash': hashed_block,
#     'index': len(blockchain),
#     'transactions': open_transactions
#     }
#   blockchain.append(block)

# def add_transaction(recipient, sender = owner, amount = 1.0): 
#   """ Append a new value as well as the last blockchain value to the blockchain """

#   transaction = {
#     'sender': sender,
#     'recipient': recipient,
#     'amount': amount
#   }
#   # We are no longer appending directly to the blockchain
#   # Instead we are appending to the open_transaction list 
#   open_transactions.append(transaction)

# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   tx_recipient = input('Enter the receipient ')
#   tx_amount = float(input('please input your transaction value: '))
#   # tuple data structure 
#   return (tx_recipient, tx_amount)


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)


# def manipulate_blockchain(): 
#   blockchain[0] = [2]


# def verify_chain():
#   # block_index = 0 
#   is_valid = True
#   # Will start at index 0 and go up to length of blockchain 
#   for block_index in range(len(blockchain)): 
#     print(f'this is len(blockchain): {len(blockchain)} ')
#     if block_index == 0: 
#       # Because we are checking first block, we should skip the iteration and move to index = 1 
#       continue 
#     if blockchain[block_index][0] == blockchain[block_index - 1]:
#       is_valid = True 
#       # print('-----This is blockchain[block_index][0]-----')
#       # print(blockchain[block_index][0])
#       # print('this is block_index')
#       # print(block_index)
#       # print('----This is block_index - 1 ---')
#       # print(block_index - 1)
#       # print('-----This is blockchain[block_index-1]-----')
#       # print(blockchain[block_index -1])  
#       # print('-----This is blockchain-----')
#       # print(blockchain)
#     else:
#       is_valid = False
#       # print('-----This is blockchain[block_index][0]-----')
#       # print(blockchain[block_index][0])
#       # print('this is block_index')
#       # print(block_index)
#       # print('----This is block_index - 1 ---')
#       # print(block_index - 1)
#       # print('-----This is blockchain[block_index-1]-----')
#       # print(blockchain[block_index -1])  
#       # print('-----This is blockchain-----')
#       # print(blockchain)
#       break
#   return is_valid

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Mine block')
#   print('3: Output the blockchain blocks')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_data = get_transaction_value()
#     # Unpacking the tuple
#     # Pulls out first el and stores in recipient then pulls second el and stores in amount 
#     recipient, amount = tx_data
#     # Since sender = owner, we need to put amount = amount to skip the default for sender 
#     add_transaction(recipient, amount = amount)
#     print(open_transactions)
#   elif user_choice == '2':
#     mine_block()
#   elif user_choice == '3':
#     print_blockchain_elements()
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   # if not verify_chain():
#   #   print_blockchain_elements()
#   #   print('Invalid blockchain!')
#   #   break
#   # else: 
#   #   print('Verfication Occurred') 
# else: 
#   print('User left!')


# print('Done!')

# import functools
# # Twelth blockchain version w/ list comprehension for mining blocks & participants 
# MINING_REWARD = 10

# genesis_block = {
#   'previous_hash': '',
#   'index': 0,
#   'transactions': []
# }
# blockchain = [genesis_block]
# # Adding a list to track our transactions 
# open_transactions = []
# owner = 'Matthew Chen'
# participants = {'Matthew Chen'}


# def hash_block(block):
#   """ Hashes a block and returns a string representation of it"""
#   return '-'.join([str(block[key] for key in block)])


# def get_balance(participant):
#   # Using a list comprehension to check tx's amount value in each block's transactions if the sender is the participant in every block in the blockchain 
#   tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
#   # Need to check open tx to ensure we are getting full list of tx. This will restrict what tx can be sent once we check processed + open tx.
#   open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
#   tx_sender.append(open_tx_sender)
#   # Replacing for loop w/ lambda function to sum our senders tx amount
#   # 1st arg = lambda function, 2nd arg = reference var, 3rd arg = initial amount
#   # tx_sum is the last value & tx_amt is the current amount 
#   amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender ,0)

#   # previous code that we are replacing w/ lambda function 
#   # amount_sent = 0
#   # for tx in tx_sender:
#   #   if len(tx) > 0:
#   #     amount_sent += tx[0]
#   tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

#   amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,tx_recipient,0)

#   # previous code that we are replacing w/ lambda function
#   # amount_received = 0
#   # for tx in tx_recipient:
#   #   if len(tx) > 0:
#   #     amount_received += tx[0]

#   return amount_received-amount_sent


# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # This is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# # Checking to see if senders balance is adequate to send the amount stated in transaction 
# def verify_transaction(transaction): 
#   sender_balance = get_balance(transaction['sender'])
#   # Do not if else statement b/c already boolean value 
#   return sender_balance >= transaction['amount']


# def add_transaction(recipient, sender = owner, amount = 1.0): 
#   """ Append a new value as well as the last blockchain value to the blockchain """

#   transaction = {
#     'sender': sender,
#     'recipient': recipient,
#     'amount': amount
#   }
#   # If verifying tx succeeds 
#   if verify_transaction(transaction):
#     # No longer appending directly to the blockchain, but instead appending to the open_transaction list 
#     open_transactions.append(transaction)
#     # We are adding to a set so repeated participants will not be duplicated 
#     participants.add(sender)
#     participants.add(recipient)
#     return True
#   return False 

 
# def mine_block():
#   last_block = blockchain[-1]
#   hashed_block = hash_block(last_block)
#   reward_transaction = {
#     'sender': 'MINING',
#     'recipient': owner,
#     'amount': MINING_REWARD
#   }
#   copied_transactions = open_transactions[:]
#   copied_transactions.append(reward_transaction)
#   block = {
#     'previous_hash': hashed_block,
#     'index': len(blockchain),
#     'transactions': copied_transactions
#     }
#   blockchain.append(block)
#   # used to clear out open transactions after every mined block 
#   return True 


# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   tx_recipient = input('Enter the receipient ')
#   tx_amount = float(input('please input your transaction value: '))
#   # tuple data structure 
#   return (tx_recipient, tx_amount)


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)


# def manipulate_blockchain():
#   # Make sure that you don't try to "hack" an empty blockchain  
#   if len(blockchain) >= 1:
#     blockchain[0] = {
#     'previous_hash': [],
#     'index': 0,
#     'transactions': {'sender': 'Rebecca', 'recipient': 'Matthew', 'amount': 100}
#   }


# def verify_chain():
#   """ Verify the current blockchain and return True if it's valid, otherwise return """
#   for (index, block) in enumerate(blockchain): 
#     if index == 0:
#       continue
#     if block['previous_hash'] != hash_block(blockchain[index - 1]): 
#       return False
#   return True 

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Mine block')
#   print('3: Output the blockchain blocks')
#   print('4: Output participants')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_data = get_transaction_value()
#     # Unpacking the tuple
#     # Pulls out first el and stores in recipient then pulls second el and stores in amount 
#     recipient, amount = tx_data
#     # Since sender = owner, we need to put amount = amount to skip the default for sender 
#     if add_transaction(recipient, amount = amount):
#       print('Added transaction!')
#     else:
#       print('Transaction failed!')
#     print(open_transactions)
#   elif user_choice == '2':
#     if mine_block():
#       # resetting the open transactions after every mining of block. Open transactions need to cleared because previous transactions have already been processed 
#       open_transactions = []
#   elif user_choice == '3':
#     print_blockchain_elements()
#   elif user_choice == '4':
#     print(participants)
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print_blockchain_elements()
#     print('Invalid blockchain!')
#     break
#   else: 
#     print('Verfication Occurred') 
#   # Using format method to output nice string 
#   print('Balance of {}:{:6.2f}'.format('Matthew Chen', get_balance('Matthew Chen')))
# else: 
#   print('User left!')


# print('Done!')

# # Thirteenth blockchain version w/ imported hashing functions & splitting code & read and write capabilities

# from functools import reduce
# import hashlib as hl 
# from collections import OrderedDict

# # importing my own functions
# from hash_util import hash_string_256, hash_block

# MINING_REWARD = 10

# genesis_block = {
#   'previous_hash': '',
#   'index': 0,
#   'transactions': [],
#   # proof value is a dummy value 
#   'proof': 100
# }
# blockchain = [genesis_block]
# # Adding a list to track our transactions 
# open_transactions = []
# owner = 'Matthew Chen'
# participants = {'Matthew Chen'}

# def load_data():
#   with open('blockchain.txt', mode = 'r') as f:
#     # returns a list of str
#     file_content = f.readlines()
#     global blockchain 
#     global open_transactions
#     # Two lines of code below have an error b/c we cant append to the strings we get from f.readlines()
#     blockchain = file_content[0]
#     open_transactions = file_content[1]

# # Runs load data as soon as the script is read 
# load_data()

# def save_data():
#   with open('blockchain.txt', mode = 'w') as f: 
#     f.write(str(blockchain))
#     f.write('\n')
#     f.write(str(open_transactions))


# def valid_proof(transactions, last_hash, proof):
#   guess = (str(transactions) + str(last_hash) + str(proof)).encode()
#   guess_hash = hash_string_256(guess)
#   print(guess_hash)
#   # Our requirement for a valid hash 
#   return guess_hash[0:2] == '00'

# def proof_of_work():
#   last_block = blockchain[-1]
#   last_hash = hash_block(last_block)
#   proof = 0
#   while not valid_proof(open_transactions, last_hash, proof):
#     proof += 1 
#   return proof 


# def get_balance(participant):
#   # Using a list comprehension to check tx's amount value in each block's transactions if the sender is the participant in every block in the blockchain 
#   tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
#   # Need to check open tx to ensure we are getting full list of tx. This will restrict what tx can be sent once we check processed + open tx.
#   open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
#   tx_sender.append(open_tx_sender)
#   # Replacing for loop w/ lambda function to sum our senders tx amount
#   # 1st arg = lambda function, 2nd arg = reference var, 3rd arg = initial amount
#   # tx_sum is the last value & tx_amt is the current amount 
#   amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender ,0)

#   # previous code that we are replacing w/ lambda function 
#   # amount_sent = 0
#   # for tx in tx_sender:
#   #   if len(tx) > 0:
#   #     amount_sent += tx[0]
#   tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

#   amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,tx_recipient,0)

#   # previous code that we are replacing w/ lambda function
#   # amount_received = 0
#   # for tx in tx_recipient:
#   #   if len(tx) > 0:
#   #     amount_received += tx[0]

#   return amount_received-amount_sent


# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # This is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]

# # Checking to see if senders balance is adequate to send the amount stated in transaction 
# def verify_transaction(transaction): 
#   sender_balance = get_balance(transaction['sender'])
#   # Do not if else statement b/c already boolean value 
#   return sender_balance >= transaction['amount']


# def add_transaction(recipient, sender = owner, amount = 1.0): 
#   """ Append a new value as well as the last blockchain value to the blockchain """

#   # transaction = {
#   #   'sender': sender,
#   #   'recipient': recipient,
#   #   'amount': amount
#   # }

#   transaction = OrderedDict(
#     [('sender', sender), ('recipient', recipient), ('amount', amount)])

#   # If verifying tx succeeds 
#   if verify_transaction(transaction):
#     # No longer appending directly to the blockchain, but instead appending to the open_transaction list 
#     open_transactions.append(transaction)
#     # We are adding to a set so repeated participants will not be duplicated 
#     participants.add(sender)
#     participants.add(recipient)
#     save_data()
#     return True
#   return False 

 
# def mine_block():
#   """Creates a new block and adds open transactions to it"""
#   last_block = blockchain[-1]
#   hashed_block = hash_block(last_block)
#   proof = proof_of_work()

#   # reward_transaction = {
#   #   'sender': 'MINING',
#   #   'recipient': owner,
#   #   'amount': MINING_REWARD
#   # }

#   reward_transaction = OrderedDict(
#     [('sender','MINING'), ('recipient', owner), ('amount', MINING_REWARD)])

#   copied_transactions = open_transactions[:]
#   copied_transactions.append(reward_transaction)
#   block = {
#     'previous_hash': hashed_block,
#     'index': len(blockchain),
#     'transactions': copied_transactions,
#     'proof': proof 
#     }
#   blockchain.append(block)
  
#   #save_data needs a string not a list
#   save_data()
#   # used to clear out open transactions after every mined block
#   return True 


# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   tx_recipient = input('Enter the receipient ')
#   tx_amount = float(input('please input your transaction value: '))
#   # tuple data structure 
#   return (tx_recipient, tx_amount)


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)


# def manipulate_blockchain():
#   # Make sure that you don't try to "hack" an empty blockchain  
#   if len(blockchain) >= 1:
#     blockchain[0] = {
#     'previous_hash': [],
#     'index': 0,
#     'transactions': {'sender': 'Rebecca', 'recipient': 'Matthew', 'amount': 100}
#   }


# def verify_chain():
#   """ Verify the current blockchain and return True if it's valid, otherwise return """
#   for (index, block) in enumerate(blockchain): 
#     if index == 0:
#       continue
#     if block['previous_hash'] != hash_block(blockchain[index - 1]): 
#       return False
#     if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
#       return False 
#   return True 

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Mine block')
#   print('3: Output the blockchain blocks')
#   print('4: Output participants')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_data = get_transaction_value()
#     # Unpacking the tuple
#     # Pulls out first el and stores in recipient then pulls second el and stores in amount 
#     recipient, amount = tx_data
#     # Since sender = owner, we need to put amount = amount to skip the default for sender 
#     if add_transaction(recipient, amount = amount):
#       print('Added transaction!')
#     else:
#       print('Transaction failed!')
#     print(open_transactions)
#   elif user_choice == '2':
#     if mine_block():
#       # resetting the open transactions after every mining of block. Open transactions need to cleared because previous transactions have already been processed 
#       open_transactions = []
#   elif user_choice == '3':
#     print_blockchain_elements()
#   elif user_choice == '4':
#     print(participants)
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print_blockchain_elements()
#     print('Invalid blockchain!')
#     break
#   else: 
#     print('Verfication Occurred') 
#   # Using format method to output nice string 
#   print('Balance of {}:{:6.2f}'.format('Matthew Chen', get_balance('Matthew Chen')))
# else: 
#   print('User left!')


# print('Done!')

# 14th blockchain version fixing the read_data function. (can't append to a str)

# from functools import reduce
# import hashlib as hl 
# from collections import OrderedDict
# import json 

# # importing my own functions
# from hash_util import hash_string_256, hash_block

# MINING_REWARD = 10

# blockchain = []
# # Adding a list to track our transactions 
# open_transactions = []
# owner = 'Matthew Chen'
# participants = {'Matthew Chen'}

# def load_data():
#   global blockchain 
#   global open_transactions
#   try:
#     with open('blockchain.txt', mode = 'r') as f:
#       # returns a list of str
#       file_content = f.readlines()

#       # json.loads takes a json str and converts to python object 
#       # we have the range function to get rid of the \n 
#       blockchain = json.loads(file_content[0][:-1])
#       updated_blockchain = []
#       # Recreating the blockchain with OrderedDict transactions so they match how we stored them
#       for block in blockchain: 
#         updated_block = {
#           'previous_hash': block['previous_hash'],
#           'index': block['index'],
#           'transactions': [OrderedDict(
#             [('sender', tx['sender']),
#             ('recipient', tx['recipient']),
#             ('amount', tx['amount'])]) 
#             for tx in block['transactions']],
#           'proof': block['proof']
#         }
#         updated_blockchain.append(updated_block)
#       blockchain = updated_blockchain
#       # Need to load open transactions first before updating it to Ordered Dict
#       open_transactions = json.loads(file_content[1]) 
#       updated_transactions = []
#       #Updating the open_transactions before they are added to blockchain
#       # Open transactions lose their OrderedDict notation with saving data
#       for tx in open_transactions:
#         updated_transaction = OrderedDict(
#           [('sender', tx['sender']),('recipient', tx['recipient']),('amount', tx['amount'])]
#         )
#         updated_transactions.append(updated_transaction)
#       open_transactions = updated_transactions
#   # This code runs when we get an IOError b/c blockchain.txt is not found. This will allow our blockchain to run even without an blockchain.txt
#   except (IOError, IndexError): 
#     genesis_block = {
#       'previous_hash': '',
#       'index': 0,
#       'transactions': [],
#       # proof value is a dummy value 
#       'proof': 100
#     }
#     blockchain = [genesis_block]
#     # Unhandled transactions 
#     open_transactions = []

# # Runs load data as soon as the script is read 
# load_data()

# def save_data():
#   try:
#     with open('blockchain.txt', mode = 'w') as f: 
#       f.write(json.dumps(blockchain))
#       f.write('\n')
#       #json dumps converts our list of transactions into a json str 
#       f.write(json.dumps(open_transactions))
#   except IOError:
#     print('Saving failed!')

# def valid_proof(transactions, last_hash, proof):
#   guess = (str(transactions) + str(last_hash) + str(proof)).encode()
#   print(guess)
#   # Hash the string
#   # IMPORTANT: This is NOT the same hash as will be stored in the previous_hash. It's a not a block's hash. It's only used for the proof-of-work algorithm.
#   guess_hash = hash_string_256(guess)
#   print(guess_hash)
#   # Our requirement for a valid hash 
#   return guess_hash[0:2] == '00'

# def proof_of_work():
#   last_block = blockchain[-1]
#   last_hash = hash_block(last_block)
#   proof = 0
#   while not valid_proof(open_transactions, last_hash, proof):
#     proof += 1 
#   return proof 


# def get_balance(participant):
#   # Using a list comprehension to check tx's amount value in each block's transactions if the sender is the participant in every block in the blockchain 
#   tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
#   # Need to check open tx to ensure we are getting full list of tx. This will restrict what tx can be sent once we check processed + open tx.
#   open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
#   tx_sender.append(open_tx_sender)
#   print(tx_sender)
#   # Replacing for loop w/ lambda function to sum our senders tx amount
#   # 1st arg = lambda function, 2nd arg = reference var, 3rd arg = initial amount
#   # tx_sum is the last value & tx_amt is the current amount 
#   amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0 ,tx_sender ,0)

#   # previous code that we are replacing w/ lambda function 
#   # amount_sent = 0
#   # for tx in tx_sender:
#   #   if len(tx) > 0:
#   #     amount_sent += tx[0]
#   tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

#   amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,tx_recipient,0)

#   # previous code that we are replacing w/ lambda function
#   # amount_received = 0
#   # for tx in tx_recipient:
#   #   if len(tx) > 0:
#   #     amount_received += tx[0]

#   return amount_received - amount_sent


# def get_last_block_value():
#   """ Returns the value of the current blockchain. """
#   if len(blockchain) < 1:
#     return None 
#   # This is an implicit else statement. If None is returned, the program will not run return blockchain[-1]
#   return blockchain[-1]


# # Checking to see if senders balance is adequate to send the amount stated in transaction 
# def verify_transaction(transaction): 
#   sender_balance = get_balance(transaction['sender'])
#   # Do not if else statement b/c already boolean value 
#   return sender_balance >= transaction['amount']


# def add_transaction(recipient, sender = owner, amount = 1.0): 
#   """ Append a new value as well as the last blockchain value to the blockchain """

#   transaction = OrderedDict(
#     [('sender', sender), ('recipient', recipient), ('amount', amount)])

#   # If verifying tx succeeds 
#   if verify_transaction(transaction):
#     # No longer appending directly to the blockchain, but instead appending to the open_transaction list 
#     open_transactions.append(transaction)
#     # We are adding to a set so repeated participants will not be duplicated 
#     participants.add(sender)
#     participants.add(recipient)
#     save_data()
#     return True
#   return False 

 
# def mine_block():
#   """Creates a new block and adds open transactions to it"""
#   last_block = blockchain[-1]
#   hashed_block = hash_block(last_block)
#   proof = proof_of_work()

#   # reward_transaction = {
#   #   'sender': 'MINING',
#   #   'recipient': owner,
#   #   'amount': MINING_REWARD
#   # }

#   reward_transaction = OrderedDict(
#     [('sender','MINING'), ('recipient', owner), ('amount', MINING_REWARD)])

#   copied_transactions = open_transactions[:]
#   copied_transactions.append(reward_transaction)
#   block = {
#     'previous_hash': hashed_block,
#     'index': len(blockchain),
#     'transactions': copied_transactions,
#     'proof': proof 
#     }
#   blockchain.append(block)
  
#   # used to clear out open transactions after every mined block
#   return True 


# def get_transaction_value(): 
#   """Returns the trasaction value as a float """
#   tx_recipient = input('Enter the receipient ')
#   tx_amount = float(input('please input your transaction value: '))
#   # tuple data structure 
#   return (tx_recipient, tx_amount)


# def get_user_choice(): 
#   user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
#   return user_input


# def print_blockchain_elements(): 
#   for block in blockchain: 
#     print('Outstanding Block')
#     print(block)
#   else:
#     print('-' * 20)


# def manipulate_blockchain():
#   # Make sure that you don't try to "hack" an empty blockchain  
#   if len(blockchain) >= 1:
#     blockchain[0] = {
#     'previous_hash': [],
#     'index': 0,
#     'transactions': {'sender': 'Rebecca', 'recipient': 'Matthew', 'amount': 100}
#   }

# def verify_chain():
#   """ Verify the current blockchain and return True if it's valid, otherwise return """
#   for (index, block) in enumerate(blockchain): 
#     if index == 0:
#       continue
#     if block['previous_hash'] != hash_block(blockchain[index - 1]): 
#       return False
#     if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
#       return False 
#   return True 


# def verify_transactions():
#   return all([verify_transaction(tx) for tx in open_transactions])

# waiting_for_input = True

# while waiting_for_input:
#   print('Please choose')
#   print('1: Add a new transaction value')
#   print('2: Mine block')
#   print('3: Output the blockchain blocks')
#   print('4: Output participants')
#   print('5: Check transaction validity')
#   print('h: Manipulate the blockchain')
#   print('q: quit')
#   user_choice = get_user_choice()
#   if user_choice == '1':
#     tx_data = get_transaction_value()
#     # Unpacking the tuple
#     # Pulls out first el and stores in recipient then pulls second el and stores in amount 
#     recipient, amount = tx_data
#     # Since sender = owner, we need to put amount = amount to skip the default for sender 
#     if add_transaction(recipient, amount = amount):
#       print('Added transaction!')
#     else:
#       print('Transaction failed!')
#     print(open_transactions)
#   elif user_choice == '2':
#     if mine_block():
#       # resetting the open transactions after every mining of block. Open transactions need to cleared because previous transactions have already been processed 
#       open_transactions = []
#        #save_data needs a string not a list
#       save_data()
#   elif user_choice == '3':
#     print_blockchain_elements()
#   elif user_choice == '4':
#     print(participants)
#   elif user_choice == '5':
#     if verify_transactions():
#       print('All transactions are valid')
#     else:
#       print('There are invalid transactions')
#   elif user_choice == 'h':
#     if len(blockchain) >= 1:
#       manipulate_blockchain()
#   elif user_choice == 'q': 
#     waiting_for_input = False
#   else:
#     print('Invalid input. Please pick from the menu items')
#   if not verify_chain():
#     print_blockchain_elements()
#     print('Invalid blockchain!')
#     break
#   else: 
#     print('Verfication Occurred') 
#   # Using format method to output nice string 
#   print('Balance of {}:{:6.2f}'.format('Matthew Chen', get_balance('Matthew Chen')))
# else: 
#   print('User left!')


# print('Done!')