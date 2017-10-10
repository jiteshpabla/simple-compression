from linkedlistnode import LinkedListNode

class Queue(object):
	def __init__(self):
		self.front = None
		self.back = None
		self.count = 0
	
	def enqueue(self, x):
		if self.count == 0:
			self.front = LinkedListNode(x)
			self.back = self.front
		else:
			temp = LinkedListNode(x)
			self.back.setNext(temp)
			self.back = temp
		self.count += 1
	
	def dequeue(self):
		if self.count == 0:
			return None
		else:
			temp = self.front.getData()
			self.front = self.front.getNext()
			if self.count == 1:
				self.back = None
			self.count -= 1
			return temp
	
	def peek(self):
		if self.front == None:
			return None
		else:
			return self.front.data
	
	def __len__(self):
		return self.count
	
