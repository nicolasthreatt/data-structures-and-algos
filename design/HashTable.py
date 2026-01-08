from typing import Any


class Node:
	def __init__(self, key: object, value: Any): 
		self.key = key 
		self.value = value
		self.next = None


class HashTable: 
	def __init__(self, capacity: int): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key: object) -> int: 
		return hash(key) % self.capacity 

	def insert(self, key: object, value: Any): 
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = Node(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					current.value = value 
					return
				current = current.next
			node = Node(key, value) 
			node.next = self.table[index] 
			self.table[index] = node 
			self.size += 1

	def search(self, key: object): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key: object): 
		index = self._hash(key) 

		previous = None
		current = self.table[index] 

		while current: 
			if current.key == key: 
				if previous: 
					previous.next = current.next
				else: 
					self.table[index] = current.next
				self.size -= 1
				return
			previous = current 
			current = current.next

		raise KeyError(key) 

	def __len__(self): 
		return self.size 

	def __contains__(self, key: object): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False


if __name__ == '__main__': 
	hash_table = HashTable(5)

	# Add some key-value pairs to the hash table 
	hash_table.insert("apple", 3)
	hash_table.insert("banana", 2) 
	hash_table.insert("cherry", 5)

	# Check if the hash table contains a key 
	print("apple" in hash_table)
	print("durian" in hash_table)

	# Get the value for a key 
	print(hash_table.search("banana"))

	# Update the value for a key 
	hash_table.insert("banana", 4) 
	print(hash_table.search("banana"))

	# Remove a key 
	hash_table.remove("apple") 

	# Check the size of the hash table 
	print(len(hash_table))
