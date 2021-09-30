# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 8.

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
answer = []
for i in range(len(users)):
    if users[i]['phone'].endswith('8'):
        answer.append(users[i]['name'])
answer.sort()
print(*answer)

# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
mylist = []
for i in range(len(users)):
    if 'email' not in users[i].keys() or users[i]['email'] == '':
        mylist.append(users[i]['name'])
mylist = sorted(mylist)
print(*mylist)

# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

mydict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
n = input()
for c in n:
    print(mydict[c], end=' ')

# Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '']
n = input()
morse_dict = dict(zip(letters, morse))
for c in n:
    if c.isalnum():
        print(morse_dict[c.upper()], end=' ')

# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
mylist = s.split()
mylist1 = []
mydict = {}
for word in mylist:
    mydict[word] = mydict.get(word, 0) + 1
maxx = max(mydict.values())
for key, value in mydict.items():
    if value == maxx:
        mylist1.append(key)
mylist1.sort()
print(mylist1[0])

"""Вам доступен список pets, содержащий информацию о собаках и их владельцах.  
Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут перечислены его собаки. 
Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек собак (сохранив исходный порядок следования)."""

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
result = {}
for set_1 in pets:
    result.setdefault((set_1[1:]), []).append(set_1[0])
print(result)