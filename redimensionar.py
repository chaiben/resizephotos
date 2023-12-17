from PIL import Image
import os
import sys

def redimensionar_imagenes(carpeta_imagenes, carpeta_destino, nuevo_ancho, nuevo_alto):
    # Crea una carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Recorre todos los archivos en la carpeta
    for archivo in os.listdir(carpeta_imagenes):
        ruta_original = os.path.join(carpeta_imagenes, archivo)

        # Verifica si el archivo es una imagen
        if os.path.isfile(ruta_original) and archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Abre la imagen original
            imagen = Image.open(ruta_original)

            # Obtiene las dimensiones actuales de la imagen
            ancho_original, alto_original = imagen.size

            # Calcula las nuevas dimensiones conservando la proporción
            proporcion = nuevo_ancho / ancho_original
            nuevo_ancho_redimensionado = int(ancho_original * proporcion)
            nuevo_alto_redimensionado = int(alto_original * proporcion)

            # Redimensiona la imagen
            imagen_resized = imagen.resize((nuevo_ancho_redimensionado, nuevo_alto_redimensionado))

            # Crea una ruta para la imagen redimensionada en la carpeta de destino
            ruta_destino = os.path.join(carpeta_destino, archivo)

            # Guarda la imagen redimensionada en la carpeta de destino
            imagen_resized.save(ruta_destino)

    print("Proceso completado.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python script.py <carpeta_imagenes> <carpeta_destino> <nuevo_ancho> <nuevo_alto>")
    else:
        carpeta_imagenes = sys.argv[1]
        carpeta_destino = sys.argv[2]
        nuevo_ancho = int(sys.argv[3])
        nuevo_alto = int(sys.argv[4])

        redimensionar_imagenes(carpeta_imagenes, carpeta_destino, nuevo_ancho, nuevo_alto)
