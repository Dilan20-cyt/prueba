'''
Ejercicio 1: Escuela Internacional de Gastronomía
En lugar de while True, inicializamos las variables con un valor inválido (0 o "")
antes de cada while, para obligar a que entre al bucle y solo salga cuando el dato sea válido.
'''


# 1. Validar cantidad de chefs a registrar (entero positivo)
cantidad_chefs = 0
while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("¿Cuántos chefs desea registrar?: "))
        if cantidad_chefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0

# Inicializamos los contadores
chefs_maestros = 0
chefs_aprendices = 0

# 2. Ciclo para registrar a cada chef
for i in range(1, cantidad_chefs + 1):
    print(f"\n--- Registro del Chef #{i} ---")
    
    # Validar Código Culinario (mínimo 8 caracteres y sin espacios)
    codigo = ""
    while len(codigo) < 8 or " " in codigo:
        codigo = input("Ingrese el Código Culinario (mín. 8 caracteres, sin espacios): ")
        if len(codigo) < 8 or " " in codigo:
            print("Error: El código debe tener al menos 8 caracteres y NO contener espacios.")
            
    # Validar Experiencia Culinaria (entero positivo)
    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("Ingrese los años de experiencia culinaria: "))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0
            
    # 3. Clasificación y conteo
    if experiencia > 5:
        chefs_maestros += 1
        print("-> Clasificado como: Chef Maestro")
    else:
        chefs_aprendices += 1
        print("-> Clasificado como: Chef Aprendiz")

# 4. Salida Final
print(f"\n¡La escuela cuenta con {chefs_maestros} Chefs Maestros y {chefs_aprendices} Chefs Aprendices! ¡A cocinar!")

'''cantidad_chefs = 0 antes del while cantidad_chefs <= 0:: Como 0 <= 0 es verdadero,
entra sí o sí la primera vez. Si el usuario escribe letras, salta al except:,
imprime el error y deja cantidad_chefs = 0 para que vuelva a repetir.
Si escribe un número positivo (ej: 3), 3 <= 0 es falso y sale solo del bucle.

while len(codigo) < 8 or " " in codigo:: El bucle se repite mientras el código sea muy corto
(menos de 8 letras) O tenga un espacio adentro. Apenas cumpla ambas cosas, sale solo.'''



'''Ejercicio 2: Sistema de Camarotes del Crucero Atlántico
Aquí controlamos el menú principal con opcion = 0 y while opcion != 5:'''

# Variables iniciales del sistema
CAPACIDAD_MAXIMA = 120
disponibles = 120
historial_reservas = 0
opcion = 0

print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

# Bucle principal del menú (se repite mientras la opción no sea 5)
while opcion != 5:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles.")
    print("2.- Reservar camarote.")
    print("3.- Cancelar camarote.")
    print("4.- Historial de reservas.")
    print("5.- Salir.")
    
    # Validar que la opción del menú sea un número
    try:
        opcion = int(input("\nSeleccione una opción (1-5): "))
    except:
        print("Error: Debe ingresar un número del 1 al 5.")
        opcion = 0

    # Opción 1: Mostrar disponibles
    if opcion == 1:
        print(f"Camarotes disponibles actualmente: {disponibles}")

    # Opción 2: Reservar camarotes
    elif opcion == 2:
        try:
            cant_reservar = int(input("Ingrese la cantidad de camarotes a reservar: "))
            if cant_reservar <= 0:
                print("Error: La cantidad a reservar debe ser mayor a 0.")
            elif cant_reservar > disponibles:
                print(f"Error: No hay suficiente capacidad. Solo quedan {disponibles} camarotes disponibles.")
            else:
                disponibles -= cant_reservar
                historial_reservas += cant_reservar
                print(f"¡Reserva exitosa! Se han reservado {cant_reservar} camarotes.")
        except:
            print("Error: Debe ingresar un número entero válido.")

    # Opción 3: Cancelar camarotes
    elif opcion == 3:
        try:
            cant_cancelar = int(input("Ingrese la cantidad de camarotes a cancelar: "))
            if cant_cancelar <= 0:
                print("Error: La cantidad a cancelar debe ser mayor a 0.")
            elif (disponibles + cant_cancelar) > CAPACIDAD_MAXIMA:
                print(f"Error: No puede superar la capacidad máxima del crucero ({CAPACIDAD_MAXIMA} camarotes).")
            else:
                disponibles += cant_cancelar
                historial_reservas -= cant_cancelar
                print(f"Cancelación exitosa. Se han liberado {cant_cancelar} camarotes.")
        except:
            print("Error: Debe ingresar un número entero válido.")

    # Opción 4: Historial de reservas
    elif opcion == 4:
        print(f"Total de camarotes reservados actualmente en esta sesión: {historial_reservas}")

    # Opción 5: Salir del sistema
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")

    # Si ingresó un número fuera de rango (y no fue 0 por el except)
    elif opcion != 0:
        print("Opción no válida. Por favor, elija una opción entre 1 y 5.")

'''Cuando el usuario escribe letras en el menú (ej: "abc"),
entra al except:, muestra el mensaje de error y pone opcion = 0

Al final pusimos elif opcion != 0: para que,
si ya mostró el error del except:  , 
no te muestre dos mensajes de error seguidos en la misma vuelta.
Si el usuario escribe 9, como 9 != 0, ahí sí le dice "Opción no válida".
'''
