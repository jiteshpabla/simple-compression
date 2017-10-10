from huffmantreenode import HuffmanTreeNode

class HuffmanTree(object):

	def __init__(self, root = None):
		self.root = root
		self.codeWords = {} 
		
	def parseCodeWords(self, currentNode, currentCode = ''):
		if currentNode == None: 
			return
		else:
			if currentNode.getValue() != None: 
				self.codeWords[currentNode.getValue()] = currentCode
				
			self.parseCodeWords(currentNode.getLeftChild(), currentCode + '0') 
			self.parseCodeWords(currentNode.getRightChild(), currentCode + '1') 
			
	def getCodeWords(self):
		return self.codeWords
		
	def setCodeWords(self, dict):
		self.codeWords = dict
		
	def getRoot(self):
		return self.root
		
	def writeFile(self, doc):		
		binStr = self.convertToBinary(doc)	
		encodedStr = self.getDictRep() 
		i = 0
		while i < len(binStr) - 8: 
			temp = chr(int(binStr[i:i+8], 2))
			encodedStr += temp
			i += 8

		lastLength = len(binStr[i:]) 
		encodedStr += chr(int(binStr[i:], 2)) + str(lastLength) 
		return (encodedStr, binStr)
		
	def getDictRep(self):
		fullStr = str(len(self.codeWords)) + '\nnjh\n'
		for char in self.codeWords:
			binStr = self.codeWords[char]
			encodedStr = char + str(len(binStr)) + ':'
			i = 0
			while i < len(binStr) - 8: 
				temp = chr(int(binStr[i:i+8], 2))
				encodedStr += temp
				i += 8
				
			encodedStr += chr(int(binStr[i:], 2)) 
			fullStr += encodedStr
		return fullStr
		
	def convertToBinary(self, originalDoc):
		binStr = ''
		for x in originalDoc:
			binStr += self.codeWords[x]
		return binStr
		
	def decodeFile(self, doc):
		binStr = ''
		lastTwoChars = doc[len(doc) - 2:] 
		adjustedDoc = doc[:len(doc) - 2] 
		for character in adjustedDoc:
			temp = bin(ord(character))[2:] 
			extraSpace = 8 - len(temp) 
			zeros = '0'*extraSpace
			temp = zeros + temp
			binStr += temp
		lastCharBin = bin(ord(lastTwoChars[0]))[2:] 
		lastCharBin = '0'*(int(lastTwoChars[1]) - len(lastCharBin)) + lastCharBin 
		
		toReturn = self.binToOriginal(binStr)
		return toReturn
		
	def binToOriginal(self, binStr):
		reverseDir = {}
		for x in self.codeWords:
			reverseDir[self.codeWords[x]] = x
		begIndex = 0
		curIndex = 0
		rebuiltStr = ''
		while curIndex < len(binStr) + 1:
			try:
				rebuiltStr += reverseDir[str(binStr[begIndex:curIndex])] 
				begIndex = curIndex 
			except KeyError:
				curIndex += 1 
		return rebuiltStr
			
