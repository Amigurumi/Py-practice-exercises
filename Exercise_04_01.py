sh = input('Enter hours: ')
sr = input('Enter rate per hour: ')

h = float (sh)
r = float (sr)

def computepay(h, r):
    if h > 40:
        pay = (40*r)+((h-40)*(r*1.5))
        return pay
    else:
        pay = r * h 
        return pay

print ('Pay', computepay (h,r))              