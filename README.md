# Generador de Base de Datos Eléctrica y Configuración de Git

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Configuración del Entorno](#configuración-del-entorno)
3. [Código Python y MySQL](#código-python-y-mysql)
4. [Configuración de Git](#configuración-de-git)

## Descripción del Proyecto
Este proyecto genera una base de datos MySQL con mediciones eléctricas aleatorias, incluyendo:
- Voltage (118V - 225V)
- Corriente (30A - 40A)
- Potencia (calculada como V * A)

## Configuración del Entorno

### Requisitos Previos
1. Python 3.x instalado
2. MySQL Server instalado
3. Conector MySQL para Python

### Instalación de Dependencias
```bash
pip install mysql-connector-python
```

## Código Python y MySQL

### Estructura de la Base de Datos
```sql
CREATE TABLE mediciones_electricas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voltage FLOAT,
    corriente FLOAT,
    potencia FLOAT
)
```

### Explicación del Código Python

#### 1. Configuración de la Conexión
```python
db_config = {
    'host': 'localhost',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'database': 'nombre_base_datos'
}
```
Esta sección define los parámetros de conexión a MySQL.

#### 2. Creación de la Base de Datos
```python
def crear_base_datos():
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
```
Establece la conexión inicial con MySQL.

#### 3. Generación de Datos
```python
for _ in range(1000):
    voltage = round(random.uniform(118, 225), 2)
    corriente = round(random.uniform(30, 40), 2)
    potencia = round(voltage * corriente, 2)
```
- Genera 1000 registros aleatorios
- Usa `random.uniform()` para números decimales
- Redondea a 2 decimales con `round()`

#### 4. Inserción en la Base de Datos
```python
cursor.execute("""
    INSERT INTO mediciones_electricas (voltage, corriente, potencia)
    VALUES (%s, %s, %s)
""", (voltage, corriente, potencia))
```
Inserta cada registro en la tabla usando consultas preparadas.

## Configuración de Git

### Configuración Inicial
Para comenzar a usar Git, necesitas configurar tu información básica:

```bash
git config --global user.name "TuNombreDeUsuario"
git config --global user.email "tuemail@ejemplo.com"
```

### Verificación
```bash
git config --global user.name    # Muestra el nombre configurado
git config --global user.email   # Muestra el email configurado
```

### Componentes del Comando
- `git config`: Comando base para configuración
- `--global`: Aplica la configuración a todos los proyectos
- `user.name`: Variable para el nombre de usuario
- `user.email`: Variable para el correo electrónico

### Ejemplo Práctico
```bash
git config --global user.name "Maria Gonzalez"
git config --global user.email "maria@gmail.com"
```

## Flujo de Trabajo Típico

1. Configura Git con tu email y username
2. Clona o inicia el repositorio
3. Ejecuta el script Python para generar la base de datos
4. Verifica los datos generados
5. Realiza commits de los cambios en el código

## Solución de Problemas Comunes

### Problemas con MySQL
1. Error de conexión
   - Verifica que MySQL esté corriendo
   - Confirma las credenciales
   - Revisa el firewall

2. Error de permisos
   - Asegura que el usuario tenga permisos CREATE y INSERT
   - Verifica los permisos de la base de datos

### Problemas con Git
1. Error en formato de email
   - Usa un email válido con @
   - Evita espacios

2. Error en nombre de usuario
   - Evita caracteres especiales
   - Mantén las comillas si hay espacios

## Referencias y Recursos
- [Documentación de MySQL](https://dev.mysql.com/doc/)
- [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- [Documentación de Git](https://git-scm.com/doc)
