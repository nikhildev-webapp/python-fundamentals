#Loops in python
#Exercise-1-print number 1-10
print('Number 1-10')
for i in range(11):
    print(i)

#Exercise-2-print number 10-1
print('Number 10-1')
i=10
while i>=1:
    print(i)
    i-=1

#Exercise-3-Write multiplicatiob table
print('Table of Five')
y=5
x=1
while x<=10:
    print(f'{y}X{x}={y*x}')
    x+=1

#Exercise-4-print odd or even number from 1-20
print('Find the even number or odd number from 1-20')
evenNumber=[]
oddNumber=[]
for i in range(21):
    if i%2==0:
        evenNumber.append(i)
    else:
        oddNumber.append(i)

print(f'Even Numbers:{evenNumber}')
print(f'Odd Numbers:{oddNumber}')

#Exercise-5-sum of first N Numbers
def sum_of_n(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum+=i
    return total_sum

n=10
print(f'Sum of first {n} number is:{sum_of_n(n)}')

#Exercise-6-factorial of number
def factorial(n):
    if n<0:
        return 'Factorial is not deined fpr negative number'

    result=1
    for i in range(1, n+1):
         result *=i
    return result

num=5
print(f'Factorial of {num} is:{factorial(num)}')

#Exercise-7-Fibonacci series
def fibonacci_series(n):
    if n<=0:
        return []
    elif n==1:
        return[0]

    series=[0,1]
    for i in range(2,n):
        next_term=series[-1]+series[-2]
        series.append(next_term)

    return series

term=10
print(f'fibonacci series up to {term} terms:{fibonacci_series(term)}')

#Exercise-8-Count the digit
def count_digit(n):
    n=abs(n)
    if n==0:
        return 1
    count=0
    while n>0:
        count+=1
        n=n//10
    return count

print(count_digit(12345))

#Exercise-9-Reverse the number
def reverse_number(n):
    is_negative=n<0
    n=abs(n)

    reversed_number=0
    while n>0:
        last_digit=n%10
        reversed_number=(reversed_number*10)+last_digit
        n=n//10

    return -reversed_number if is_negative else reversed_number

print(reverse_number(12345))