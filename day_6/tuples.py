tpl = ()

brothers = (
    'Simon' , 'KSI'
)

sisters = (
    'Comatozze' , 'Riley' , 'Lauren'
)

siblings = brothers + sisters

print(f'I have {len(siblings)} siblings')


parents = (
    'Jonny' , 'Bonnie'
)

family_members = siblings + parents

print('Family Member: ' , family_members)



*siblings , father , mother = family_members


print('Siblings: ' , siblings)
print('Father: ' , father)
print('Mother: ', mother)


fruits = (
    'Grapes' , 'Mangoes'
)

vegetables = (
    'tomato' , 'lettuce'
)

animal_products =(
    'Milk' , 'Egg'
)

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp) 

food_stuff_lt.pop(3)


food_stuff_lt[:3]
food_stuff_lt[3:]

del(food_stuff_lt)

exists = 'Bonnie' in food_stuff_tp
print(exists)


nordic_countries =(
    'Denmark' , 'Finland' , 'Iceland' , 'Norway' , 'Sweeden'
)



estonia_exists = 'Estonia' in nordic_countries
iceland_exists = 'Iceland' in nordic_countries

print('Estonia is a nordic country' , estonia_exists)
print('Iceland is a nordic country' , iceland_exists)
