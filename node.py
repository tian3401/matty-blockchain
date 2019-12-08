# module that helps us generate a unique id
from uuid import uuid4
from blockchain import Blockchain
from utility.verification import Verification

class Node: 
  def __init__(self):
    # self.id = str(uuid4())
    # Temporary until we can create a wallet to make data persist
    self.id = 'Matt'
    self.blockchain = Blockchain(self.id)
    

  def get_transaction_value(self): 
    """Returns the trasaction value as a float """
    tx_recipient = input('Enter the receipient ')
    tx_amount = float(input('please input your transaction value: '))
    # tuple data structure 
    return (tx_recipient, tx_amount)


  def get_user_choice(self): 
    user_input = input('Your choice: ') # This is a local variable so no issues with reusing 
    return user_input


  def print_blockchain_elements(self): 
    for block in self.blockchain.chain: 
      print('Outstanding Block')
      print(block)
    else:
      print('-' * 20)


  def listen_for_input(self): 
    waiting_for_input = True

    while waiting_for_input:
      print('Please choose')
      print('1: Add a new transaction value')
      print('2: Mine block')
      print('3: Output the blockchain blocks')
      print('4: Check transaction validity')
      print('q: quit')
      user_choice = self.get_user_choice()
      if user_choice == '1':
        tx_data = self.get_transaction_value()
        # Unpacking the tuple
        # Pulls out first el and stores in recipient then pulls second el and stores in amount 
        recipient, amount = tx_data
        # Since sender = owner, we need to put amount = amount to skip the default for sender 
        if self.blockchain.add_transaction(recipient, self.id, amount = amount):
          print('Added transaction!')
        else:
          print('Transaction failed!')
        print(self.blockchain.get_open_transactions())
      elif user_choice == '2':
        self.blockchain.mine_block()
      elif user_choice == '3':
        self.print_blockchain_elements()
      elif user_choice == '4':
        # Calling the class directly with static methods
        if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
          print('All transactions are valid')
        else:
          print('There are invalid transactions')
      elif user_choice == 'q': 
        waiting_for_input = False
      else:
        print('Invalid input. Please pick from the menu items')
      if not Verification.verify_chain(self.blockchain.chain):
        self.print_blockchain_elements()
        print('Invalid blockchain!')
        break
      else: 
        print('Verfication Occurred') 
      # Using format method to output nice string 
      print('Balance of {}:{:6.2f}'.format(self.id, self.blockchain.get_balance()))
    else: 
      print('User left!')


    print('Done!')

if __name__ == '__main__':
  node = Node()
  node.listen_for_input()

print(__name__) #Tells us who is executing the file 