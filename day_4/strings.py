#Merging or connecting strings is called concatenation
#1
w1 = 'Thirty'
w2 = 'Days'
w3 = 'Of'
w4 = 'Python'
space = ' '

full_word = w1 + space + w2 + space + w3 + space + w4
print('First Word: ',full_word)

#2
wo1 = 'Coding'
wo2 = 'For'
wo3 = 'All'

full_word2 = wo1 + space + wo2 + space + wo3

print('Second Word: ',full_word2)

#3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 13 , 12
company = 'Coding For All'
print(company)
print('Length: ',len(company))
print('Upper: ',company.upper()) 
print('Lower: ',company.lower()) 
print('Capitalize: ' , company.capitalize())
print(company.find('Coding'))
print('Title: ' , company.title())
print('Swapcase: ' , company.swapcase())
print('Sliced the word coding: ',company[7:14])
first_space = company.find(" ")
first_word = company[:first_space]
print('First Word: ',first_word)
print(company.replace('Coding' , 'Python'))
print(company.split())
sentance = 'Python for Everyone'
new_sentance = 'Python for All'
print(sentance.replace(sentance , new_sentance))

#14
big_company = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(big_company.split(', '))

#15 , 16 , 17

print(company[0])
print(company[13])
print(company[10])

#18 , 19 , 20 , 21 , 22
phrase1 = 'Python For Everyone'
words1 = phrase1.split()

acronym1 = words1[0][0] + words1[1][0] + words1[2][0]

print(acronym1)

phrase2 = 'Coding For All'
words2 = phrase2.split()

acronym2 = words2[0][0] + words2[1][0] + words2[2][0]

print(acronym2)
print(phrase2.index('C'))
print(phrase2.index('F'))
sen2 = 'Coding For All People'
print(sen2.rfind('l'))

#23 , 24 , 25 , 26 , 27
phrase3 = 'You cannot end a sentence with because because because is a conjunction'
print(phrase3.rindex('because'))
print(phrase3.index('because'))
print()


start = phrase3.find('because because because')

stop = start + len('because because because')

print(phrase3[start:stop])



#28 , 29 , 30 , 31 , 32 , 33
sen3 = 'Coding For All'
print(sen3.startswith("Coding"))
print(sen3.endswith("coding"))

sen4 = ' Coding For All '
print(sen4.strip())


sen5 = '30DaysOfPython'
sen6 = 'thirty_days_of_python'

print(sen5.isidentifier())
print(sen6.isidentifier())

libraries = ['Django' , 'Flask' , 'Bottle' , 'Pyramid' , 'Falcon']

print('# '.join(libraries))

print('Iam enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabenh\t250\tFinland\tHelsinki')


#35
radius = 10 
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

#36
a = 8
b = 6

print(f'{a} + {b} ={a + b}')
print(f'{a} - {b} ={a - b}')
print(f'{a} * {b} ={a * b}')
print(f'{a} / {b} ={a / b}')
print(f'{a} % {b} ={a % b}')
print(f'{a} // {b} ={a // b}')
print(f'{a} ** {b} ={a ** b}')