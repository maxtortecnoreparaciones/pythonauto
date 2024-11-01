from PIL import Image

import os

downloadsFolder = "C:\\Users\\Administrador\\Downloads\\"
 # Verifica si el archivo tiene una de las extensiones permitidas
if __name__ == "__main__":
   for filename in os.listdir(downloadsFolder):
    name,extension = os.path.splitext(downloadsFolder + filename)
    # Guarda la imagen comprimida
    if extension in [".jpg", ".jpeg", ".png"]:
        picture = Image.open(downloadsFolder + filename)
        picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)
        #borrar las originales que se comprimieron
        os.remove(os.path.join(downloadsFolder, filename))
