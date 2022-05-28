# Conexion a MongoDB con Python 3.10.2

## _Operaciones CRUD (Create,Read,Update,Delete)_

Este programa fue en base a los requerimientos solicitados en el curso de bases de datos, el corte 3 consistia en bases
NoSQL.


## Dependicias y/o plugins

- pymongo
- pylint

> Se recomienda utilizar un entorno virtual (VENV)
> para no afectar las dependicias instaladas globlamente

## Creacion de un VENV
Para crear un entorno virtual, primero debemos estar en nuestra carpeta de trabajo, posterior a esto utilizamos

- Windows
```sh
    py -m venv nombre_venv
```
- Bash
```sh
    python3 -m venv nombre_venv
```

Una vez creado nuestro entorno virtual procedemos a activarlo

- Windows
```sh
    .\nombre_venv\Scripts\activate
```
- Bash
```sh
    source nombre_venv/Bin/activate
```

Para desactivar nuestro entorno virtual

- Windows / Bash
```sh
    deactivate 
```

## Installacion de dependencias
El archivo requierements.txt posee las dependencias usadas para el desarrollo del programa, para instalar todas a la vez
utilizamos el siguente comando.

```sh
pip install -r requierements.txt
```
> Utilizar este comando cuando ya este creado el venv y este activado


**Software Libre :D!**