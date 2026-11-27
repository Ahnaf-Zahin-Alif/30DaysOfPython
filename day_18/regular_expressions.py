import re
from collections import Counter
import keyword
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r"\b\w+\b" , paragraph)            

word_counter = [
    (count , word) for word , count in Counter(words).most_common()
]

print(word_counter)


text = ( "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction." )


points = re.findall(r"-?\d+" , text)
sorted_points = sorted(int(p) for p in points)

distance = sorted_points[-1] - sorted_points[0]

print('Points: ' , sorted_points)
print('Distance: ' , distance)



def is_valid_variable(name: str) ->bool:
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern , name)) and not keyword.iskeyword(name)


print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') 


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z\s]" , "" , text)
    return re.sub(r"\s+" , " " , cleaned).strip()


def most_frequent_words(text: str , top_n: int = 3) -> list[tuple[int , str]]:
    words = text.split()
    return [(count , word) for word , count in Counter(words).most_common(top_n)]


clean_text = clean_text(sentence)
print(clean_text)
print(most_frequent_words(clean_text))






























