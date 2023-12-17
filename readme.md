# Descripción:

2 scripts que redimensiona todas las fotos de una carpeta.

## Pre-requesitos

- instalar python3 en su máquina - [descarga](https://www.python.org/downloads/)
- instalar Pillow. Ejecutar en la terminal:
    
    `pip3 install Pillow ` 

## redimensionar.py

Ese script mantiene la proporcion de la foto y a redimensiona según un ancho y un alto máximo.

Comando a ejecutar:

    `python3 redimensionar.py [ORIGEN] [DESTINO] [ANCHO] [ALTO]`

### Ejemplo

- ORIGEN de los archivos en la carpeta "original"
- DESTINO de los archivos en la carpeta "resized"
- ANCHO igual a 904px
- ALTO igual a 508px
    
    `python3 redimensionar.py ./original ./resized 904 508`

## redimensionar-fijo.py

Ese script dimensiona la foto al ancho seleccionado y después corta la misma con el alto definido de modo que el centro de la foto original siga en el centro de la foto obtenida.

    `python3 redimensionar-fijo.py [ORIGEN] [DESTINO] [ANCHO] [ALTO]`

### Ejemplo

- ORIGEN de los archivos en la carpeta "original"
- DESTINO de los archivos en la carpeta "resized"
- ANCHO igual a 904px
- ALTO igual a 508px
    
    `python3 redimensionar-fijo.py ./original ./resized 904 508`
