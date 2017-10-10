import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *

filename =''
data=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
jj = 0
i=0
from huffman import *
from sf1 import *
from lzw import *
from update1 import *

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#--------------------------------------------MAIN GUI START-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

class TkFileDialogExample(Tkinter.Frame):

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 50, 'pady': 10}
        button_opt2 = {'padx': 50, 'pady': 10}

        # define buttons
        Tkinter.Button(self, text='choose file', command=self.choose_file).grid(row = 1, column = 1, padx = 50, pady = 5)
        Tkinter.Button(self, text='compress', command=self.compress_fn).grid(row = 2, column = 0, padx = 20, pady = 10)
        Tkinter.Button(self, text='decompress', command=self.decompress_fn).grid(row = 2, column = 2, padx = 20, pady = 10)
	Tkinter.Button(self, text='learn', command=self.learn_fn).grid(row = 3, column = 1, padx = 20, pady = 10)        
	#label_var = StringVar()
	global string_set
	string_set = StringVar()
        #label = Label( root, textvariable=label_var).grid(row = 4, column = 0, padx = 0, pady = 0)
	label2 = Label( root, textvariable=string_set).grid(row = 4, column = 0, padx = 0, pady = 0)
        #label_var.set("Algo chosen:")
        #label1 = Label(self, textvariable="henlo!!!!!!!!!!!!", height=4).grid(row = 3, column = 0, padx = 20, pady = 10)
        #Tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'
        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'


    def choose_file(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        global filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        return filename

        # open file on your own
        #if filename:
        #  return open(filename, 'r')

    def learn_fn(self):
	_j,_i = update_find(filename,data)	

	string_set.set("learned")
	avg_insert = 0.0
	avg_insert = huff_encode(filename)
	update_insert(avg_insert,data,0,_i)
	avg_insert = shannon_compress(filename)
	update_insert(avg_insert,data,2,_i)	
	avg_insert = lzw_compress(filename)
	update_insert(avg_insert,data,4,_i)        

        return 0


    def compress_fn(self):

	_j,_i = update_find(filename,data)	
	
	avg_insert = 0.0
	if(_j==0):
		avg_insert = huff_encode(filename)
		string_set.set("Huffman")
	elif(_j==2):        
		avg_insert = shannon_compress(filename)
		string_set.set("Shannon Fano")
	elif(_j==4):
		avg_insert = lzw_compress(filename)
		string_set.set("LZW")
	else:
		print("Something wrong ;(")


	update_insert(avg_insert,data,_j,_i)        

        return 0

    def decompress_fn(self):

        print "decompress button pressed"
        global filename

        print type(filename)
        #shannon_decompress(filename)
        #huff_decode(filename)
        if filename.find("_huff") != -1:
            #huffdecompression
            huff_decode(filename)
            print "huffman!!!"

        if filename.find("_shannon") != -1:
            print "shannon fano!!!!"
            shannon_decompress(filename)

        if filename.find("_lzw") != -1:
            lzw_decompress(fileame)
            print "lzw!!!!!"
        

        

        return 0


if __name__=='__main__':
    root = Tkinter.Tk()
    #TkFileDialogExample(root).pack()
    TkFileDialogExample(root).grid(row = 0, column = 0)
    root.mainloop()


#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------
#--------------------------------------------MAIN GUI END---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
