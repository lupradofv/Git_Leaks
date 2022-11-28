# Git_Leaks

Extraer los datos del repositorio provisto mediante la clase Repo: representa un repositorio de git y va a permitir solicitar información de commits realizados.

El usuario introduce las palabras claves que desea localizar en los commits del repositorio: la búsqueda se realiza mediante el uso de expresiones regulares, almacenando en un diccionario la información de cada coincidencia (hash del commit, autor, fecha de realización, palabra clave solicitada y su posición en dicho commit).

En el caso de no dar con ninguna ocurrencia de la palabra clave, se indica que no ha habido coincidencias.

# Formato json

El repositorio contiene además el código necesario para exportar los datos obtenidos con el buscador de leaks a un fichero json.
