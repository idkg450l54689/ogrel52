
import random

# все символы
symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# длину пароля
password_len = int(input("Введи длиину пароля "))

# сгенерированный пароль
password = ""

# выбирай случайный символ из переменной с символами и добавляй его в переменную с сгенерированным паролем
for i in range(password_len):
    password += random.choice(symbol)

# Выведи получившийся пароль на консоль
print(password)