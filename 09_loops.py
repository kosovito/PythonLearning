# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional y pertenece al while
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")
    
#mostramos key y value en un solo for

for key, value in my_dict.items():
    print(f"{key} - {value}")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
    
#simular un for clásico de otros lenguajes

for i in range(10):
    print(i)
    
#ahora incluimos condición más compleja

for i in range(10):
    if i % 2 == 0: # Si el número es divisible entre 2
        print(i)

#incluimos saltos en el iterador
for i in range(0, 10, 2):
    print(i)