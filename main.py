#=========================#
# Jehiden Diez Bustamante #
#      Ficha 3493204      #
#=========================#

#=========================#
#Agenda de Asistencia#
#Marca asistencia, ver asistencia, ver ausentes, buscar personas, salir#
#=========================#

asistencia = []

nombre = input("Ingrese su nombre: ")
tipo = input("¿Eres estudiante o profesor?: ").lower()

while True:
    print("\n--- Agenda de Asistencia ---")
    print("1. Marcar asistencia")
    print("2. Ver asistencia")
    print("3. Ver ausentes")
    print("4. Buscar personas")
    print("5. Salir")

    opcion = int(input("Seleccione una opcion: "))
    print("\n")

    if opcion == 1:

        if tipo == "estudiante":
            asistencia.append(nombre)
            print("Asistencia registrada.")

        elif tipo == "profesor":
            print("Profesor identificado. No se registra en asistencia.")

        else:
            print("Tipo de persona no valido.")

    elif opcion == 2:
        print("\nPersonas presentes:")

        for persona in asistencia:
            print(persona)

    elif opcion == 3:
        print("\nPersonas ausentes:")

    elif opcion == 4:
        print("Buscar personas")

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("Opcion no valida")
