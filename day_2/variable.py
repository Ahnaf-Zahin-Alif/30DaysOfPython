#Day 2 : 30 days of programming 
import math

firstName = 'Ahnaf'
lastName = 'Zahin'
fullName = 'Ahnaf Zahin Alif'

country = 'Bangladesh'

city = 'Dhaka'

age = 21

year = 2026

is_married = False

is_true = True

is_light_on = True

x , y , z = 1 , 2 , 3 



print('First Name: ' , firstName)
print('Last Name: ' , lastName)
print('Full Name: ' , fullName)
print('Country: ' , country)
print('City: ' , city)
print('Age: ' , age)
print('Year: ' , year)
print('Is Married: ' , is_married)
print('Iam a student: ' , is_true)
print('The light is on: ' , is_light_on)
print('X' ,x , 'Y' , y  , 'Z' , z)


print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x) , type(y) , type(z))



print(len(firstName))
print(len(lastName))

print(len(firstName) - len(lastName))



num_one = 5 
num_two = 4

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)
product = num_two * num_one
print(product)
divison = num_one / num_two
print(divison)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_divison = num_one // num_two
print(floor_divison)



area_of_circle = math.pi * (30 ** 2)
print('Area: ',area_of_circle)


circum_of_circle = 2 * math.pi * (30 **2)
print('Circumference: ' , circum_of_circle)



radius = float(input("Enter the radius: "))
area = math.pi * (radius ** 2)
print(area)

First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
Country = input("Enter your country: ")
Age = input("Enter your age: ")


print(f"First Name , {First_Name}")
print(f"Last Name , {Last_Name}")
print(f"Country , {country}")
print(f"Age , {age}")


help('keywords')