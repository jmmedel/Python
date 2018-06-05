

"""

Python Forensics - Hash Function

A hash function is defined as the function that maps on a large amount of data to a fixed value with a specified length. This function ensures that the same input results in the same output, which is actually defined as a hash sum. Hash sum includes a characteristic with specific information.

This function is practically impossible to revert. Thus, any third party attack like brute force attack is practically impossible. Also, this kind of algorithm is called one-way cryptographic algorithm.

An ideal cryptographic hash function has four main properties −

It must be easy to compute the hash value for any given input.
It must be infeasible to generate the original input from its hash.
It must be infeasible to modify the input without changing the hash.
It must be infeasible to find two different inputs with the same hash.
Example
Consider the following example which helps in matching passwords using characters in hexadecimal format.


"""

import uuid
import hashlib
  
def hash_password(password):
   # userid is used to generate a random number
   salt = uuid.uuid4().hex #salt is stored in hexadecimal value
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
     
def check_password(hashed_password, user_password):
   # hexdigest is used as an algorithm for storing passwords
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode()
      + user_password.encode()).hexdigest()

new_pass = input('Please enter required password ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Re-enter new password ')

if check_password(hashed_password, old_pass):
   print('Yuppie!! You entered the right password')
else:
   print('Oops! I am sorry but the password does not match')



"""

Flowchart
We have explained the logic of this program with the help of the following flowchart −


The password entered twice matches with the hash function. This ensures that the password entered twice is accurate, which helps in gathering useful data and save them in an encrypted format.
"""
