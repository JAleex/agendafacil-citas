# AgendaFácil – Prototipo del módulo de citas

Prototipo sencillo del módulo de citas de AgendaFácil S.A.S (empresa ficticia), hecho para el taller de Git y GitHub de Mantenimiento de Software.
Permite registrar citas (cliente, teléfono, servicio, fecha y hora) y ver la lista de citas agendadas.

Tecnologías: Python 3.10 o superior, Django 5.2 y SQLite.

## Cómo ejecutarlo (Windows, desde Git Bash)

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir http://127.0.0.1:8000/ en el navegador.

Desde CMD, el entorno virtual se activa con `venv\Scripts\activate`.

## Historias de usuario

Ver [docs/HISTORIAS_DE_USUARIO.md](docs/HISTORIAS_DE_USUARIO.md).
