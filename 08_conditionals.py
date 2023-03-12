# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442

### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")
    
#Para simular un switch case, que no exite en python usamos if, elif y else, o si es devolver un valor
#un diccionario, ejemplo dias de la semana y frase
# Definir el diccionario

dia = "Viernes"

dias = {
"lunes": "Hoy es lunes y el cuerpo lo sabe.",
"martes": "Hoy es martes y toca trabajar duro.",
"miércoles": "Hoy es miércoles y estamos a mitad de semana.",
"jueves": "Hoy es jueves y ya se siente el fin de semana.",
"viernes": "Hoy es viernes y el cuerpo lo celebra.",
"sábado": "Hoy es sábado y hay que disfrutarlo.",
"domingo": "Hoy es domingo y hay que descansar."
}

print(dias.get(dia.lower(), "No es un día válido."))
