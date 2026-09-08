
#=========================#
# Jehiden Diez Bustamante #
#      Ficha 3493204      #
#=========================#


#==============================================#
#              AGENDA DE ASISTENCIA             #
#==============================================#
# El programa permite:
# - Marcar asistencia.
# - Ver personas presentes.
# - Ver personas ausentes.
# - Buscar estudiantes o profesores.
#==============================================#


# Lista de estudiantes registrados inicialmente.
estudiantes = ["Miguel", "Paulo", "Valdez", "Milton", "Jesus", "Santiago"]

# Lista de profesores registrados inicialmente.
profesores = ["Victor", "Nestor"]


# Estas listas comienzan vacías y almacenarán únicamente
# las personas que hayan registrado su asistencia.
asistencia_estudiantes = []
asistencia_profesores = []


# Ciclo principal del programa.
# while True mantiene el menú funcionando indefinidamente
# hasta que el usuario seleccione la opción de salir.
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

        # Submenú para seleccionar qué tipo de persona
        # desea registrar.
        while True:

            print("\n--- Marcar asistencia ---")
            print("1. Estudiante")
            print("2. Profesor")
            print("3. Volver")

            opcion_asistencia = int(input("Seleccione una opcion: "))
            print()


            #-----------#
            # ESTUDIANTE
            #-----------#

            if opcion_asistencia == 1:

                nombre = input("Ingrese el nombre del estudiante: ")

                # Primero verificamos que el estudiante exista
                # dentro de la lista de estudiantes registrados.
                if nombre in estudiantes:

                    # Se verifica que el estudiante todavía no haya
                    # registrado asistencia para evitar duplicados.
                    if nombre not in asistencia_estudiantes:

                        # append() agrega el nombre al final de la lista.
                        asistencia_estudiantes.append(nombre)

                        print("Asistencia del estudiante registrada.")

                    else:
                        print("Este estudiante ya tiene asistencia registrada.")

                else:
                    print("El estudiante no se encuentra registrado.")


            #-----------#
            # PROFESOR
            #-----------#

            elif opcion_asistencia == 2:

                nombre = input("Ingrese el nombre del profesor: ")

                # Verificamos que el profesor exista en los registros.
                if nombre in profesores:

                    # Evitamos que una misma persona registre
                    # asistencia más de una vez.
                    if nombre not in asistencia_profesores:

                        asistencia_profesores.append(nombre)

                        print("Asistencia del profesor registrada.")

                    else:
                        print("Este profesor ya tiene asistencia registrada.")

                else:
                    print("El profesor no se encuentra registrado.")


            #-----------#
            # VOLVER
            #-----------#

            elif opcion_asistencia == 3:

                print("Volviendo al menú principal...")

                # break finaliza únicamente este while,
                # permitiendo regresar al menú principal.
                break


            else:
                print("Opcion no valida.")


    #================================#
    #        2. VER ASISTENCIA
    #================================#

    elif opcion == 2:

        # Submenú para consultar las diferentes asistencias.
        while True:

            print("\n--- Ver asistencia ---")
            print("1. Estudiantes presentes")
            print("2. Profesores presentes")
            print("3. Todos los presentes")
            print("4. Volver")

            opcion_ver = int(input("Seleccione una opcion: "))
            print()


            #--------------------------#
            # VER ESTUDIANTES PRESENTES
            #--------------------------#

            if opcion_ver == 1:

                print("--- Estudiantes presentes ---")

                # len() cuenta la cantidad de elementos de una lista.
                # Si la lista tiene 0 elementos significa que nadie
                # ha registrado asistencia.
                if len(asistencia_estudiantes) == 0:

                    print("No hay estudiantes presentes.")

                else:

                    # Recorremos la lista mostrando cada estudiante.
                    for estudiante in asistencia_estudiantes:

                        print(estudiante)


            #--------------------------#
            # VER PROFESORES PRESENTES
            #--------------------------#

            elif opcion_ver == 2:

                print("--- Profesores presentes ---")

                if len(asistencia_profesores) == 0:

                    print("No hay profesores presentes.")

                else:

                    # Mostramos cada profesor que haya registrado asistencia.
                    for profesor in asistencia_profesores:

                        print(profesor)


            #--------------------------#
            # VER TODOS LOS PRESENTES
            #--------------------------#

            elif opcion_ver == 3:

                print("--- Personas presentes ---")

                # Se revisan ambas listas. Si las dos están vacías,
                # significa que ninguna persona ha registrado asistencia.
                if len(asistencia_estudiantes) == 0 and len(asistencia_profesores) == 0:

                    print("No hay personas presentes.")

                else:

                    print("\nEstudiantes:")

                    # Mostramos todos los estudiantes presentes.
                    for estudiante in asistencia_estudiantes:

                        print(estudiante)

                    print("\nProfesores:")

                    # Mostramos todos los profesores presentes.
                    for profesor in asistencia_profesores:

                        print(profesor)


            #-----------#
            # VOLVER
            #-----------#

            elif opcion_ver == 4:

                print("Volviendo al menú principal...")

                # Sale del submenú de asistencia.
                break


            else:
                print("Opcion no valida.")


    #================================#
    #          3. AUSENTES
    #================================#

    elif opcion == 3:

        print("--- Personas ausentes ---")

        print("\nEstudiantes ausentes:")

        # Variable bandera.
        # Nos permite saber si durante el recorrido encontramos
        # al menos una persona ausente.
        hay_ausentes = False


        # Recorremos todos los estudiantes registrados.
        for estudiante in estudiantes:

            # Si el estudiante NO está dentro de la lista de asistencia,
            # significa que está ausente.
            if estudiante not in asistencia_estudiantes:

                print(estudiante)

                # Cambiamos la variable a True porque encontramos
                # al menos una persona ausente.
                hay_ausentes = True


        # Si después de recorrer toda la lista la variable sigue
        # siendo False, significa que todos asistieron.
        if not hay_ausentes:

            print("No hay estudiantes ausentes.")


        print("\nProfesores ausentes:")

        # Reiniciamos la variable porque ahora se utilizará
        # para revisar a los profesores.
        hay_ausentes = False


        # Recorremos todos los profesores registrados.
        for profesor in profesores:

            # Si el profesor no aparece en la lista de asistencia,
            # significa que está ausente.
            if profesor not in asistencia_profesores:

                print(profesor)

                hay_ausentes = True


        # Si nunca se encontró un profesor ausente,
        # todos los profesores están presentes.
        if not hay_ausentes:

            print("No hay profesores ausentes.")


    #================================#
    #        4. BUSCAR PERSONAS
    #================================#

    elif opcion == 4:

        # Submenú para realizar diferentes tipos de búsqueda.
        while True:

            print("\n--- Buscar personas ---")
            print("1. Buscar estudiante")
            print("2. Buscar profesor")
            print("3. Buscar en todos")
            print("4. Volver")

            opcion_buscar = int(input("Seleccione una opcion: "))
            print()


            #----------------#
            # BUSCAR ESTUDIANTE
            #----------------#

            if opcion_buscar == 1:

                nombre = input("Ingrese el nombre del estudiante: ")

                # Primero verificamos si existe.
                if nombre in estudiantes:

                    # Después verificamos si registró asistencia.
                    if nombre in asistencia_estudiantes:

                        print(nombre, "está presente.")

                    else:

                        print(nombre, "está ausente.")

                else:

                    print("Estudiante no encontrado.")


            #----------------#
            # BUSCAR PROFESOR
            #----------------#

            elif opcion_buscar == 2:

                nombre = input("Ingrese el nombre del profesor: ")

                if nombre in profesores:

                    if nombre in asistencia_profesores:

                        print(nombre, "está presente.")

                    else:

                        print(nombre, "está ausente.")

                else:

                    print("Profesor no encontrado.")


            #----------------#
            # BUSCAR EN TODOS
            #----------------#

            elif opcion_buscar == 3:

                nombre = input("Ingrese el nombre que desea buscar: ")


                # Primero verificamos si pertenece al grupo
                # de estudiantes.
                if nombre in estudiantes:

                    if nombre in asistencia_estudiantes:

                        print(nombre, "es estudiante y está presente.")

                    else:

                        print(nombre, "es estudiante y está ausente.")


                # Si no es estudiante, verificamos si pertenece
                # al grupo de profesores.
                elif nombre in profesores:

                    if nombre in asistencia_profesores:

                        print(nombre, "es profesor y está presente.")

                    else:

                        print(nombre, "es profesor y está ausente.")


                # Si no pertenece a ninguna lista,
                # la persona no está registrada.
                else:

                    print("Persona no encontrada.")


            #-----------#
            # VOLVER
            #-----------#

            elif opcion_buscar == 4:

                print("Volviendo al menú principal...")

                # Finaliza el ciclo del submenú de búsqueda.
                break


            else:

                print("Opcion no valida.")


    #================================#
    #              5. SALIR
    #================================#

    elif opcion == 5:

        print("Saliendo de la Agenda de Asistencia...")

        # break termina el while principal,
        # finalizando completamente el programa.
        break


    # Si el usuario ingresa un número diferente
    # a las opciones disponibles.
    else:

        print("Opcion no valida.")

