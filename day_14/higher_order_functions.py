#map is function that you can act it on every item

#filter is a function that extracts what you need

#reduce is a function that takes two input and takes the result and goes forward until one value remains



#higher order functions take another functions as parameters or take arguments or returns another function


#Closure means a function within another function


#A decorator uses the @ keyword and modifies the original function returns it without touching the original function

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce
from countries import countries_name
from countries_data import countries_data
from collections import Counter
for a in countries:
    print(a)

for b in names:
    print(b)

for c in numbers:
    print(c)



def upper(country):
    return country.upper()

uppercase_countries = map(upper , countries)

print(list(uppercase_countries))


numbers_squared = list(map(
    lambda x : x ** 2 , numbers
))

print(numbers_squared)

uppercase_name = list(map(
    lambda name : name.upper() , names
))

print(uppercase_name)



def contains_land(country):
    if 'land' in country:
        return True
    return False

has_land = filter(contains_land , countries)

print(list(has_land))



has_land = list(filter(
    lambda country:'land' in country , countries
))

print(has_land)

has_six_characters = list(filter(
    lambda country : len(country) == 6 , countries
))

print(has_six_characters)


has_six_characters_and_more = list(filter(
    lambda country : len(country) >= 6 , countries
))

print(has_six_characters_and_more)

starts_with_e = list(filter(
    lambda country : country[:1] == 'E' , countries
))

print(starts_with_e)




result = reduce(
    lambda summed , current : summed + current , 
    filter(
        lambda x : x % 2 == 0 ,
        map(
            lambda x : x**2 , numbers
        )
    )
)


print(result)


def get_strings_lists(lst):
    return list(filter(
        lambda item : isinstance(item , str) , lst
    ))
        

print(get_strings_lists(numbers))



result = reduce(
    lambda summed , current : summed + current , numbers
)

print(result)


def concatenate_countries(acc , country):
   
        if country == countries[-1]:
            return f"{acc}, and {country}"
        else:
            return f"{acc}, {country}"

sentance = reduce(concatenate_countries , countries) + ' are north European countries'

print(sentance)


def categorize_country(pattern):
    return list(filter(
        lambda country : pattern in country , countries_name
    ))

print(categorize_country('land'))


def country_starting_letter(country):
    letter_counts ={}
    for country in countries_name:
        letter = country[0]
        if letter in letter_counts:
            letter_counts[letter] = letter_counts[letter] + 1
        else:
            letter_counts[letter] = 1

    return letter_counts

print(country_starting_letter(countries_name))



def get_first_ten(country):
    return country[:10]

print(get_first_ten(countries_name))

def get_last_ten(country):
    return country[-10:]

print(get_last_ten(countries_name))


sorted_by_name = sorted(countries_data , key=lambda c : c['name'] )

sorted_by_capital = sorted(countries_data , key=lambda c: c.get('capital' , ''))

sorted_by_population = sorted(countries_data , key=lambda c : c['population'] , reverse=True)


print(sorted_by_name)
print(sorted_by_capital)
print(sorted_by_population)


def sorted_by_location(data , limit =10):
    all_lang = []
    for country in data:
        all_lang.extend(country['languages'])

    return Counter(all_lang).most_common(limit)

sorted_by_population_top_10 = sorted(countries_data , key=lambda c : c['population'] , reverse=True)


print(sorted_by_population_top_10[:10])



