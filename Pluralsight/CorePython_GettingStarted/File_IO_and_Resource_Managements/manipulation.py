"""
Mode | Meaning
  r  | open for reading
  w  | open for writing
  a  | open for appending
  
Selector | Meaning
   b     | binary mode
   t     | text mode

"""
# Writing
f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('What are the roots that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stony rubbish?')
f.close()

# reading
g = open('wasteland.txt', mode='rt', encoding='utf-8')
g.read()
# g.seek(0) # get back to the begin of the file

# g.readline() #reads each line every time is called
# g.readlines() # reads all lines
g.close()

# appending
h = open('wasteland.txt', mode='at', encoding='utf-8')
h. writelines(
              ['Son of aman,\n',
              'You cannot say, or guess, ',
              'for you know only,\n',
              'A heap of broken images,',
              'where the sun beats\n'])
h.close()


