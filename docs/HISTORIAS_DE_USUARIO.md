# Historias de usuario – AgendaFácil (módulo de citas)

Cada historia se implementa en su propia rama y se une a `main` con un pull request que cierra su issue.
El tipo de mantenimiento sigue las categorías del SWEBOK.

| ID | Historia | Tipo de mantenimiento | Rama | Issue |
| --- | --- | --- | --- | --- |
| HU-01 | Evitar cruce de horarios | Correctivo | `hu-01-cruce-horarios` | #1 |
| HU-02 | Cancelar una cita | Perfectivo | `hu-02-cancelar-cita` | #2 |
| HU-03 | Filtrar citas por fecha | Perfectivo | `hu-03-filtro-fecha` | #3 |
| HU-04 | Autorización de datos (Ley 1581) | Adaptativo | `hu-04-autorizacion-datos` | #4 |
| HU-05 | Pruebas automáticas | Preventivo | `hu-05-pruebas` | #5 |

---

## HU-01 – Evitar cruce de horarios

**Como** recepcionista, **quiero** que el sistema no deje agendar dos citas en la misma fecha y hora, **para** evitar cruces de horario.

- [ ] Si ya hay una cita activa en esa fecha y hora, el formulario muestra un mensaje de error y no guarda.

## HU-02 – Cancelar una cita

**Como** recepcionista, **quiero** cancelar una cita, **para** liberar ese horario.

- [ ] La lista muestra el estado de cada cita (Activa o Cancelada).
- [ ] Las citas activas tienen un botón "Cancelar".
- [ ] Una cita cancelada deja libre su horario.

## HU-03 – Filtrar citas por fecha

**Como** recepcionista, **quiero** filtrar las citas por fecha, **para** ver rápido la agenda del día.

- [ ] La lista tiene un campo de fecha y un botón "Filtrar".
- [ ] El enlace "Ver todas" quita el filtro.

## HU-04 – Autorización de tratamiento de datos

**Como** negocio, **quiero** que el cliente autorice el tratamiento de sus datos al pedir una cita, **para** cumplir la Ley 1581 de 2012.

- [ ] El formulario tiene una casilla de autorización obligatoria.
- [ ] La autorización queda guardada en la cita.

## HU-05 – Pruebas automáticas

**Como** desarrollador, **quiero** pruebas automáticas de las reglas de las citas, **para** detectar errores antes de que lleguen a los usuarios.

- [ ] Hay pruebas para crear, cancelar y filtrar citas, para el cruce de horarios y para la autorización de datos.
- [ ] Todas pasan con `python manage.py test`.
