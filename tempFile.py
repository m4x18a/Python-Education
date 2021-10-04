def print_products(*args):
    count = 1
    for c in args:
        if type(c) == str and len(c) > 0:
            print(count, ') ', c, sep='')
            count += 1

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)