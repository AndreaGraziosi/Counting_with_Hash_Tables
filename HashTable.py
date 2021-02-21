from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣  Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    self.arr = [LinkedList() for i in range(self.size)]
    return self.arr


  # 2️⃣  Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    """get the index of the key"""
    #get the first letter of the key
    first_letter = key[0]
    #calculate how far the distance is from a and mod it
    distance_from_a = ord(first_letter)-ord('a')
    index = distance_from_a % self.size
    return index

  # 3️⃣ Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    #get the index
    key_hash = self.hash_func(key)

    #go to index  desired 
    while self.arr[key_hash] = key_hash:
    
    # get the linked list at that index

    #append the (key,value) tot the linnked list
       if self.arr[key_hash] = key_hash
            append(key,value)



  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
      print_nodes()
      
    pass
