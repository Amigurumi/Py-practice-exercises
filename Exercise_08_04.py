# ask 4 use input for file name
fname = input('Enter file name: ')

#open file
ofile = open (fname)

#create empty list
ls = []

for line in ofile:
    #remove white space at the end of line
    line = line.rstrip()
    #create list from words in line
    words = line.split()
    #check to if the word is already in the list and if not append it to the list.
    for word in words:
        if word not in ls:
            ls.append(word)            
        else: continue

#sort words in the list             
ls.sort()
print (ls)

