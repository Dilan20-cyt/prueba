'''
Tip 1: Validar longitud mínima de un texto
tamanio = "HolaHola"
print("El numero de la variable es: ", len(tamanio))

if len(tamanio) > 11:
    print("Ingreso correcto")
else:
    print("Ingreso debe ser al menos de 12 caracteres")

len(tamanio) cuenta cuántos caracteres tiene la variable,
en este caso, "HolaHola" tiene 8 letras

La condición > 11 (mayor a 11) es igual a decir "mínimo 12",
 como 8 no es mayor a 11, se ejecuta el bloque else
 
Tip 2: Obligar al usuario a ingresar un entero positivo

numero = int(input("Ingrese un numero: "))

while numero <= 0:
    print("Dato de investigación inválido! Ingresa un entero positivo")
    numero = int(input("Ingrese un numero: "))
    
Pide un número y lo convierte a entero con int()
Si el usuario escribe 0 o un número negativo (como -5),
entra al while y le vuelve a pedir el dato.
El bucle solo se rompe cuando el usuario ingresa un número positivo (1, 2, 3..)
numero = int(input("Ingrese un numero: ")) 
esta linea de codigo esta para que despues del error vuelva a preguntar por el numero
sin que se caiga el programa

Tip 3: Manejo de errores (try / except)

opcion = 0

while opcion == 0:
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Ha ocurrido un error: debe ingresar un número entero.")
        opcion = 0

try: ("Intenta esto"): Ponemos dentro el código peligroso (el int(input(...)))
que puede ocasionar caida del programa
except: ("Si falla, haz esto"): Si el usuario escribe "abc",
en lugar de cerrar el programa, ejecuta lo que esté dentro del except,
imprimiendo el mensaje de alerta y manteniendo opcion = 0 para reintentar.

Tip 4: Limpieza de espacios en blanco (strip vs replace)

# Caso A: strip() quita espacios al inicio y al final únicamente
palabra_con_espacios = "    hola mundo    "
print(palabra_con_espacios.strip())  # Imprime: "hola mundo"

# Caso B: replace() reemplaza TODOS los espacios por nada
palabra = "   b h a   "
palabra = palabra.replace(" ", "")
print(palabra)       # Imprime: "bha"
print(len(palabra))  # Imprime: 3

strip(): Ideal para limpiar lo que escribe un usuario por error al principio o al final
replace(" ", ""): Busca cualquier espacio dentro del texto (incluso al medio) y lo elimina

Tip 5: Controlar el tamaño máximo de una lista con un bucle infinito

lista = ["1", "2", "3", "4", "5", "6", "7", "8"]

while len(lista) < 10:  # El bucle se detiene automáticamente al llegar a 10 elementos
    variable = input("Ingrese un elemento: ")
    lista.append(variable)
    print("Ingresado exitosamente")
    print("Lista actual:", lista)

print("La lista ha alcanzado su límite máximo (10 elementos).")

La variable lista comienza con 8 elementos: ["1", "2", "3", "4", "5", "6", "7", "8"]
len(lista) vale 8, la Condición del Bucle while len(lista) < 10:

"¿La cantidad de elementos de la lista es menor a 10?"Como $8 < 10$ es Verdadero,
el programa entra al bucle

Iteración 1: Pide un elemento (ejemplo: "9"). Con lista.append("9"),
lo agrega al final, la lista ahora tiene 9 elementos

Iteración 2: Como 9 < 10 sigue siendo Verdadero, vuelve a pedir otro elemento
En la siguiente vuelta,
evalúa la condición de nuevo: "¿Es 10 < 10?" Como 10 no es menor que 10,
la condición se vuelve falsa, el bucle termina de inmediato y el programa avanza
a la última línea: imprime (muestra en pantalla) 
"La lista ha alcanzado su límite máximo (10 elementos)
'''

#Validar un número entero positivo (mayor a 0)

numero = 0                      # 1. Arranca en 0 para obligar a entrar al while
while numero <= 0:              # 2. Mientras sea 0 o negativo, repite
    try:
        numero = int(input("Ingrese un número positivo: "))
        if numero <= 0:
            print("Error: Debe ser mayor a 0.")
    except:
        print("Error: Ingrese solo números.")
        numero = 0              # 3. Si escribió letras, resetea a 0 para no salir

#Validar texto (largo mínimo y sin espacios)

texto = ""                      # 1. Arranca vacío para entrar al while
while len(texto) < 8 or " " in texto:   # 2. Pon la condición contraria (lo que NO quieres)
    texto = input("Ingrese el código: ")
    if len(texto) < 8 or " " in texto:
        print("Error: Mínimo 8 caracteres y sin espacios.")

#Menú de opciones repetitivo

opcion = 0                      # 1. Arranca en 0
while opcion != 5:              # 2. Cambia el 5 por el número de "Salir"
    print("\n1.- Opción A")
    print("2.- Opción B")
    print("5.- Salir")
    
    try:
        opcion = int(input("Elija una opción: "))
    except:
        print("Error: Ingrese un número.")
        opcion = 0              # 3. Resetea a 0 si puso letras

    if opcion == 1:
        # Código opción 1
        pass
    elif opcion == 2:
        # Código opción 2
        pass
    elif opcion == 5:
        print("Saliendo...")
    elif opcion != 0:           # 4. Evita doble error cuando cae en except
        print("Opción fuera de rango.")

#Contadores y Acumuladores (en ciclos for)

contador = 0                    # Siempre nace en 0 ANTES del ciclo

for i in range(1, cantidad + 1):
    # Pides los datos aquí adentro...
    if condicion_cumplida:
        contador += 1           # Suma 1 cada vez que se cumple (contador)
        # suma += valor         # Suma el valor ingresado (acumulador)

print("Total:", contador)       # Se imprime DESPUÉS (fuera) del ciclo



variable = input("ingrese un texto: ")

if len(variable) >= 8:
    print("Tamaño texto correcto")
else:
    print("Tamaño texto debe ser mayor o igual a 8")

#variable = " H O L A "
#print(len(variable.strip()))

variable = "   H    O  L A "
variable = variable.replace(" ", "")
print(len(variable))  # Devuelve 4
print(variable)       # Imprime "HOLA"




variable = 0
while variable == 0:
    try:
        variable = int(input("Ingrese el texto"))
    except:
        print("Ha ocurrido un error")
        variable = 0


lista = [1, 2, 3, 4, 5]
while True:
    variable = int(input("Ingrese un elemento numérico: \n"))
    if len(lista) < 15:
        lista.append(variable)
        print(lista)


try:
    variable = int(input("Ingrese un número"))
except:
    print("Ha ocurrido un error")  


# Contadores y Acumuladores (en ciclos for)

contador = 0
suma = 0

# 1. Definimos "cantidad" pidiéndola al usuario
cantidad = int(input("¿Cuántos números vas a ingresar?: "))

# 2. Ahora "cantidad" sí existe para el for
for i in range(1, cantidad + 1):
    valor = int(input(f"Ingresa el número #{i}: "))
    
    # 3. Reemplazamos "condicion_cumplida" por una condición real (ej: mayores a 10)
    if valor > 10:
        contador += 1       # Cuenta cuántos fueron mayores a 10
        suma += valor       # Suma los valores de esos números mayores a 10

print("Cantidad de números mayores a 10:", contador)
print("Suma total de esos números:", suma)