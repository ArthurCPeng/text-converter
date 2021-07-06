# text-converter
A program which converts Chinese text from horizontal orientation to vertical orientation, with an interface built with Tkinter.

The full text inputted into the program is converted into blocks of text, with a specified number of characters for each row and column.  

The blocks of text are separated by separators and empty lines.

The converted text is outputted as a file. The characters before the first return, space, dot or comma, or the first 10 characters are used as the file name. If the file name already exists, the original file is overwritten. 

To ensure proper alignment, any Arabic numerals are replaced with Chinese characters, and any English punctuation marks are replaced by their Chinese counterpart. 

Several parameters can be specified in the conversion. All numeric inputs must be integers.
- **rows**: the number of rows, or the number of non-space characters in each column.  
- **columns**: the number of columns, or the number of non-space characters in each row.  
- **left to right / right to left**: specify whether the outputted text is to be read from left to right or right to left.  
- **separation distance**: the number of lines added before and after each line of separators.  
- **separator length**: the length of (or number of characters contained in) each separator line.  
- **separator marker**: what symbol to use as the separator (e.g. "*").  
