ss = input('Enter a number between 0.0 and 1.0: ')
try:
    fs = float (ss)
except:
    print ('Number is out of range')
    quit ()

if fs >= 0.9:
    print ('A')
elif fs >= 0.8:
    print ('B')
elif fs >= 0.7:
    print ('C')
elif fs >= 0.6:
    print ('D')
else:
    print ('F')