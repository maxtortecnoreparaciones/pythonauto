from PIL import Image

import os

downloadsFolder = "C:\\Users\\Administrador\\Downloads"

if __name__ == "__main__":
   for filename in os.listdir(downloadsFolder):
    name,extension = os.path.splitext(downloadsFolder + filename)

    if extension in [".jpg", ".jpg", ".png"]:
        picture = Image.open(downloadsFolder + filename)
        picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)
