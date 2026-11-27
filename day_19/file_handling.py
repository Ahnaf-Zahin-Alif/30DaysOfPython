# def count_lines_words(file_path):
#     with open(file_path , 'r' , encoding='utf-8') as f:
#         text = f.read()

#     lines = text.splitlines()
#     words = text.split()
#     return len(lines) , len(words)



# print(count_lines_words('./data/obama.txt'))
# print(count_lines_words('./data/michelle.txt'))
# print(count_lines_words('./data/trump.txt'))
# print(count_lines_words('./data/melina.txt'))


import json
from collections import Counter

# def most_spoken_language(file_path , limit):
#     with open(file_path , 'r' , encoding='utf-8') as f:
#         data = json.load(f)

#     all_lang =[]
#     for country in data:
#         all_lang.extend(country['languages'])

#     return Counter(all_lang).most_common(limit)


# print(most_spoken_language('./data/countries_data.json' , 10))



def most_populated(file_path , limit):
    with open(file_path , 'r' , encoding='utf-8') as f:
        data = json.load(f)

    sorted_population = sorted(
        data , key=lambda item : item['population'], reverse=True
    )

    return [
        {'country': item['name'] , 'population': item['population'] } for item in sorted_population[:limit]
    ]    


print(most_populated('./data/countries_data.json' , 10))













































 