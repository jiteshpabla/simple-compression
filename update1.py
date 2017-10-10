def update_find(filename,data):
	#filename = raw_input()
	l=filename.rfind('.')
	t=filename[l+1:]
	i=0
	jj=0
	j=0
	#avg_insert = 15
	fobj = open("data_file.txt",'r')
	for line in fobj:
	  for num in line.split():
	    data[i][j] =  float(num)
	    j=j+1
	  j=0
	  i=i+1

		
	if(t=='txt'):
	  i=0
	elif(t=='tif'):
	  i=1
	elif(t=='mp3'):
	  i=2
	elif(t=='wav'):
	  i=3
	j=0
	#jj=0
	k=min(data[i][0],data[i][2],data[i][4])
	for j in range(0,6,2):
	  if(data[i][j]==k):
	    jj=j
	fobj.close()
	fobj2 = open("log_file.txt",'a+')
	fobj2.write("File_Used : ")
	fobj2.write(str(filename))
	fobj2.write("        Algo Used : ")
	if(jj == 0):
		fobj2.write("Huffman\n")
	if(jj == 2):
		fobj2.write("Shannon Fano\n")
	if(jj == 4):
		fobj2.write("LZW\n")
	fobj2.close()
	print "gsdagjggsdgdsghgdg",data[i][0],"iiiiiiiiiiiii",data[i][2],"jjjjjjjjjjjjjjjjjjj",data[i][4]
	return jj,i

def update_insert(avg_insert,data,jj,i):
	'''print "printing da "	
	for i in range(0,4):
	  for j in range(0,6):
		print data[i][j]," "
		#fobj1.write(" ")
	  print("\n")'''
	print "    ",avg_insert,"  "
	avg = ((data[i][jj]*data[i][jj+1]) + avg_insert)/(data[i][jj+1] +1)	
	data[i][jj] = avg
	data[i][jj+1] = data[i][jj+1] + 1.0
	print "gsdagjggsdgdsghgdg",data[i][0],"iiiiiiiiiiiii",data[i][2],"jjjjjjjjjjjjjjjjjjj",data[i][4]
	'''for i in range(0,4):
	  for j in range(0,6):
		print data[i][j]," "
		#fobj1.write(" ")
	  print("\n")'''
	fobj1 = open("data_file.txt",'w')
	for i in range(0,4):
	  for j in range(0,6):
		fobj1.write(str(data[i][j]))
		fobj1.write(" ")
	  fobj1.write("\n")

