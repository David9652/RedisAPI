# Redis API

Se implementó una cola de mensajes utilizando **Redis** (un almacén de estructura de datos en memoria, que se emplea como una base de datos distribuida de valores clave en memoria), la cual podrá ser manejada por una *API, construida en **Python* y *Flask, que está conformada por diferentes endpoints como **LPOP, **RPOP, **LPUSH, **RPUSH, **COUNT* y *LRANGE. Es importante aclarar que estos cuentan con diferentes parámetros que permitirán enviar y remover mensajes en masa de la cabeza o cola, escoger la lista y la base de datos sobre la cual se realizará la transacción y muchas más acciones que se detallarán a lo largo del documento. Además, se realizó el endpoint **STATUS* para consultar el estado de salud de *Redis, el cual puede ser usado para obtener información general o específica de algún componente como los clientes conectados, el servidor, uso de la memoria, entre otros. Por último, se hicieron pruebas unitarias y de integración por medio de la librería **unittest* de *Python* donde se podrá escoger cuál funcionalidad de la aplicación se desea ejecutar o si es necesario probar todos los conjuntos de casos.

## Instalación

1. Debe clonar el [proyecto](https://github.com/David9652/RedisAPI.git) siguiendo estas [instrucciones](https://docs.github.com/es/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 
2. Una vez clonado, debe asegurarse de tener instalado una versión de [Python](https://www.python.org/downloads/) superior a la 3.4+ o 2.7.9+. De lo contrario, tendrás que instalar pip por aparte.
3. En caso de no tener instalado el paquete *virtualenv*, debes instalarlo de la siguiente forma:
bash
$ pip install virtualenv

4. El siguiente paso es ejecutar el archivo *start* desde *git bash* o alguna consola que acepte comandos de la familia *UNIX. Es importante aclarar que es necesario verificar el contenido del archivo para determinar si la ruta del ambiente virtual corresponde a **Windows* o *UNIX* en caso de que sea necesario cambiarla.
bash
$ ./start

5. Después de haber instalado todas las dependencias, asegúrese de comentar todas las líneas del archivo con excepción de las que configuran las variables de entorno de Flask y la que ejecuta la aplicación.

6. Si tiene un computador con sistema operativo *Windows, puede iniciar el servicio de **Redis* que está dentro de la carpeta */redis_server. De lo contrario, tendrá que [instalarlo](https://redis.io/download) y copiar la configuración del archivo **redis.windows.conf*.
bash
$./redis-server.exe redis.windows.conf

7. Después de esto, debe [importar](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/) las colecciones que se encuentran dentro del directorio */postman* para comenzar a interactuar con la aplicación.

8. Por último, si desea verificar el comportamiento de las pruebas unitarias y de integración, diríjase a la sección del documento *Pruebas Unitarias y de Integración* para un mejor entendimiento de este módulo.

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)
