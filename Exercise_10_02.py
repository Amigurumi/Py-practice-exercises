#open and read through mbox-short.txt
name = input('Enter file: ')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = []
cthour = dict()

for line in handle:
    #scan for line that begins with From
    if not line.startswith('From '): continue
    else:
        # look for time (position 6th) block
        block = line.split()
        hour = block[5]
        # pull out the hour from time (e.g. 09:00:30) and add leading 0
        block = hour.split(':')
        hour = block[0].zfill(2)
        # append the hour to the time list 
        time.append(hour)
        
#create dictionary of all hour sent/recieved and counts 
for hr in time:
    cthour[hr] = cthour.get(hr, 0) + 1

#convert dictionary to a list of tuples and sort 
count = list (cthour.items())
count.sort()

# print out key & value
for key, value in count:
    print (key, value)      
