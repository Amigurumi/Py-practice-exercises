# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.


text = 'X-DSPAM-Confidence:    0.8475'

x = text.find('0')
y = len(text)
num = text[x:y]
print (float(num))

# Prof. solution
str =  'X-DSPAM-Confidence:    0.8475'

ipos = str.find(:)
piece = str [ipos+2:]
value = float(piece)
print (value)
