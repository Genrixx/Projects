num = int(input("Введите число из которого требуется факториал: "))
while True:
    num = int(input("Введите число из которого требуется факториал: "))
    res = 1
    for i in range(1, num):
        res += res * i
        print(res)
        
