print('Что сложить?')


def add_everything_up1(*args):
    try:
        summa = sum(args)
        return summa
    except TypeError:
        print('Внесите числа, чтобы их сложить:)')


print(add_everything_up1(123.456, 'строка'))
print(add_everything_up1('яблоко', 4215))
print(add_everything_up1(123.456, 7))


print('***********************')
def add_everything_up2(a, b):
    try:
        summa = sum(a, b)
        return summa
    except TypeError:
        print('Введите числа, чтобы их сложить:)')


print(add_everything_up2(123.456, 'строка'))
print(add_everything_up2('яблоко', 4215))
print(add_everything_up2(123.456, 7))

print('***********************')
def add_everything_up3(a, b):
    try:
        summa = a + b
        return summa
    except TypeError:
        print(a, b)


print(add_everything_up3(123.456, 'строка'))
print(add_everything_up3('яблоко', 4215))
print(add_everything_up3(123.456, 7))



