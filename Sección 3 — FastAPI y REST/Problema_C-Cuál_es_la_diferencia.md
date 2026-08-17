### 1. GET vs POST
* **GET:** Se utiliza exclusivamente para **consultar o solicitar datos** al servidor sin modificar nada (por ejemplo, ver la lista de películas); sus parámetros van visibles en la URL y los navegadores pueden guardar la respuesta en caché.
* **POST:** Se usa para **enviar datos y crear o procesar un recurso** en el servidor (por ejemplo, registrar una nueva película); la información viaja en el cuerpo (*body*) de la petición y no se guarda en caché.

---

### 2. Status Code 400 vs 422 vs 500
* **400 Bad Request:** La petición ni siquiera pudo ser procesada porque el cliente envió una estructura rota o una sintaxis inválida (como un JSON mal formado o con comas sobrantes).
* **422 Unprocessable Entity:** La estructura del JSON es válida, pero los datos no cumplen con los tipos o reglas requeridas (por ejemplo, enviar un texto en un campo de fecha o dejar un parámetro obligatorio vacío).
* **500 Internal Server Error:** El cliente envió la petición correctamente, pero ocurrió un error no controlado en el servidor o la base de datos que impidió completar la operación.

---

### 3. Path Param (`/movies/{id}`) vs Query Param (`/movies?format=IMAX`)
* **Path Param (`/movies/{id}`):** Forma parte de la ruta principal y se utiliza para **identificar un recurso específico** de manera obligatoria (por ejemplo, obtener los detalles exactos de la película con ID 5).
* **Query Param (`/movies?format=IMAX`):** Se añade al final de la URL como un parámetro opcional y sirve para **filtrar, ordenar, buscar o paginar** un listado de datos.