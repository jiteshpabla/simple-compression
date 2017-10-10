import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *

filename =''

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

    label_var = StringVar()
    label = Label( root, textvariable=label_var, relief=RAISED).grid(row = 3, column = 0, padx = 10, pady = 5)
    label_var.set("Algo chosen:")

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
    filename = tkFileDialog.askopenfilename(**self.file_opt)

    return filename

    # open file on your own
    #if filename:
    #  return open(filename, 'r')


  def compress_fn():



    return 0

  def decompress_fn():
    return 0

  def asksaveasfilename(self):

    """Returns an opened file in write mode.
    This time the dialog just returns a filename and the file is opened by your own code.
    """

    # get filename
    filename = tkFileDialog.asksaveasfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'w')


if __name__=='__main__':
  root = Tkinter.Tk()
  #TkFileDialogExample(root).pack()
  TkFileDialogExample(root).grid(row = 0, column = 0)
  root.mainloop()
