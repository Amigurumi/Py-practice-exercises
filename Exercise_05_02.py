smallest = None
largest = None

while True:
    num = (input ('Enter a number: '))
    if num == 'done':
        break
    try:
        fn = int (num)        
    except:
        print ('Invalid input')
    if smallest is None and largest is None:
        smallest = fn
        largest = fn
    elif fn < smallest:
        smallest = fn
    elif fn > largest:
        largest = fn

print ('Maximum is',largest)
print ('Minimum is', smallest)