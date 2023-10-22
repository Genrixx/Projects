slovo = input("Введите слово: ")
for b in slovo:
    prov = slovo[::-1]

if prov == slovo:
    print("{0} - ваше слово, {1} - оно наоборот".format(slovo, prov))
    print("Это слово палендрома")
else:
    print("{0} - ваше слово, {1} - оно наоборот".format(slovo, prov))
    print("Это слово не палендрома")