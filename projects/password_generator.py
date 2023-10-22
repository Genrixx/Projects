import random
run = True
num = "1234567890qwertyuiopasdfghjklzxcvbnm<>/?!@#$%^&*~"
easy = 5
medium = 12
hard = 16
print('*' * 5 + "Генератор паролей" + '*' * 5)
print("Введите h для помощи по командам")
help = str(input())
if help == "h":
    print("""               Меню помощи
            easy - легкий пароль состоящий из 5 символов
            medium - средний пароль состоящий из 12 символов
            hard - сложный пароль состоящий из 16 символов
                """)
number = input("Введите  колличество паролей: ")
length = input("Введите сложность паролей: ")
number = int(number)
length = str(length)
fp = open('C://Users//Андрей//Desktop//password.txt','w')
if length == "easy":
    for n in range(number):
        password =''
        for i in range(easy):
            password += random.choice(num)
        fp.write(password + "\n")
    fp.close()



if length == "medium":
    for n in range(number):
        password =''
        for i in range(medium):
            password += random.choice(num)
        fp.write(password + "\n")
    fp.close()





if length == "hard":
    for n in range(number):
        password =''
        for i in range(hard):
            password += random.choice(num)
        fp.write(password + "\n")
    fp.close()




