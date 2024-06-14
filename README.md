# Examen Final
## Programación Web III - MVC API RESTful

### Antes de Empezar:

1. Realiza un **Fork** de este repositorio:

![Repositorio Examen Final](https://live.staticflickr.com/65535/53786372843_49b3358b74_z.jpg)

1. Si vas a trabajar en tu equipo local clona el nuevo repositorio resultado del **Fork** y ábrelo con **VSCode** o el editor de tu preferencia para trabajar tu solución. También puedes trabajar tu solución en **GitHub Codespaces**.

2. Completa tus datos personales en la siguiente tabla:
    | Nombre   | Apellido   | CI   |
    | -------- | ---------- | ---- |
    | `Ariel` | `Quizaya Callisaya` | `6814344` |

3. Realiza un commit de esta modificación y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "datos actualizados"
    git push origin main
    ```
4. En la terminal ejecuta el siguiente comando para instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Contexto:
Eres el **Back-End Developer** de una StartUp que está desarrollando una plataforma para **reservar mesas en restaurantes** en Bolivia. Debes desarrollar una **API MVC RESTful** que permita administrar la información de los restaurantes, las reservas y los usuarios de la plataforma.

En **Base de Datos** se debe almacenar los siguientes datos de los Restaurantes:
- id: Identificador único del restaurante. De tipo **entero y autoincremental**.
- name: Nombre del restaurante. De tipo  **cadena de texto**.
- address: Dirección del restaurante. De tipo  **cadena de texto**.
- city: Ciudad del restaurante. De tipo  **cadena de texto**.
- phone: Número de teléfono del restaurante. De tipo  **cadena de texto**.
- description: Descripción del restaurante. De tipo  **cadena de texto**.
- rating: Calificación promedio del restaurante. De tipo **decimal**.

Se debe almacenar en **Base de Datos** los siguientes datos de las Reservas:
- id: Identificador único de la reserva. De tipo **entero y autoincremental**.
- user_id: Identificador único del usuario que realiza la reserva. De tipo  **entero**.
- restaurant_id: Identificador único del restaurante para la reserva. De tipo  **entero**.
- reservation_date: Fecha y hora de la reserva. De tipo datetime.
- num_guests: Número de invitados. De tipo  **entero**.
- special_requests: Solicitudes especiales del usuario. De tipo  **cadena de texto**.
- status: Estado de la reserva (p.ej., pendiente, confirmada, cancelada). De tipo  **cadena de texto**.

Se debe almacenar en **Base de Datos** los siguientes datos de los Usuarios:
- id: Identificador único del usuario. De tipo **entero y autoincremental**.
- name: Nombre del usuario. De tipo  **cadena de texto**.
- email: Correo electrónico del usuario. De tipo  **cadena de texto**.
- password: Contraseña del usuario. De tipo  **cadena de texto**.
- phone: Número de teléfono del usuario. De tipo  **cadena de texto**.
- role: Rol del usuario (`admin`, `customer`). De tipo  **cadena de texto**.

Existe un usuario con el rol de administrador (`admin`) que puede realizar las siguientes acciones:
- **Listar los restaurantes**: Listar todos los restaurantes registrados en el sistema.
- **Mostrar un restaurante**: Mostrar la información de un restaurante específico.
- **Crear un restaurante**: Crear un nuevo restaurante en el sistema.
- **Actualizar un restaurante**: Actualizar la información de un restaurante existente.
- **Eliminar un restaurante**: Eliminar un restaurante existente.
- **Listar las reservas**: Listar todas las reservas realizadas en el sistema.
- **Mostrar una reserva**: Mostrar la información de una reserva específica.
- **Crear una reserva**: Crear una nueva reserva en el sistema.
- **Actualizar una reserva**: Actualizar la información de una reserva existente.
- **Eliminar una reserva**: Eliminar una reserva existente.

Existen usuarios con el rol cliente (`customer`) que puede realizar las siguientes acciones:
- **Listar los restaurantes**: Listar todos los restaurantes registrados en el sistema.
- **Mostrar un restaurante**: Mostrar la información de un restaurante específico.
- **Listar sus propias reservas**: Listar todas las reservas realizadas por el usuario.
- **Mostrar una de sus reservas**: Mostrar la información de una reserva específica realizada por el usuario.
- **Crear una reserva**: Crear una nueva reserva en el sistema.
- **Actualizar una de sus reservas**: Actualizar la información de una reserva existente realizada por el usuario.
- **Eliminar una de sus reservas**: Eliminar una reserva existente realizada por el usuario.

### Tareas:
- Construye una **API MVC RESTful** que permita realizar las **operaciones CRUD** sobre los restaurantes, las reservas y los usuarios de la plataforma.
- Implementa **autenticación con JWT** para que los usuario puedan acceder a los recursos de la **API**.
- Los usuarios deben poder **cerrar sesión** en la API para **invalidar el token de autenticación**.
- Implementa **autorización por roles** para que los usuarios de tipo `admin` y `customer` puedan realizar las acciones listadas previamente.
- La **API** que construyas debe pasar todos los **test** que se encuentran en `app/test`
- Integra la documentación con **Swagger** del documento `app/static/swagger.json`
- Automatiza la ejecución de los **test** de la carpeta `app/test` implementando **GitHub Actions** en el repositorio de tu solución.

### Rutas y resultados esperados:
- Revisa el documento `app/static/swagger.json` para conocer las rutas y los resultados esperados de la **API**.
- Revisa los **test** que debe pasar tu solución en la carpeta `app/test` para conocer las rutas y los resultados esperados de la **API**.

Restricciones:
1. Debes utilizar **Python** como lenguaje de programación.
2. Debes utilizar el framework **Flask** para el desarrollo de la **API**.
3. Debes utilizar **SQLAlchemy** como ORM para la conexión con la **Base de Datos**.
4. Debes utilizar **SQLite** como motor de **Base de Datos**.
5. Debes utilizar **Swagger** para documentar la **API**.
6. Debes utilizar **JWT** para la autenticación de los usuarios.
7. Las respuestas de la **API** deben ser en formato **JSON**.
8. Debes utilizar el patrón de diseño **MVC** para la estructura de tu proyecto.
9. Debes manejar los errores y excepciones que puedan ocurrir en la **API** con los códigos de estado **HTTP** correspondientes.
10. Debes automatizar la ejecución de los **Test** cada vez que se realice un commit en el repositorio de tu solución usando **GitHub Actions**.

Entrega:
1. La estructura de carpetas de tu solución debe estar dentro de la carpeta app
2. Una vez tengas tu solución debes realizar un **commit** y un Push a tu repositorio en GitHub ejecutando los siguientes comandos desde la terminal de tu equipo local o desde GitHub Codespaces:
    ```bash 
    git add .
    git commit -m "Entrega Final"
    git push origin main
    ```
3. Una vez completado el paso anterior adjunta la **URL** de tu repositorio de **GitHub** en la tarea asignada en **Google Classroom**. 

### Enlaces Permitidos
Durante el examen solo puede consultar los siguientes recursos:
- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Documentación de SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Documentación de Flask Login](https://flask-login.readthedocs.io/en/latest/)
- [Documentación de JWT](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Documentación de SQLite](https://www.sqlite.org/docs.html)
- [Documentación de Swagger](https://swagger.io/docs/)
- [Documentación de GitHub Actions](https://docs.github.com/en/actions)

### Comandos Útiles
- Windows:
``` bash
$env:PYTHONPATH="<la ruta de tu proyecto>"
```
- Linux:
```bash
export PYTHONPATH=$(pwd)
```
