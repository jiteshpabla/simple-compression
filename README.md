# simple-compression

This is a modular and simple compression software written in python.

The basic and famous compression algorithms:

 *shannon fano
 *huffman encoding
 *LZW
 
have been implemented and can be used to compress any file.

The universal compression software  has a very simplistic and easy to use GUI interface made for the user. The first button lets the user choose the file they want to compress using our software, or decompress a file that had previously been compressed by our software. Then our software provides the user with two more buttons namely - “compress” and “decompress” which do exactly what they spell out.

The compression button reads the data-file of our software and chooses which algorithm to use for the given file extention based on previously learned compression ratios, and it also calculates the average compression ratio of the chosen algorithm for the given file format and updates it in the data file. The compressed file is saved with the same filename plus a trailing identifier to to show that it is a compressed file and which algorithm was used to compress it. A label also displays the name of the compression algorithm to the user. 
A log-file is also maintained to keep track of which files were compressed and used which algorithm for compression

The decompression button chooses the decompression algorithm based on the trailing filename information, from among the three decompression algorithms. Then, it invokes the said decompression function and writes the decompressed file in the same extention as it was compressed from with a “decompressed” string attached to the filename.

Finally, the ‘learn’ button is present at the end so that the user can train the software on different file formats so that the user gets the optimal compression ratio every time based on their own personal usage. It invokes all three compression ratios and updates the compression ratio data in the data-file to essentially train the software.

###NOTE: 
This project is mainly for educational purposes, as the algorithms used are very basic and are not as capable as the compression techniques used today.
