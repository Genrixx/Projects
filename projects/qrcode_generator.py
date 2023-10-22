import qrcode

text = input("Введите ссылку: ")
img = qrcode.make(text)
img.save("qrcode.png")
