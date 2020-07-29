#prompt user input & open file
fl = input ('Enter file name: ')
ofile = open (fl)
ct = 0

for line in ofile:
    #look for line that starts with 'From' and print the 2nd word
    if not line.startswith('From '):
        continue
    else:
        #convert each line to a list of words
        words = line.split()    
        ct = ct + 1
        print (words [1])

#print total count of prints
print ('There were', ct, 'lines in the file with From as the first word')