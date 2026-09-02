#=========================#
# Jehiden Diez Bustamante #
#      Ficha 3493204      #
#=========================#

#=========================#
#Agenda de Asistencia#
#Marca asistencia, ver asistencia, ver ausentes, buscar personas, salir#
#=========================#

#=========================#
# Agenda de Asistencia
# Marca asistencia, ver asistencia, ver ausentes,
# buscar personas, salir
#=========================#

estudiantes = ["Miguel", "Paulo", "Valdez", "Milton", "Jesus", "Santiago".lower()]
profesores = ["Victor", "Nestor".lower()]

asistencia_estudiantes = []
asistencia_profesores = []


while True:

    print("\n--- Agenda de Asistencia ---")
    print("1. Marcar asistencia")
    print("2. Ver asistencia")
    print("3. Ver ausentes")
    print("4. Buscar personas")
    print("5. Salir")

    opcion = int(input("Seleccione una opcion: "))
    print()


    #================================#
    #      1. MARCAR ASISTENCIA
    #================================#

    if opcion == 1:

        while True:

            print("\n--- Marcar asistencia ---")
            print("1. Estudiante")
            print("2. Profesor")
            print("3. Volver")

            opcion_asistencia = int(input("Seleccione una opcion: "))
            print()

            if opcion_asistencia == 1:

                nombre = input("Ingrese el nombre del estudiante: ")

                if nombre in estudiantes:

                    if nombre not in asistencia_estudiantes:
                        asistencia_estudiantes.append(nombre)
                        print("Asistencia del estudiante registrada.")
                    else:
                        print("Este estudiante ya tiene asistencia registrada.")

                else:
                    print("El estudiante no se encuentra registrado.")


            elif opcion_asistencia == 2:

                nombre = input("Ingrese el nombre del profesor: ")

                if nombre in profesores:

                    if nombre not in asistencia_profesores:
                        asistencia_profesores.append(nombre)
                        print("Asistencia del profesor registrada.")
                    else:
                        print("Este profesor ya tiene asistencia registrada.")

                else:
                    print("El profesor no se encuentra registrado.")


            elif opcion_asistencia == 3:

                print("Volviendo al menú principal...")
                break


            else:

                print("Opcion no valida.")


    #================================#
    #        2. VER ASISTENCIA
    #================================#

    elif opcion == 2:

        while True:

            print("\n--- Ver asistencia ---")
            print("1. Estudiantes presentes")
            print("2. Profesores presentes")
            print("3. Todos los presentes")
            print("4. Volver")

            opcion_ver = int(input("Seleccione una opcion: "))
            print()

            if opcion_ver == 1:

                print("--- Estudiantes presentes ---")

                if len(asistencia_estudiantes) == 0:
                    print("No hay estudiantes presentes.")
                else:
                    for estudiante in asistencia_estudiantes:
                        print(estudiante)


            elif opcion_ver == 2:

                print("--- Profesores presentes ---")

                if len(asistencia_profesores) == 0:
                    print("No hay profesores presentes.")
                else:
                    for profesor in asistencia_profesores:
                        print(profesor)


            elif opcion_ver == 3:

                print("--- Personas presentes ---")

                if len(asistencia_estudiantes) == 0 and len(asistencia_profesores) == 0:
                    print("No hay personas presentes.")
                else:

                    print("\nEstudiantes:")

                    for estudiante in asistencia_estudiantes:
                        print(estudiante)

                    print("\nProfesores:")

                    for profesor in asistencia_profesores:
                        print(profesor)


            elif opcion_ver == 4:

                print("Volviendo al menú principal...")
                break


            else:

                print("Opcion no valida.")


    #================================#
    #          3. AUSENTES
    #================================#

    elif opcion == 3:

        print("--- Personas ausentes ---")

        print("\nEstudiantes ausentes:")

        hay_ausentes = False

        for estudiante in estudiantes:

            if estudiante not in asistencia_estudiantes:
                print(estudiante)
                hay_ausentes = True

        if not hay_ausentes:
            print("No hay estudiantes ausentes.")


        print("\nProfesores ausentes:")

        hay_ausentes = False

        for profesor in profesores:

            if profesor not in asistencia_profesores:
                print(profesor)
                hay_ausentes = True

        if not hay_ausentes:
            print("No hay profesores ausentes.")


    #================================#
    #        4. BUSCAR PERSONAS
    #================================#

    elif opcion == 4:

        while True:

            print("\n--- Buscar personas ---")
            print("1. Buscar estudiante")
            print("2. Buscar profesor")
            print("3. Buscar en todos")
            print("4. Volver")

            opcion_buscar = int(input("Seleccione una opcion: "))
            print()

            if opcion_buscar == 1:

                nombre = input("Ingrese el nombre del estudiante: ")

                if nombre in estudiantes:

                    if nombre in asistencia_estudiantes:
                        print(nombre, "está presente.")
                    else:
                        print(nombre, "está ausente.")

                else:
                    print("Estudiante no encontrado.")


            elif opcion_buscar == 2:

                nombre = input("Ingrese el nombre del profesor: ")

                if nombre in profesores:

                    if nombre in asistencia_profesores:
                        print(nombre, "está presente.")
                    else:
                        print(nombre, "está ausente.")

                else:
                    print("Profesor no encontrado.")


            elif opcion_buscar == 3:

                nombre = input("Ingrese el nombre que desea buscar: ")

                if nombre in estudiantes:

                    if nombre in asistencia_estudiantes:
                        print(nombre, "es estudiante y está presente.")
                    else:
                        print(nombre, "es estudiante y está ausente.")

                elif nombre in profesores:

                    if nombre in asistencia_profesores:
                        print(nombre, "es profesor y está presente.")
                    else:
                        print(nombre, "es profesor y está ausente.")

                else:
                    print("Persona no encontrada.")


            elif opcion_buscar == 4:

                print("Volviendo al menú principal...")
                break


            else:

                print("Opcion no valida.")


    #================================#
    #              5. SALIR
    #================================#

    elif opcion == 5:

        print("Saliendo de la Agenda de Asistencia...")
        break


    else:

        print("Opcion no valida.")
