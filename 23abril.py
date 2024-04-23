import random
print("Hola mundo")
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Añade la longitud de la contraseña:"))
password = ""
for i in range (longitud):
    password += random.choice(elementos)
print(password)
