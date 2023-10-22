import random
cards = [6, 7, 8, 9, 10, 11, 2, 3, 4] * 4
random.shuffle(cards)
print('*' * 5 + "БлэкДжэк" +'*' * 5)
game = True
count = 0
while game:
    choice = input("Будете брать карту y/n?: ")
    if choice == "y":
        curent = cards.pop()
        print("Вам выпала карта %d" %curent)
        count += curent
        if count > 21:
            print("Вы проиграли(")
            count = 0
            
        elif count == 21:
            print("Поздравляю у вас 21 очко!!")
            game = False
        else:
            print("У вас %d очков" %count)
    elif choice == "n":
        print("У вас %d очков, всего доброго" %count)
        game = False
        