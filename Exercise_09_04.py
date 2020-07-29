#open and read through mbox-short.txt
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
emails =[]

for line in handle:
    #scan for line that begins with From
    if not line.startswith('From '): continue
    else:
        # looks for sender's email
        words = line.split()
        email = words[1]
        # append email addres list 
        emails.append(email)

# create dictionary of email addresses and counts of emails recieved
for email in emails:
    counts[email] = counts.get(email, 0) + 1

bigword = 0
bigcount = 0

#look for the sender sent most emails  
for email, count in counts.items():
    if count is None or count > bigcount:
        bigword = email
        bigcount = count

print (bigword, bigcount)