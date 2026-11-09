list1 = []

list5 = ['apple' , 'mango' , 'banana' , 'grape' , 'borokola']


print('Length: ' , len(list5))


print('First Item: ' , list5[0])
print('Middle Item: ' , list5[2])
print('Last Item: ' , list5[4])


mixed_data_types = [
    'Ahnaf Zahin Alif',
    21,
    5.6,
    'unmarried',
    'Dhaka'
    
]


it_companies =[
    'Facebook' , 'Google' , 'Microsoft' , 'Apple' , 'IBM' , 'Oracle' , 'Amazon'
]

print(it_companies)

print('Length of companies: ' , len(it_companies))

print('First Company: ' , it_companies[0])
print('Middle Company: ' , it_companies[3])
print('Last Company: ' , it_companies[6])


it_companies[2] = 'Nvidia'
print('Modified company: ',it_companies)

it_companies.append('AMD')
print('Appended: ' , it_companies)


it_companies.insert(3 , 'Meta')
print('Inserted: ',it_companies)


it_companies[1] = it_companies[1].upper() 
print(it_companies)


print('Joined: ' , '# '.join(it_companies))



print('Meta' in it_companies)

it_companies.sort()
print('Sorted' , it_companies)

it_companies.reverse()
print('Reversed: ' , it_companies)



print('Sliced First Three: ' , it_companies[:3])
print('Sliced Last Three: ' , it_companies[-3:])

length = len(it_companies)
mid = length // 2
print('Middle removed: ' , it_companies.pop(mid))

print('Sliced middle company: ' , it_companies[mid:mid+1])

print('First company removed: ' , it_companies.pop(0))

print('Last company removed: ' , it_companies.pop())


it_companies.clear()
del it_companies

front_end = [
    'HTML' , 'CSS' , 'JS' , 'React' , 'Redux'
]

back_end = [
    'Node' , 'Express' , 'MongoDB'
]

full_stack = front_end + back_end


print(full_stack)

full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')

print('Appended: ' , full_stack)




ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


ages.sort()
print('Sorted: ' , ages)



min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)

print("Max and min added: " , ages)

length_ages = len(ages)
mid1 = ages[length_ages // 2 -1]
mid2 = ages[len(ages) // 2]
median = (mid1 + mid2) / 2

print('Median: ' , median)


average_age = sum(ages) / length_ages
print('Average: ' , average_age)

range_age = max_age - min_age
print(range_age)


diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)

print('abs(min - average): ' , diff_min)
print('abs(max - average): ' , diff_max)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];


length_countries = len(countries)
mid_country = length_countries // 2

print('Middle Country: ',countries[mid_country])


if length_countries % 2 == 0:
    split = length_countries // 2
else:
    split = (length_countries // 2) + 1
    
    
first_half = countries[:split]    
second_half = countries[split:] 
    
print('First Half Length: ' , len(first_half))    
print('Second Half Length: ' , len(second_half))    
    

sample_countries = [
    'China' , 'Russia' , 'USA' , 'Finland' , 'Sweeden' , 'Norway' , 'Denmark']    
 
print('First Country: ' , sample_countries[0]) 
print('Second Country: ' , sample_countries[1]) 
print('Third Country: ' , sample_countries[2]) 
print('Scandic Countries: ' , sample_countries[3:])    