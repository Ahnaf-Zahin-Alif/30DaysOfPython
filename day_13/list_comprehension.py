numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filterd_negative_and_zero = [
    i for i in numbers if i <= 0
]
print(filterd_negative_and_zero)


list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [
    number for row in list_of_lists for number in row
    ]
print(flattened_list)


lst = [
    (i , i**0 , i**1 , i**2  , i**3 , i**4 , i**5) for i in range(11)
    ]
print(lst)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


new_countries = [
    [
        country.upper() , country.upper()[:3] , city.upper() 
    ]
    for row in countries
    for country , city in row
]

print(new_countries)


dict_countries = [
    
        {'country': country.upper() , 'city' : city.upper()}
    
    for row in countries
    for country , city in row
]


print(dict_countries)



names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]


full_name = [
    
    first_name + ' ' + last_name 
    
    for row in names
    for first_name , last_name in row
]

print(full_name)


slope = lambda x1 , y1 , x2 , y2 : (y2 - y1) / (x2 - x1)

print('Slope' , slope(2 , 2 , 6 , 10))

