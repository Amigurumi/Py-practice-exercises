#P4E Chapter 2 - Variables and Expressions
#Exercise 2.2
name = input("What's your name?")
print('Welcome',name)

#Exercise 2.3
hrs = input('Enter Hours:')
rate = input ('Enter the rate per hour')
pay = float(hrs) * float(rate)
print ('Pay:', pay)

#Chapter 3 - Conditional Code
#Exercise 3.1
hrs = float(input('Enter hours:'))
rate = float(input('Enter rate per hour:'))

if hrs <=40:
    pay = hrs * rate
else hrs >40:
    pay = (40 * rate)+ ((hrs-40)*(rate*1.5))

print (pay)







