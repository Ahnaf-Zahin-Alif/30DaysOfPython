def add_two_numbers(num1 , num2):
     sum = num1 + num2
     print(sum)    
       
add_two_numbers(4 , 5)    


def area_of_circle(r):
     pi = 3.1416
     area = pi*r**2
     return area

print(area_of_circle(10))


def add_all_nums(*nums):
     total = 0
     for n in nums:
         if not isinstance(n , (int , float)):
             return 'Error ! Wrong Argument Passed'
         else:
             total += n
     return total        


print(add_all_nums(4 , 6))




def convert_celcius_to_farenheit(C):
     F = (C*(9/5)) + 32
     return F

print(convert_celcius_to_farenheit(46))


def check_season(month):

     if month in ['December' , 'January' , 'February']:
         return 'The Season is Winter'
     elif month in ['September' , 'October' , 'November']:
         return 'The Season is Autumn'
     elif month in ['March' , 'April' , 'May']:
         return 'The Season is Spring'
     else:
         return 'The Season is Summer'


print(check_season('january'))


import math 
def calculate_slope(m , b):
         return m

def solve_quadratic_eqn(a , b , c):
     D = (b**2) - (4*a*c)

     if D > 0:
         x1 = (-b + math.sqrt(D)) / (2 * a)
         x2 = (-b - math.sqrt(D)) / (2 * a)
         return (x1 , x2)

     elif D==0:
         x = -b / (2 * a)
         return x
     else:
         return "No real roots"


print(solve_quadratic_eqn(1 , 2 , 3))



def print_list(lst):
    for n in lst:
        print(n)


family = [
    'Father' , 'Mother' , 'Brother'
]
print_list(family)


reversed_arr = []
def reverse_list(lst):
    for i in range(len(lst) - 1 , -1 , -1):
        reversed_arr.append(lst[i])
    return reversed_arr



print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 




def capitalize_list(lst):
    capitalize_arr = []
    for i in lst:
        capitalize_arr.append(i.capitalize())

    return capitalize_arr


print(capitalize_list(['ami' , 'valo']))


def add_item(lst , item):
    lst.append(item)
    return lst
    

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat')) 


def remove_item(lst , item):
    lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Milk')) 



def sum_of_numbers(nums):
    sums = 0
    for i in range(0 , nums+1):
        sums += i
    return sums

print(sum_of_numbers(5))
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


def sum_of_odds(nums):
    sums = 0
    for i in range(0 , nums+1):
        if(i % 2 != 0):
            sums += i
    return sums

print(sum_of_odds(5))  

def sum_of_evens(nums):
    sums = 0
    for i in range(0 , nums+1):
        if(i % 2 == 0):
            sums += i
    return sums

print(sum_of_evens(5))  

def evens_and_odds(nums):
    even = 0
    odd = 0
    for i in range(0 , nums+1):
        if(i % 2 == 0):
            even+= 1
        else:
            odd+= 1
    return f"The number odds are {odd}\nThe number of evens are {even}"
    

print(evens_and_odds(100))


def factorial(num):
    
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact

print(factorial(4))



def is_empty(args):
    if not args:
        return True
    return False

print(is_empty([]))


def calculate_mean(lst):
    return (sum(lst) / len(lst))

def calculate_range(lst):
    return (max(lst) - min(lst ))


def calculate_median(lst):
    sorted_list = sorted(lst)
    length_sorted_list = len(sorted_list)
    
    if length_sorted_list % 2 != 0:
        median = sorted_list[length_sorted_list//2]
        return median
    else:
        median1 = sorted_list[(length_sorted_list // 2) - 1]
        median2 = sorted_list[length_sorted_list//2] 
        median = (median1 + median2) / 2
        return median


def calculate_mode(lst):
    return max(lst , key=lst.count)



def calculate_variance(lst):
    mean = calculate_mean(lst)
    total = 0
    for x in lst:
        total += (x-mean) ** 2

    return total / len(lst)




def calculate_std(lst):
    return calculate_variance(lst) ** 0.5


def greet(name = 'Guest'):
     print(f"Hello {name}")


greet('Alif')


def show_args(name , age , city):
    print(f"Received: name: {name} , age: {age} , city: {city}")


show_args('Alif' , 21 , 'Dhaka')




def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2 , num):
                if num % i  == 0:
                    return False
        return True

print(is_prime(7))


def check_list(lst):
    convert_set = set(lst)
    if len(convert_set) == len(lst):
        print('The items are unique')
    else:
        print('It has duplicates')

check_list(lst=[1 , 2 , 3 , 3 , 4])


def check_same_type(lst):
    if not lst:
        return False

    for item in lst:
        if type(item) != type(lst[0]):
            return False

    return True

print(check_same_type([1 , 2 , 'three' , 4]))

def is_valid_variable(name):
    return name.isidentifier()

print(is_valid_variable('alif'))


from day_14.countries_data import countries_data
from collections import Counter

def total_language(data):
    
    all_lang=[]
    for country in data:
        all_lang.extend(country['languages'])

    result = set(all_lang)
    return len(result)


print(total_language(countries_data))


def most_spoken_languages(data , limit=10):
    all_lang=[]
    for country in data:
         all_lang.extend(country['languages'])

    return Counter(all_lang).most_common(limit)


def most_populated_countries(data , limit = 10):
    
    sorted_country = []
    
    sorted_country = sorted(data , key=lambda country:country['population'] , reverse= True)

    return sorted_country[:limit]



print(most_populated_countries(countries_data))
