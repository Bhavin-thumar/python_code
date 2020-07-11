class Node:
	def __init__(self, data):
		self.data = data
		self.next = None



class Linkedlist:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		self.printList()


	def insertAfter(self, prev_data, new_data):
		new_node = Node(new_data)
		instance = self.head
		while  instance.data != prev_data :
			instance = instance.next
			if instance.next is None:
				break
		if instance.next is None:
			print("Data must be in Linkedlist")
			return
		new_node.next = instance.next
		instance.next = new_node
		self.printList()


	def append(self, new_data):
		if self.head is None:
			new_node = Node(new_data)
			self.head = new_node
			self.printList()
			return
		instance = self.head
		while instance.next is not None:
			instance = instance.next
		new_node = Node(new_data)
		instance.next = new_node
		self.printList()


	def getCount(self):
		count = 0
		instance = self.head
		while instance :
			instance = instance.next
			count += 1
		return count


	def inserttoposition(self, position, new_data):

		if position >= self.getCount():
			print("Position out of range")
			return


		if position == 0:
			return self.push(new_data)

		count = 0
		instance = self.head

		while position - count != 1:
			instance = instance.next
			count += 1

		new_node = Node(new_data)
		new_node.next = instance.next
		instance.next = new_node
		self.printList()


	def printList(self):
		instance = self.head
		while instance:
			print(instance.data,end = '--->')
			instance = instance.next
		print()


	def deleteKey(self, key):
		instance = self.head
		if instance.data == key:
			self.head = instance.next
			instance = None
			self.printList()
			return
		while instance.data != key:
			prev = instance
			if instance.next is None:
				print('Key not found')
				return
			instance = instance.next

		prev.next = instance.next
		instance = None
		self.printList()


	def deleteNode(self, position):
		if position == 0:
			first = self.head
			self.head = first.next
			first = None
			return self.printList()
		else:
			if position >= self.getCount():
				print('Position out of range')
				return
			count = 0
			instance = self.head
			while count != position:
				prev = instance
				instance = instance.next
				count += 1
			prev.next = instance.next
			instance = None
			return self.printList()


	def reverse(self):
		instance = self.head
		next_node = instance.next
		instance.next = None

		while next_node is not None:

			next_of_next_node = next_node.next
			next_node.next = instance
			instance = next_node
			next_node = next_of_next_node

		self.head = instance

llist = Linkedlist()
llist.append(11)
llist.append(22)
llist.append(33)
llist.append(44)
llist.append(55)
llist.reverse()
llist.printList()
