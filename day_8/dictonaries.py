dog = {}
 
dog['name'] = 'Brown'
dog['color'] = 'Golden'
dog['breed'] = 'Pitbull'
dog['legs'] = '4'
dog['age'] = '2'


student = {
    'first_name': 'Ahnaf',
    'last_name': 'Alif',
    'gender': 'male',
    'age': 21,
    'marital_status': 'Unmarried',
    'skills': ['Python', 'Java', 'C++'],
    'country': 'Bangladesh',
    'city': 'Dhaka',
    'address': {
        'area': 'Middle Badda',
        'building_name': 'Badda Nitol Tata House'
    }
}


length_student = len(student)
print(length_student)

skills = student['skills']
print(skills)

print(type(skills))

student['skills'].append('Html , Css')
print(student)




keys = list(student.keys())
print(keys)

values = list(student.values())
print(values)

items = list(student.items())
print(items)


del student['city']
del student
















