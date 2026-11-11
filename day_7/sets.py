it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


length_it_companies = len(it_companies)
print(length_it_companies)

it_companies.add('Twitter')


it_companies.update(['Brain Station' , 'Nvidia' , 'AMD'])

it_companies.pop('Google')


#

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.union(B)


A.issubset(B)
A.isdisjoint(B)


A.union(B)
B.union(A)
A.symmetric_difference(B)

del A
del B


age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)

print(len(age))
print(len(age_set))


sentatance = 'I am a teacher and I love to inspire and teach people'

words = sentatance.split()
unique = set(words)


