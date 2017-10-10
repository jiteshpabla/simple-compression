class HuffmanTreeNode(object):
	
	def __init__(self, weight=0, value=None):
		self.value = value
		self.left = None
		self.right = None
		self.weight = weight

	def setValue(self, value):
		self.value = value
	
	def getValue(self):
		return self.value
		
	def setWeight(self, newWeight):
		self.weight = newWeight
		
	def getWeight(self):
		return self.weight
		
	def setLeftChild(self, node):
		self.left = node
		self.weight += node.getWeight()

	def getLeftChild(self):
		return self.left
	
	def setRightChild(self, node):
		self.right = node
		self.weight += node.getWeight()

	def getRightChild(self):
		return self.right

	def getHeight(self):
		if self.left == None:
			leftHeight = -1
		else:
			leftHeight = self.left.getHeight()
		if self.right == None:
			rightHeight = -1
		else:
			rightHeight = self.right.getHeight()
		return 1 + max(leftHeight, rightHeight)
		
