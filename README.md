# Bot de Gestión de Vacaciones por WhatsApp

## Proyecto Integrador

### Autor

Ignacio Evans

## Descripción del Proyecto

Este proyecto consiste en el análisis, modelado y simulación de un asistente virtual para la gestión de solicitudes de vacaciones de empleados mediante WhatsApp.

La propuesta busca optimizar un proceso administrativo tradicional que actualmente requiere correos electrónicos, validaciones manuales y actualización de planillas por parte del personal de Recursos Humanos.

A través de la automatización, el sistema permite que los empleados consulten y soliciten vacaciones de forma autónoma, rápida y segura.

---

## Objetivos

* Automatizar la solicitud de vacaciones.
* Reducir tiempos de respuesta.
* Minimizar errores humanos.
* Mejorar la experiencia del empleado.
* Garantizar el cumplimiento de las reglas de negocio.
* Mantener un registro organizado de las solicitudes.

---

## Proceso Administrativo Modelado

Gestión y Solicitud de Vacaciones Anuales de los Empleados.

El proyecto incluye:

* Análisis del proceso actual (As-Is).
* Diseño del proceso optimizado (To-Be).
* Diagramas BPMN 2.0.
* Diccionario de datos.
* Máquina de estados.
* Manejo de caminos felices e infelices.
* Simulación funcional en Python.

---

## Tecnologías Utilizadas

* Python 3
* BPMN 2.0
* WhatsApp (simulado)
* Diccionarios Python como base de datos simulada
* GitHub para control de versiones

---

## Funcionamiento General

### Validación de Usuario

El sistema verifica si el número de teléfono del empleado se encuentra registrado.

### Consulta de Saldo

Si el usuario es válido, el bot informa la cantidad de días disponibles.

### Solicitud de Vacaciones

El empleado ingresa:

* Cantidad de días solicitados.
* Fecha de inicio.

### Verificación de Reglas de Negocio

El sistema valida:

* Formato correcto de los datos.
* Disponibilidad de días.
* Autorización del usuario.

### Confirmación

Si la solicitud es válida:

* Se actualiza el saldo disponible.
* Se genera un código de trámite.
* Se informa la confirmación al usuario.

---

## Máquina de Estados

El flujo de conversación utiliza los siguientes estados:

START

↓

ESPERANDO_DIAS

↓

ESPERANDO_FECHA

↓

CONFIRMADO

---

## Manejo de Errores

El sistema contempla distintos escenarios:

### Usuario no registrado

Se rechaza el acceso.

### Formato inválido

Si el usuario ingresa texto en lugar de números, el sistema solicita nuevamente el dato.

### Saldo insuficiente

Si la cantidad de días solicitada supera el saldo disponible, la solicitud es rechazada.

---

## Archivos del Repositorio

* README.md
* Proyecto_Integrador.pdf
* bot_vacaciones.py
* Diagrama_AsIs.png
* Diagrama_ToBe.png

---

## Herramientas de Inteligencia Artificial Utilizadas

Durante el desarrollo se utilizó ChatGPT como herramienta de asistencia para:

* Revisión de documentación.
* Elaboración de BPMN.
* Validación de lógica de programación.
* Generación de ejemplos de manejo de errores.
* Redacción de documentación técnica.

---

## Ejecución

1. Instalar Python 3.
2. Descargar el archivo `bot_vacaciones.py`.
3. Abrir una terminal.
4. Ejecutar:

```python
python bot_vacaciones.py
```

5. Seguir las instrucciones mostradas por el sistema.

---

## Conclusión

La automatización propuesta demuestra cómo un chatbot puede optimizar significativamente un proceso administrativo tradicional, reduciendo tiempos operativos, disminuyendo errores humanos y mejorando la experiencia de los empleados mediante una interfaz ampliamente utilizada como WhatsApp.
