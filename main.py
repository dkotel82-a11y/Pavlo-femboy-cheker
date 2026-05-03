from random import*
Ima = input('Введіть ваше імя')
vik = input('Введіть ваш вік')
print(f'Привіт {Ima}, тобі {vik} ')
in1 = input('Тепер вгадай число від 1 до 10')
in2 = randint(1, 10)
if in1 == in2 :
    print('вгадав')
else :
    print(f'не вгадав твоє число:{in2}')
