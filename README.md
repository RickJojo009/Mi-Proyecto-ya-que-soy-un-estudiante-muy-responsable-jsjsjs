#Agenda de Asistencia

Descripción

Agenda de Asistencia es un prototipo desarrollado en Python para gestionar de manera sencilla el registro de asistencia de personas. El programa solicita inicialmente el nombre y el tipo de persona, permitiendo identificar si se trata de un estudiante o un profesor. A través de un menú interactivo, el usuario puede registrar su asistencia, consultar las personas presentes, acceder a opciones para visualizar ausentes y buscar personas, además de salir del sistema. En esta primera versión, el registro de asistencia se realiza únicamente para estudiantes.

Funcionalidades
Marcar asistencia: permite registrar la asistencia de un estudiante.
Identificación del profesor: reconoce cuando la persona ingresada es un profesor y evita registrarlo en la lista de asistencia.
Ver asistencia: muestra la lista de personas que han registrado su asistencia.
Ver ausentes: incluye una opción destinada a consultar las personas ausentes, aunque esta funcionalidad todavía no está implementada.
Buscar personas: 
incluye una opción para buscar personas, aunque esta funcionalidad todavía está pendiente de implementación.
Salir: permite finalizar la ejecución del programa.
Validación básica: muestra mensajes cuando se introduce un tipo de persona u opción de menú no válida.
Cómo ejecutar

Para ejecutar el proyecto se necesita tener Python instalado.

Guardar el código en un archivo con extensión .py, por ejemplo:

asistencia.py

Abrir una terminal en la carpeta donde se encuentra el archivo.

Ejecutar el programa con:

python asistencia.py

Ingresar el nombre y seleccionar el tipo de persona cuando el programa lo solicite.

Utilizar las opciones disponibles en el menú de Agenda de Asistencia.

Tecnologías usadas
Python: lenguaje de programación utilizado para desarrollar el prototipo.
Entrada y salida por consola: se utilizan input() y print() para la interacción con el usuario.
Lista (list): se utiliza la estructura asistencia para almacenar los nombres de los estudiantes que registran su asistencia.
Estructuras de control: se utilizan while, if, elif y else para controlar el funcionamiento del programa.
Método .lower(): se utiliza para convertir el tipo de persona ingresado a minúsculas y facilitar su comparación.
