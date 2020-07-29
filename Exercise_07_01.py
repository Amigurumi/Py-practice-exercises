file = input ('Enter file name: ')
rfile = open (file, 'r')

for line in rfile:
    line = line.rstrip()
    uline = line.upper()
    print (uline)ine)

# words.txt