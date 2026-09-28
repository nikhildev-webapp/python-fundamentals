#Conditional Statments in python
#Exercise-1-Check the number is odd or even
userN=int(input('Enter the number:'))
if userN%2==0:
    print('Number is Even')
else:
    print('Number is Odd')

#Exercise-2-check the number is positive or negative
userN_1=int(input('Enter the Number:'))
if userN_1<0:
    print('Number is Negative')
else:
    print('Number is positive')

#Exercis-3-find the largest of two number
num1=float(input('Enter the Number 1:'))
num2=float(input('Enter the Number 2:'))

if num1>num2:
    largest=num1
else:
    largest=num2

print(f'The largest number is:{largest}')

#Exercise-4-find the largest of three number
numX=float(input('Enter the value of X:'))
numY=float(input('Enter the value of Y:'))
numZ=float(input('Enter the value of Z:'))

if numX>=numY and numX>=numZ:
    largestValue=numX
elif numY>=numX and numY>=numZ:
    largestValue=numY
else:
    largestValue=numZ

print(f'The largest value of Three Variable is:{largestValue}')

#Exercise-5-check the year is leap year or not
year=int(input('Enter the Year:'))
if(year%4==0 and year%100!=0) or(year%400==0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

#Exercise-6-check the voting eligiblity
userAge=int(input('Enter the Your Age:'))
if userAge>=18:
    print('You are Eligible to Vote')
else:
    print('You are not Eligible to Vote')