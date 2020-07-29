# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input ('Enter file name: ')
afile = open(fname)

count = 0
num = 0

for line in afile:
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        # manual count of character
        x = line[19:].strip()
        num = num + float (x)   


# Bremen's solution: 

searchText = 'X-DSPAM-Confidence'
for line in afile:
    if line.startswith(searchText):
        count = count + 1
        x = line[len(searchText)+1:].strip()
        num = num + float (x)

average = num / count
print ('Average spam confidence:', average)    