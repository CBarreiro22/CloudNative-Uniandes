# proyecto-202314  

```bash
.
├── config.yaml
├── docker-compose.yml
├── k8s-autoscale.yml
├── k8s-base-layer-deployment.yaml
├── k8s-ingress-deloyment.yaml
├── k8s-new-services-deployment.yaml
├── LICENSE
├── offers
│   ├── Dockerfile
│   ├── file.py
│   ├── __init__.py
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   ├── __init__.py
│   │   │   ├── offer.py
│   │   │   └── __pycache__
│   │   │       ├── __init__.cpython-310.pyc
│   │   │       └── offer.cpython-310.pyc
│   │   ├── commands
│   │   │   ├── base_command.py
│   │   │   ├── __init__.py
│   │   │   ├── offersOperations.py
│   │   │   ├── offers.py
│   │   │   ├── __pycache__
│   │   │   │   ├── base_command.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── offers.cpython-310.pyc
│   │   │   │   ├── offersOperations.cpython-310.pyc
│   │   │   │   └── userService.cpython-310.pyc
│   │   │   └── userService.py
│   │   ├── errors
│   │   │   ├── errors.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── errors.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   ├── offer.py
│   │   │   └── __pycache__
│   │   │       ├── __init__.cpython-310.pyc
│   │   │       ├── model.cpython-310.pyc
│   │   │       └── offer.cpython-310.pyc
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   └── tests
│       ├── blueprint
│       │   ├── test_Offer.py
│       │   └── test_user_mock_service.py
│       ├── commands
│       │   └── __init__.py
│       ├── conftest.py
│       └── __init__.py
├── Pipfile
├── posts
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   └── operations.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   └── user_service.py
│   │   ├── errors
│   │   │   ├── errors.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── models
│   │       ├── __init__.py
│   │       ├── model.py
│   │       └── post.py
│   └── tests
│       ├── blueprints
│       │   ├── test_operations.py
│       │   └── test_user_service.py
│       ├── conftest.py
│       └── __init__.py
├── README.md
├── requirements.txt
├── RF-003
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   └── rf003.py
│   │   ├── commands
│   │   │   ├── BaseCommand.py
│   │   │   ├── __init__.py
│   │   │   ├── PostService.py
│   │   │   └── RoutesService.py
│   │   ├── erros
│   │   │   ├── errors.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── tests
│       ├── blueprints
│       │   ├── test_create_route_request.py
│       │   ├── test_ping.py
│       │   ├── test_post_service.py
│       │   ├── test_rf003_post.py
│       │   ├── test_routes_service.py
│       │   ├── test_schema_validations.py
│       │   └── test_validate_dates.py
│       ├── conftest.py
│       └── __init__.py
├── RF-004
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   └── operations.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── offer_service.py
│   │   │   ├── post_service.py
│   │   │   ├── score_service.py
│   │   │   └── user_service.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── models
│   │       ├── __init__.py
│   │       ├── model.py
│   │       └── post.py
│   └── tests
│       ├── blueprints
│       │   ├── test_offer_service.py
│       │   ├── test_operations.py
│       │   ├── test_post_service.py
│       │   ├── test_score_service.py
│       │   └── test_user_service.py
│       ├── conftest.py
│       └── __init__.py
├── RF-005
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   ├── __init__.py
│   │   │   └── operations.py
│   │   ├── errors
│   │   │   ├── errors.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── tests
│       ├── blueprints
│       │   └── test_rf005_operations.py
│       ├── conftest.py
│       └── __init__.py
├── routes
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   ├── __init__.py
│   │   │   ├── operations.py
│   │   │   └── __pycache__
│   │   │       ├── __init__.cpython-310.pyc
│   │   │       └── operations.cpython-310.pyc
│   │   ├── errors
│   │   │   ├── errors.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── errors.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── model.cpython-310.pyc
│   │   │   │   └── route.cpython-310.pyc
│   │   │   └── route.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   └── tests
│       ├── blueprints
│       │   └── test_routes_operations.py
│       ├── conftest.py
│       └── __init__.py
├── scores
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── src
│   │   ├── blueprints
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── scoreOperation.cpython-310.pyc
│   │   │   │   └── user.cpython-310.pyc
│   │   │   └── scoreOperation.py
│   │   ├── errors
│   │   │   ├── errors.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── errors.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── model.cpython-310.pyc
│   │   │   │   └── score.cpython-310.pyc
│   │   │   └── score.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   └── tests
│       ├── blueprint
│       │   ├── __init__.py
│       │   └── test_scores.py
│       ├── conftest.py
│       └── __init__.py
├── secrets.yaml
└── users
    ├── Dockerfile
    ├── file.py
    ├── __init__.py
    ├── k8s-service.yml
    ├── __pycache__
    │   └── __init__.cpython-310.pyc
    ├── README.md
    ├── requirements.txt
    ├── src
    │   ├── blueprints
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   └── user.cpython-310.pyc
    │   │   └── user.py
    │   ├── errors
    │   │   ├── errors.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── errors.cpython-310.pyc
    │   │       └── __init__.cpython-310.pyc
    │   ├── __init__.py
    │   ├── main.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── model.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── model.cpython-310.pyc
    │   │   │   └── user.cpython-310.pyc
    │   │   └── user.py
    │   └── __pycache__
    │       ├── __init__.cpython-310.pyc
    │       └── main.cpython-310.pyc
    └── tests
        ├── blueprint
        │   └── test_users.py
        ├── conftest.py
        └── __init__.py
```


## Tabla de contenido

- [Pre-requisitos para cada microservicio](#pre-requisitos-para-cada-microservicio)
- [Estructura de cada microservicio](#estructura-de-cada-microservicio)
  - [Archivos de soporte](#archivos-de-soporte)
  - [Carpeta src](#carpeta-src)
  - [Carpeta test](#carpeta-test)
- [Ejecutar un microservicio](#ejecutar-un-microservicio)
  - [Instalar dependencias](#instalar-dependencias)
  - [Variables de entorno](#variables-de-entorno)
  - [Ejecutar el servidor](#ejecutar-el-servidor)
  - [Ejecutar pruebas](#ejecutar-pruebas)
  - [Ejecutar desde Dockerfile](#ejecutar-desde-dockerfile)
- [Ejecutar Docker Compose](#ejecutar-docker-compose)
- [Ejecutar Colección de Postman](#ejecutar-colección-de-postman)
- [Ejecutar evaluador github action workflow](#ejecutar-evaluador-github-action-workflow)
- [Ejecucion de Kubernet en cloud](#ejecucion-de-Kubernet-en-cloud)
- [Consumo Postman con el ingress](#consumo-Postman-con-el-ingress)

## Pre-requisitos para cada microservicio
- Python ~3.10
- pipenv
    - Ejecuta `pip install pipenv` para instalarlo
- Docker
- Docker-compose
- Postman
- PostgreSQL
    - Las instrucciones pueden variar según el sistema operativo. Consulta [la documentación](https://www.postgresql.org/download/). Si estás utilizando un sistema operativo basado en Unix, recomendamos usar [Brew](https://wiki.postgresql.org/wiki/Homebrew).

## Estructura de cada microservicio
Cada microservicio utiliza Python y Flask para ejecutar el servidor, y pytest para ejecutar las pruebas unitarias. En general, dentro de cada uno de ellos hay dos carpetas principales: `src` y `tests`, así como algunos archivos de soporte.

### Archivos de soporte
- `Pipfile`: Este archivo declara todas las dependencias que serán utilizadas por el microservicio. Consulta la sección **Instalar dependencias**.
- `.env.template`: Archivo de plantilla Env utilizado para definir variables de entorno. Consulte la sección  **Variables de entorno**.
- `.env.test`: Archivo utilizado para definir variables de entorno para las pruebas unitarias. Consulta la sección **Variables de entorno**.
- Dockerfile: Definición para construir la imagen Docker del microservicio. Consulta la sección **Ejecutar desde Dockerfile**.

### Carpeta src
Esta carpeta contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio, así como para la comunicación con la base de datos. Hay 4 carpetas principales:
- `/models`: Esta carpeta contiene la capa de persistencia, donde se declaran los modelos que se van a persistir en la base de datos en forma de tablas, así como la definición de cada columna. Incluimos un archivo `model.py` que contiene un modelo base llamado `Model`, que realiza la configuración básica de una tabla e incluye las columnas `createdAt` y `updatedAt` por defecto para que puedas utilizarlo. Para crear un nuevo modelo en un archivo separado, solo necesitas extender esta clase `Model`. Por ejemplo:
```python
# /models/car.py
from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, Integer
from .model  import  Model, Base

# Extender la clase Model proporcionada
class Car(Model, Base):
	__tablename__  =  'cars'
	price  =  Column(Integer)
	name  =  Column(String)

# Constructor
def  __init__(self, price, name):
	Model.__init__(self)
	self.price  =  price
	self.name  =  name

# Especificar los campos que estarán presentes al serializar el objeto como JSON.
class  CarJsonSchema(Schema):
	id  = fields.Number()
	price  = fields.Number()
	name  = fields.Str()
	createdAt  = fields.DateTime()
	updatedAt  = fields.DateTime()
```
- `/commands`: Esta carpeta contiene cada caso de uso que estamos implementando en nuestro microservicio, es decir, la lógica del negocio siguiendo un patrón de diseño de comandos. Para cada caso de uso (como crear un automóvil, modificar un automóvil, vender un automóvil, etc.) tendremos un archivo separado. Cada comando heredará una clase `BaseCommand` que ya está proporcionada en el archivo `/commands/base_command.py` e implementará el método `execute`. Este método es el que contendrá la lógica del negocio. Por ejemplo, si estamos implementando un comando para sumar dos números, declararíamos una clase de comando `SumTwoNumbers` con la siguiente implementación:
```python
# /commands/sum_two_numbers.py
from .base_command  import  BaseCommand

class  SumTwoNumbers(BaseCommannd):
	def  __init__(self, first_numer, second_number):
		self.first_number = first_number
		self.second_number = second_number

	def  execute(self):
		return self.first_number + self.second_number
```
Después de declararlo, podemos utilizar el caso de uso importándolo y llamando al método execute.

```python
from ..commands.sum_two_numbers  import  SumTwoNumbers

def example():
	result = SumTwoNumbers(5, 2).execute()
	print(result) # This prints 7
```

- `/blueprints`: Esta carpeta contiene la capa de aplicación de nuestro microservicio, responsable de declarar cada servicio API que estamos exponiendo, así como su implementación. Por ejemplo, para declarar un simple HTTP GET con la ruta `/calculator/sum` utilizando el comando declarado anteriormente, deberíamos seguir los siguientes pasos:
1. Crear el archivo de blueprint `/blueprints/calculator.py`
2. Implementar la ruta GET
```python
from flask import Flask, jsonify, request, Blueprint
from ..commands.sum_two_numbers  import  SumTwoNumbers

calculator_blueprint  = Blueprint('calculator', __name__)

@calculator_blueprint.route('/sum', methods  = ['GET'])
def sum():
	params = request.args.to_dict()
	result = SumTwoNumbers(params["first_number"], params["second_number"]).execute()
	return jsonify({ 'result': result })
```
3. Por último, modifica `main.py` en la raíz de la carpeta del microservicio para utilizar este nuevo blueprint.
```python
...
from .blueprints.calculator  import  calculator_blueprint

app  = Flask(__name__)
app.register_blueprint(calculator_blueprint)
...
```

- `/errors`: Para devolver errores HTTP en los blueprints, utilizamos clases de excepción personalizadas que declaran qué mensaje y qué código HTTP retornar cuando ocurre esa excepción. Estas excepciones se declaran dentro del archivo `/errors/errors.py`, donde se proporciona una clase base `ApiError`. Para declarar una nueva excepción personalizada, declara una nueva clase que extienda `ApiError`, de la siguiente manera:
```python
class  InvalidParams(ApiError):
	code  =  400
	description  =  "Bad param"
```
Ahora, cada vez que el servidor Flask esté en ejecución y levantes la excepción `InvalidParams`, el usuario recibirá un código HTTP 400 con el mensaje "Bad param". Esta excepción puede ser lanzada a nivel del blueprint o del comando, y Flask traducirá esta excepción al resultado HTTP correspondiente.
```python
# /commands/sum_two_numbers.py
from .base_command  import  BaseCommand
from ..errors.errors  import  InvalidParams

class  SumTwoNumbers(BaseCommannd):
	def  __init__(self, first_numer, second_number):
		self.first_number = first_number
		self.second_number = second_number

	def  execute(self):
		if self.first_number == 0 or self.second_number == 0:
			raise InvalidParams()
		
		return self.first_number + self.second_number
```
Si te preguntas cómo Flask es capaz de traducir una clase de excepción a JSON HTTP, es gracias a un middleware de manejo de errores proporcionado por la biblioteca de Flask y utilizado en el archivo `main.py`.
```python
@app.errorhandler(ApiError)
def  handle_exception(err):
	response  = {
		"msg": err.description
	}
	return jsonify(response), err.code
``` 

### Carpeta test
Esta carpeta contiene las pruebas para los componentes principales del microservicio que han sido declarados en la carpeta `/src`

## Ejecutar un microservicio
### Instalar dependencias
Utilizamos pipenv para gestionar las dependencias (verificar la sección de requisitos previos) y las declaramos todas dentro del archivo Pipfile del microservicio. Antes de instalar las dependencias, inicia el shell de pipenv para activar el entorno virtual con el siguiente comando:

```bash
$> pipenv shell
``` 
Luego ejecuta el comando de instalación.
```bash
$> pipenv install
```
Esto instalará las dependencias solo dentro del entorno virtual, así que recuerda activarlo cuando estés trabajando con el microservicio. Para obtener más información sobre pipenv, consulta la documentación oficial en https://pipenv-es.readthedocs.io.

Para salir del entorno virtual, utiliza el siguiente comando:
```bash
$> deactivate
```

### Variables de entorno

El servidor Flask y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:
- DB_USER: Usuario de la base de datos Postgres
- DB_PASSWORD: Contraseña de la base de datos Postgres
- DB_HOST: Host de la base de datos Postgres
- DB_PORT: Puerto de la base de datos Postgres
- DB_NAME: Nombre de la base de datos Postgres
- USERS_PATH: Para los microservicios que se comunican con el microservicio de Usuarios, necesitas especificar esta variable de entorno que contiene la URL utilizada para acceder a los endpoints de usuarios. (Ejemplo: http://localhost:3000, http://users-service)

Estas variables de entorno deben especificarse en `.env.development` y `.env.test`. El segundo archivo ya está provisto para ti, pero el primero debe crearse basado en la plantilla `.env.template` en la raíz de la carpeta del microservicio.

Como se mencionó anteriormente, tenemos dos archivos de entorno dentro de la carpeta del microservicio:
- `.env.template`
Este archivo contiene una plantilla de la estructura que el archivo `.env.development` utilizado por el servidor Flask requiere para funcionar.
- `.env.test`
Este es el archivo de entorno utilizado por pytest para ejecutar las pruebas unitarias.

### Ejecutar el servidor
Una vez que las variables de entorno estén configuradas correctamente, para ejecutar el servidor utiliza el siguiente comando:
```bash
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p <PORT_TO_RUN_SERVER>

# Ejemplos

# Users
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000

# Posts
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3001

# Routes
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3002

# Offers
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3003

# Scores
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3004

# RF-005
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3005

# RF-003
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3006

# RF-004
$> FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3007
```
### Ejecutar pruebas
Para ejecutar las pruebas unitarias de los microservicios y establecer el porcentaje mínimo de cobertura del conjunto de pruebas en 70%, ejecuta el siguiente comando:
```bash
pytest --cov-fail-under=70 --cov=src
pytest --cov-fail-under=70 --cov=src --cov-report=html
```
### Ejecutar desde Dockerfile
Para construir la imagen del Dockerfile en la carpeta, ejecuta el siguiente comando:
```bash
$> docker build . -t <NOMBRE_DE_LA_IMAGEN>
```
Y para ejecutar esta imagen construida, utiliza el siguiente comando:
```bash
$> docker run <NOMBRE_DE_LA_IMAGEN>
```

## Ejecutar Docker Compose
Para ejecutar todos los microservicios al mismo tiempo, utilizamos docker-compose para declarar y configurar cada Dockerfile de los microservicios. Para ejecutar docker-compose, utiliza el siguiente comando:
```bash
$> docker-compose -f "<RUTA_DEL_ARCHIVO_DOCKER_COMPOSE>" up --build

# Ejemplo
$> docker-compose -f "docker-compose.yml" up --build
```

## Ejecutar Colección de Postman
Para probar los servicios API expuestos por cada microservicio, hemos proporcionado una lista de colecciones de Postman que puedes ejecutar localmente descargando cada archivo JSON de colección e importándolo en Postman.

Lista de colecciones de Postman para cada entrega del proyecto:
- Entrega 1: https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/monitor-202314/main/entrega1/entrega1.json
- Entrega 2: https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/monitor-202314/main/entrega2/entrega2_verify_new_logic.json
- Entrega 3: Para esta entrega no tenemos un workflow evaluador, por lo que no se proporciona ninguna colección de Postman.

Después de descargar la colección que deseas usar, impórtala en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

Una vez importada la colección, actualiza las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/efafbb3d-5938-4bd8-bfc7-6becfccd2682" alt="Screenshot" width="800">

Finalmente, ejecuta la colección haciendo clic derecho en su nombre y haciendo clic en el botón "Run collection", esto ejecutará múltiples solicitudes API y también ejecutará algunos assertions que hemos preparado para asegurarnos de que el microservicio esté funcionando como se espera.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/f5ca6f7c-e4f4-4209-a949-dcf3a6dab9e3" alt="Screenshot" width="800">

## Ejecutar evaluador github action workflow

Para las entregas 1 y 2, hemos proporcionado un evaluador automático que ejecutará validaciones en los servicios API expuestos en cada entrega. Este evaluador se ejecuta como un workflow de Github Actions en el repositorio. Para ejecutar el workflow, ve a la sección de "Actions" del repositorio que se encuentra en la parte superior.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/92d686b7-21b1-42b1-b23a-e8c3d626dfd3" alt="Screenshot" width="800">

Luego, encontrarás en la sección izquierda una lista de todos los flujos de trabajo (workflows) disponibles para ejecución. En este caso, verás "Evaluator_Entrega1" y "Evaluator_Entrega2", correspondientes a los evaluadores de las dos primeras entregas. Haz clic en el que deseas ejecutar. Verás un botón "Run workflow" en la sección superior derecha, haz clic en este botón, selecciona la rama en la que deseas ejecutarlo y haz clic en el botón "Run workflow".

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/4bcf1c0d-e422-4f9d-9ff6-a663f8248352" alt="Screenshot" width="800">

Esto iniciará la ejecución del workflow en la rama. Si todo funciona correctamente y la entrega es correcta, verás que todas las comprobaciones aparecen como aprobadas (passed).

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/c6c580b2-80e0-411d-8971-a252312ce5ea" alt="Screenshot" width="800">

## Ejecucion de Kubernet en cloud

Para el desarrollo de la segunda entrega se realizó lo que fue el despliegue en Cloud implementando kubernet.
1. Auténtica con google cloud de acuerdo al proyecto
2. Autoriza a gcloud con el registry
> gcloud auth configure-docker us-central1-docker.pkg.dev

3. Luego de haberte generado el Cluster con sus respectivas redes y subred procedemos a construir las imagenes con lo siguiente:
>docker build -t us-central1-docker.pkg.dev/{{ProyectID}}/{{KubernetName}}/{{NombreDelServicio}}:{{Version}} .

Ejemplo:
>docker build -t us-central1-docker.pkg.dev/secure-guru-383402/uniandes-containers-app/score:1.0 .\n

4. Luego de haber construido las imagenes procedemos a subirlas al repositorio de google cloud con el siguiente comando:
>docker push -t us-central1-docker.pkg.dev/{{proyectID}}/{{ClusterKubernateName}}/{{NomnbreDelMicro}}:{{Version}}

Ejemplo:
>docker push -t us-central1-docker.pkg.dev/secure-guru-383402/uniandes-containers-app/score:1.0

5. Luego de haber subido las imagenes al repositorio de google cloud procedemos a crear los deployments con el siguiente comando:

Despliegue solo los microservicios (user, post, routes, offers)
>kubectl apply -f k8s-base-layer-deployment.yaml

Despliegue de los microservicios (RF-003, RF-004, RF-005,SCORE)
> kubectl apply -f k8s-new-layer-service.yaml

Despligue del ingress
> kubectl apply -f k8s-ingress-deloyment.yaml

## Consumo Postman con el ingress

Se procede abrir el postman que de la entrega 2 mencionadas en este readme tal y como se muestra a continuación y se selecciona variables:

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/6ccc4139-f917-4acb-a8a2-b6390a65258b)

Y se modifica el INGRESS_PATH que en nuestro caso es el 34.117.67.117

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/9c907057-2caa-4480-b9d4-e7629a266d47)

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/314c4279-f6da-423e-80ad-3eb1862a2d3d)


Y luego se relaiza las pruebas de la siguiente manera

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/64cd2e07-6fb6-49f3-88a4-494917347a43)

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/aad19010-903a-439f-b8cc-020dbd72b444)

Finalmente, debe aparece algo como esto:
![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/assets/111206402/64314851-0114-4e80-b348-9dfdbe90e1ca)

Version v1.0.5
