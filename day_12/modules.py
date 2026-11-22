import random
import string

def random_user_id():
    char = string.ascii_letters + string.digits
    
    return ''.join(random.choices(char , k = 6))


print(random_user_id())


def user_id_gen_by_user():
    i1 = int(input())
    i2 = int(input())
    char = string.ascii_letters + string.digits
    
    for i in range(0 , i2):
        print(''.join(random.choices(char , k = i1)))

user_id_gen_by_user()


def rgb_color_gen():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)

    print(f"rgb({r} , {g} , {b})")


rgb_color_gen()


def list_of_hexa(n):
    hex_chars = '0123456789abcdef'
    colors = []
    for _ in range(n):
        color = '#'+''.join(random.choices(hex_chars , k=6))
        colors.append(color)
        
    return colors

print(list_of_hexa(3))

def list_of_rgb_colors(n):
   
    colors = []
    for _ in range(n):
         r = random.randint(0 , 255)
         g = random.randint(0 , 255)
         b = random.randint(0 , 255)
        
         colors.append(f"{r} , {g} , {b}")

    return colors


print(list_of_rgb_colors(3))



def generate_colors(type , times):

    if type == 'hexa':
        hex_chars = '0123456789abcdef'
        hex_list =[]
        for _ in range(times):
            color = '#' +''.join(random.choices(hex_chars , k = 6))
            hex_list.append(color)
        return hex_list
    elif type == 'rgb':
        rgb_list = []
        for _ in range(times):
            r = random.randint(0 , 255)
            g = random.randint(0 , 255)
            b = random.randint(0 , 255)
            rgb_list.append(f"rgb({r} , {g} , {b})")
        return rgb_list
        

print(generate_colors('rgb' , 3))



def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1 , 2 , 3 , 4]))



def random_nums():
    return random.sample(range(10) , 7)

print(random_nums())









