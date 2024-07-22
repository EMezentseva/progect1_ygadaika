# проект 1
import random

print("Добро пожаловать в числовую угадайку")
print("Выберите диапазон от 1 до ...")
n = int(input())
print("Введите число от 1 до", n)
num = random.randrange(1, n)


def is_valid(x):
    if x.isdigit() == True:
        if 1 <= int(x) <= n:
            return True
        else:
            return False
    else:
        return False


count = 0
while num:
    x = input()
    if is_valid(x) == False:
        print("А может быть все-таки введем целое число от 1 до ", n, "?", sep="")
        continue

    if True:
        x = int(x)
        count += 1
        if x > num:
            print("Слишком много, попробуйте еще раз")
        if x < num:
            print("Слишком мало, попробуйте еще раз")
        if x == num:
            print("Вы угадали, поздравляем!")
            print("Число попыток:", count)
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
    continue
