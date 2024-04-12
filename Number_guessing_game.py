import random
choice = 'да'
print('Добро пожаловать в числовую угадайку')
while choice == 'да':    
    def is_number(x):
        if x.isdigit():
            return True
        else:
            return False
    while True:
        max_num = input('Введите верхнюю границу целого числа: ')
        if is_number(max_num) == False:
            print('Укажите верхнюю границу числа только цифрами')
        else:
            max_num = int(max_num)
            break
        
    num = random.randint(1, max_num)    
    def is_valid(a):
        if a.isdigit():
            if 1 <= int(a) <= max_num:
                return True
            else: 
                return False
        else:
            return False
    cnt = 0        
    while True:
        n = input('Введите целое число от 1 до указанной Вами верхней границы: ')
        if is_valid(n) == False:
            print('А может быть все-таки введем целое число от 1 до указанной Вами верхней границы?')
        else:
            n = int(n)
            if n == num:
                cnt += 1
                print('Вы угадали c', cnt, 'раза, поздравляем!')                
                break
            elif n < num:
                cnt += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > num:
                cnt += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
    choice = input('Если Вы хотите начать заново, введите да: ')
    if choice != 'да':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')