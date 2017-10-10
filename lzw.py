def lzw_compress(filename):
    """Compress a string to a list of output symbols."""
    p=open(filename,"r")
    q=open(filename+'_lzw',"w")
    s=p.read()
    ll=len(s)
    print(ll)#prints size of intial file
    print("\n")
    uncompressed=s
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
   # return result
    compressed = result
    compressed2=map(str,compressed)
    comp=compressed2
    q.write(' '.join(compressed2))
    q.close()
    q=open(filename+'_lzw',"r")
    characters=0
    for line in q:
      characters = characters + len(line)
    #l=len(xy)
    print(characters)
    q.close()
    rr=float(characters)/float(ll)
    return rr
 
 
def lzw_decompress(filename):
    """Decompress a list of output ks to a string."""
    from io import BytesIO
    r=open(filename,"r")
    outFileName = filename[:filename.index('_lzw')]
    outFileName = outFileName[:outFileName.index('.')] + 'Decompressed' + outFileName[outFileName.index('.'):]
    s=open(outFileName,"w")
    ss=r.read()
    compressed=list(map(int,ss.split()))
    #compressed = [int(i) for i in compressed]
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = BytesIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    compressed2=map(str,result.getvalue())
    #comp=compressed2
    s.write(''.join(compressed2))
    s.close()
 
if __name__ == "__main__":
    #lzw_compress()
    #lzw_decompress()
    print
'''# How to use:
#ss="1.txt"
p=open("1.txt","r")
q=open("1_lzw.txt","w")
s=p.read()
ll=len(s)
print(ll)#prints size of intial file
print("\n")
compressed = compress(s)
compressed2=map(str,compressed)
comp=compressed2
#xy=' '.join(comp)
q.write(' '.join(compressed2))
q.close()
q=open("1_lzw.txt","r")
characters=0
for line in q:
    characters = characters + len(line)
#l=len(xy)
print(characters)#prints the size of compressed file
#print (compressed)
decompressed = decompress(compressed)
#print (decompressed)'''
