class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class CicularLinkedList:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head

		else:
			instance = self.head
			while instance.next != self.head:
				instance = instance.next
			self.head = new_node
			new_node.next = instance.next
			instance.next = new_node

		self.printList()


	def printList(self):
		instance = self.head
		while instance:
			print(instance.data, end = '\t')
			instance = instance.next
			if self.head == instance:
				print()
				break


	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head

		else:
			instance = self.head
			while instance.next != self.head:
				instance = instance.next
			first_instance = instance.next
			instance.next = new_node
			new_node.next = first_instance

		self.printList()


	def countlength(self):
		count = 0
		instance = self.head
		while instance.next != self.head:
			instance = instance.next
			count +=1
		count += 1

		return count


	def inserttoposition(self, position, new_data):
		if position == 0 :
			self.push(new_data)
			return
		elif self.countlength() - position >= 1 :
			new_node = Node(new_data)
			instance = self.head
			count = 0
			while position - count != 1 :
				instance = instance.next
				count +=1
			new_node.next = instance.next
			instance.next = new_node

			self.printList()
			return
		elif self.countlength() - position == 0 :
			self.append(new_data)
			return
		else:
			print('position out of range')
			return


	def deleteKey(self, key):
		if self.head.data == key :
			first = self.head
			instance = self.head
			while instance.next != self.head :
				instance = instance.next
			self.head = first.next
			instance.next = self.head
			first = None

			self.printList()
			return
		else:
			instance = self.head
			while instance.data != key :
				prev = instance
				instance = instance.next
				if instance.next == self.head and instance.data != key :
					print('key not found')
					return
			prev.next = instance.next
			instance = None

			self.printList()
			return


	def deleteNode(self, position):
		if self.countlength() - position < 1 :
			print('position out of range')
			return

		elif position == 0:
			instance = self.head
			first = instance
			while instance.next != self.head :
				instance = instance.next
			instance.next = first.next
			self.head = first.next
			first = None

			self.printList()
			return
		else:
			instance = self.head
			count = 0
			while count != position:
				prev = instance
				instance = instance.next
				count += 1
			prev.next = instance.next
			instance = None

			self.printList()
			return


cllist = CicularLinkedList()
cllist.push(10)
cllist.push(30)
cllist.append(20)
cllist.push(40)
cllist.append(50)
cllist.push(60)
cllist.append(70)
cllist.inserttoposition(5, 5)
cllist.deleteKey(70)
cllist.deleteNode(5)