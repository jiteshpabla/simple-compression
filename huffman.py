from huffmantreenode import HuffmanTreeNode
from queue import Queue
from huffmantree import HuffmanTree
import sys


def huff_encode(fileName):
	"""Takes in a fileName, creates a HuffmanTree and compresses the original file based on this tree."""
	try:
		wholeDoc = open(fileName, 'r')
	except IOError:
		print 'Invalid filename. Make sure your file is in same directory as this program.'
		return
	docStr = wholeDoc.read()
	
	allNodes = createHuffmanNodes(docStr)
	tree = createTree(allNodes)
	tree.parseCodeWords(tree.getRoot())
	codeWordDict = tree.getCodeWords()

	(chars, charsBin) = tree.writeFile(docStr)
	compressedSize = len(chars)/1024.0
	originalSize = tree.getRoot().getWeight()/1024.0
	
	# write the file:
	#outFileName = fileName[:len(fileName) - 4] + 'Compressed.txt'
	outFileName = fileName + "_huff"
	f = open(outFileName, 'w')
	f.write(chars)
	print 'Done. Your compressed file is saved as:', outFileName
	print 'Original:', originalSize, 'KB;', 'Compressed:', compressedSize, 'KB'
	print 'Compression rate of', compressedSize/originalSize
	return compressedSize/originalSize
	
def huff_decode(fileName):
	"""Takes in a file name, rebuilds dictionary and writes the decompressed file."""
	(rebuiltDict, truncatedFileStr) = importDict(fileName)
	if (rebuiltDict, truncatedFileStr) != (None, None):
		tree = HuffmanTree()
		tree.setCodeWords(rebuiltDict)
		reconstructed = tree.decodeFile(truncatedFileStr)
		outFileName = fileName[:fileName.index('_huff')]
		outFileName = outFileName[:outFileName.index('.')] + 'Decompressed' + outFileName[outFileName.index('.'):]
		f = open(outFileName, 'w')
		f.write(reconstructed)
		
		print 'Done. Your decompressed file is saved as:', outFileName

def createHuffmanNodes(docStr):
	"""Reads string of entire document (docStr) and returns a dictionary of form: individual character -> HuffmanNode for that char"""
	results = {}
	for x in docStr: 
		try:
			temp = results[x]
			temp.setWeight(temp.getWeight() + 1)
		except KeyError:
			results[x] = HuffmanTreeNode(1, x)
	return results
		
def createTree(allNodes):
	"""Takes in dictionary of Huffman nodes. Creates a Huffman Tree based on each node's frequencies."""
	listNodes = allNodes.values()
	listNodes.sort(compareHuffNodes)
		
	singleNodes = Queue() 
	comboNodes = Queue()
	while len(listNodes) > 0:
		singleNodes.enqueue(listNodes.pop(0))
	
	
	while len(singleNodes) + len(comboNodes) > 1:
		i = 0
		temp = [None, None]
		for i in range(2):
		
			singleNodeWeight = None
			comboNodeWeight = None
			if singleNodes.peek() != None:
				singleNodeWeight = singleNodes.peek().getWeight()
			if comboNodes.peek() != None:
				comboNodeWeight = comboNodes.peek().getWeight()
				
			if singleNodeWeight == None:
				temp[i] = comboNodes.dequeue()
			elif comboNodeWeight < singleNodeWeight and comboNodeWeight != None:
				temp[i] = comboNodes.dequeue()
			else: 
				temp[i] = singleNodes.dequeue()
					
		parent = HuffmanTreeNode()
		parent.setLeftChild(temp[0]) 
		parent.setRightChild(temp[1])
		comboNodes.enqueue(parent)
		
	root = comboNodes.dequeue() # should only be one left
	
	tree = HuffmanTree(root)
	return tree
	
def importDict(fileName):
	"""Rewrites the dictionary of key value pairs based on the first few lines of compressed file."""
	rebuiltDict = {}
	try:
		f = open(fileName, 'r')
	except IOError:
		print 'Invalid filename. Make sure your file is in same directory as this program.'
		return (None, None)
	numEntries = int(f.readline())

	if f.readline() != 'njh\n':
		print 'maybe this isn\'t a file comprresed by NJ Huffman'
	entryNum = 0
	while entryNum < numEntries: 
		
		tempchar = f.read(1)
		temp = f.read(1) 
		length = ''
		while temp != ':':
			length += temp
			temp = f.read(1)
		
		length = int(length)
		binStr = ''
		i = 0
		for i in range(length/8):
			encodedChar = f.read(1)
			tempBinStr = bin(ord(encodedChar))[2:] 
			binStr += tempBinStr.zfill(8) 
		if length % 8 != 0: 
			encodedChar = f.read(1)
			tempBinStr = bin(ord(encodedChar))[2:] 
			binStr += tempBinStr.zfill(length % 8) 
		
		rebuiltDict[tempchar] = binStr
		entryNum += 1
	return (rebuiltDict, f.read())
	
def compareHuffNodes(node1, node2):
	"""Compares two Huffman nodes by weight"""
	if node1.getWeight() < node2.getWeight():
		return -1
	else:
		return 1

if __name__ == "__main__":
	if sys.argv[1] == 'compress':
		encode(sys.argv[2])


	elif sys.argv[1] =='decompress':
		decode(sys.argv[2])
	else:
		print 'Invalid input. Please enter in the form: huffman.py [compress/decompress] [filename]'

