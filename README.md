# Agenda de Asistencia

Proyecto desarrollado en Python para gestionar la asistencia de estudiantes y profesores mediante un sistema de menú interactivo en consola.

El programa permite registrar la asistencia, consultar las personas presentes, identificar quiénes están ausentes y buscar personas específicas dentro del sistema.

---

## Funcionalidades

La Agenda de Asistencia cuenta con las siguientes funciones:

* Registrar asistencia de estudiantes.
* Registrar asistencia de profesores.
* Ver estudiantes presentes.
* Ver profesores presentes.
* Ver todas las personas presentes.
* Consultar estudiantes ausentes.
* Consultar profesores ausentes.
* Buscar estudiantes específicos.
* Buscar profesores específicos.
* Buscar una persona dentro de todos los registros.
* Evitar registros duplicados de asistencia.
* Salir correctamente del programa.

---

## Menú principal

Al ejecutar el programa, el usuario encontrará el siguiente menú:

```text
--- Agenda de Asistencia ---

1. Marcar asistencia
2. Ver asistencia
3. Ver ausentes
4. Buscar personas
5. Salir
```

Cada opción cuenta con sus respectivos submenús para facilitar la navegación dentro del programa.

---

## Tecnologías utilizadas

* Python 3
* Listas
* Ciclos `while`
* Ciclos `for`
* Condicionales `if`, `elif` y `else`
* Métodos de listas como `.append()`
* Funciones básicas como `len()` e `input()`

---

## Estructura del programa

El programa maneja diferentes listas para almacenar la información:

### Personas registradas

```python
estudiantes = []
profesores = []
```

### Personas con asistencia registrada

```python
asistencia_estudiantes = []
asistencia_profesores = []
```

Esto permite diferenciar entre las personas registradas y aquellas que han marcado su asistencia.

---

##  Cómo ejecutar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/RickJojo009/Mi-Proyecto-ya-que-soy-un-estudiante-muy-responsable-jsjsjs.git
```

2. Ingresa a la carpeta del proyecto.

3. Ejecuta el archivo utilizando Python:

```bash
python nombre_del_archivo.py
```

> Asegúrate de tener Python 3 instalado en tu computadora.

---

## Ejemplo de uso

El usuario puede seleccionar la opción **Marcar asistencia** y posteriormente indicar si desea registrar a un estudiante o profesor.

El sistema verificará:

* Si la persona existe dentro de los registros.
* Si ya tiene asistencia registrada.
* Si pertenece al grupo de estudiantes o profesores.

Posteriormente, la asistencia podrá ser consultada desde el menú principal.

---

## Posibles mejoras futuras

Este proyecto se encuentra en una etapa inicial y podría incluir futuras mejoras como:

* Guardar la información en archivos.
* Implementar una base de datos.
* Agregar fechas a los registros de asistencia.
* Permitir registrar nuevos estudiantes y profesores.
* Mejorar la validación de datos ingresados.
* Evitar errores cuando el usuario ingrese letras en opciones numéricas.
* Crear una interfaz gráfica.
* Generar reportes de asistencia.

---

##  Autor

**Jehiden Diez Bustamante**

Ficha: **3493204**

Estudiante de **Análisis y Desarrollo de Software - SENA**

---

## Estado del proyecto

En desarrollo / Versión beta.

Este proyecto fue desarrollado con fines académicos como práctica de programación en Python y manejo de estructuras básicas como listas, ciclos y condicionales.

---

> *Proyecto realizado por un estudiante extremadamente responsable y profesional... probablemente.*
