from tkinter import *

#How many spaces is equivalent to one character
space_width = 3
spacing = 1
default_rows = 10
default_columns = 10

#Default values
default_separation_distance = 1
default_separator_length = 15
default_separator_marker = '*'
direction = 'right to left'


root = Tk()
root.geometry('800x600')
root.title('Text Converter')

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

rows_label = Label(frame1, text = 'rows', width = 20)
rows_label.grid(row = 0, column = 0)

rows = Entry(frame1, width = 20)
rows.grid(row = 1, column = 0)

columns_label = Label(frame1, text = 'columns', width = 20)
columns_label.grid(row = 0, column = 1)

columns = Entry(frame1, width = 20)
columns.grid(row = 1, column = 1)


#Functions to change the direction of the vertical text
def left_right():
    global direction
    direction = 'left to right'
    print('direction changed: left to right')
    
def right_left():
    global direction
    direction = 'right to left'
    print('direction changed: right to left')

left_to_right_button = Button(frame1, text = 'left to right', width = 10, command = left_right)
left_to_right_button.grid(row = 1, column = 2)

right_to_left_button = Button(frame1, text = 'right to left', width = 10, command = right_left)
right_to_left_button.grid(row = 1, column = 3)



separation_distance_label = Label(frame2, text = 'separation distance', width = 20)
separation_distance_label.grid(row = 0, column = 0)

separation_distance = Entry(frame2, width = 20)
separation_distance.grid(row = 1, column = 0)

separation_length_label = Label(frame2, text = 'separator length', width = 20)
separation_length_label.grid(row = 0, column = 1)

separation_length = Entry(frame2, width = 20)
separation_length.grid(row = 1, column = 1)

separation_marker_label = Label(frame2, text = 'separation marker', width = 20)
separation_marker_label.grid(row = 0, column = 2)

separation_marker = Entry(frame2, width = 20)
separation_marker.grid(row = 1, column = 2)


entrybox = Text(frame3, width = 100, height = 35)
entrybox.pack()

def callback():

    #If no values are specified in the interface, default values are used
    if rows.get() == '':
        row = default_rows
    else:
        row = int(rows.get())

    if columns.get() == '':
        column = default_columns
    else:
        column = int(columns.get())

    if separation_distance.get() == '':
        sep_distance = default_separation_distance 
    else:
        sep_distance = int(separation_distance.get())

    if separation_length.get() == '':
        sep_length = default_separator_length
    else:
        sep_length = int(separation_length.get())

    if separation_marker.get() == '':
        sep_marker = default_separator_marker
    else:
        sep_marker = separation_marker.get()

    page_chars = row * column

    #Get the text from the entrybox
    text = entrybox.get(1.0,END)

    
    #Extract the characters before the first return, space, period or comma as the title, whichever comes first.
    first_return = text.find('\n')
    first_space = text.find(' ')
    first_dot = text.find('。')
    first_comma = text.find('，')


    #If there are no returns, spaces or dots, extract the first 10 characters as title
    if first_return == -1 and first_space == -1 and first_dot == -1 and first_comma == -1:
        title_end = 10
    else:
        indexes = []
        for index in [first_return, first_space, first_dot, first_comma]:
            if index != -1:
                indexes.append(index)
            
        title_end = min(indexes)


    #If the resulting title is over 20 characters long, extract the first 10 characters as the title.
    #If the resulting title is an empty string, extract the first 5 characters as the title.
    if title_end > 20:
        title_end = 10
    elif title_end < 1:
        title_end = 5

    title = text[0:title_end]
    title = title.replace('/','-')

    #Remove spaces and new lines
    text = text.replace('\n','')
    text = text.replace(' ','')

    #Replace English punctuation with Chinese punctuation
    text = text.replace(',','，')
    text = text.replace('\'','‘')
    text = text.replace('\"','”')
    text = text.replace(':','：')
    text = text.replace(')','）')
    text = text.replace('(','（')
    text = text.replace('[','【')
    text = text.replace(']','】')
    text = text.replace('!','！')
    text = text.replace('?]','？')

    #Replace Arabic numerals with Chinese characters
    text = text.replace('0','零')
    text = text.replace('1','一')
    text = text.replace('2','二')
    text = text.replace('3','三')
    text = text.replace('4','四')
    text = text.replace('5','五')
    text = text.replace('6','六')
    text = text.replace('7','七')
    text = text.replace('8','八')
    text = text.replace('9','九')

    pages = int(len(text)/page_chars)+1
     
    text_list = []

    converted_text = ''


    for i in range(0,pages-1):
        text_list.append(text[i*page_chars:(i+1)*page_chars])

    final_text = text[(pages-1)*page_chars:len(text)]

    #For text blocks whose length are smaller than the pre-specified length of row*column,
    #pad with either Chinese commas (right to left) or spaces (left to right), to ensure alignment
    if direction == 'right to left':
        final_text = final_text[:] + '。'*(page_chars-len(final_text))
    if direction == 'left to right':
        final_text = final_text[:] + ' '*(page_chars-len(final_text))
        
    text_list.append(final_text)

        
    #Convert text into vertical orientation, block by block
    for page_text in text_list:
        page_text_converted = ''
        for j in range(0,row):
            for i in range(0,column):
                if direction == 'left to right':
                    page_text_converted += page_text[i * row + j ]
                if direction == 'right to left':
                    page_text_converted += page_text[page_chars - (i+1) * row + j ]
                if spacing == 1:
                    page_text_converted += ' '*space_width

            
            page_text_converted += '\n'

        converted_text += page_text_converted

        #Add separators and new lines
        converted_text += sep_distance*'\n'
        converted_text += sep_length*sep_marker
        converted_text += (sep_distance+1)*'\n'

    file = open(title,'w')
    file.write(converted_text)
    file.close()
    print('Converted!')
    

convert = Button(frame3,text = 'convert', width = 20, command = callback)
convert.pack()

frame1.pack()
frame2.pack()
frame3.pack()
