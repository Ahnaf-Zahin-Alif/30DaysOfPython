
age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f"You need {18-age} more years to learn to drive")


my_age = 21

your_age = int(input('Enter your age: '))


if my_age > your_age :
    print(f"Iam {my_age - your_age} years older than you")
elif my_age == your_age:
    print('We are equal of age')
else:
    print(f"You are {your_age-my_age} years older than me")



num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))

if num1 > num2 :
    print(f"{num1} is greater than {num2}")
else:    
    print(f"{num2} is greater than {num1}")




grade = int(input('Enter your number: '))

if 90 <= grade <= 100:
    print('A')
elif 80 <= grade <= 89:
    print('B')
elif 70 <= grade <= 79:
    print('C')
elif 60 <= grade <= 69:
    print('D')
else:
    print('F')

month = input('Enter month: ')

if month in ['September' , 'October' , 'November']:
    print('The season is autumn')
elif month in ['December' , 'January' , 'February']:
    print('The season is winter')
else:
    print('The season is summer')


fruits = ['banana', 'orange', 'mango', 'lemon']


fruits_in = input('Enter fruit: ')

if fruits_in not in fruits:
    fruits.append(fruits_in)
    print('Modified Fruits: ' , fruits)
else:
    print('The fruit is already on the list')



person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


if 'skills' in person:
    print(person['skills'][2])
   

if 'Python' in person['skills']:
        print('The person has python as a skill')
        
else:
        print('The person does not have python as a skill')


if 'Javascript' and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a backend developer')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")







