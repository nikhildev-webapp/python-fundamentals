# Taking Inputs from user in Python
# Exercise-1-create a program take username and age of user and display it
username=input('Enter your Name:')
age=int(input('Enter your age:'))
print(f'He my name is:{username}\nI am {age} year old')

#Exercise-2-take the length and width of rectangle and find the area
length=int(input('Enter the length of rectangle:'))
width=int(input('Enter the Width of rectangle:'))
print(f'Area of rectangle is:{length*width}')

#Exercise-3-find the area of circle
radius=int(input('Enter the radius of circle:'))
pi=3.14
print(f'Aread of circle is:{pi*radius**2}')

#Exercise-4-find the simple intrest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")
print(f"Total Return Amount: {principal + simple_interest}")

#Exercise-find the sqaure and cube of the number
n=int(input('Enter the Number:'))
sqaureN=n**2
cubeN=n**3
print(f'Sqaure of the Number:{sqaureN}\nCube of the Number:{cubeN}')