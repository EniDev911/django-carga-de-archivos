from django.db import models
import os
# Create your models here.
class Imagen(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def delete(self, *args, **kwars):
        imagen_path = self.image.path
        super().delete(*args, **kwars)

        if os.path.isfile(imagen_path):
            os.remove(imagen_path)

        folder_path = os.path.dirname(imagen_path)
        while folder_path:
            if os.path.exists(folder_path):
                try:
                    os.rmdir(folder_path) # intenta eliminar la carpeta
                except OSError:
                    break # La carpeta no está vacía, no se elimina
            else:
                break # Se sale del bucle si la carpeta no existe
            folder_path = os.path.dirname(folder_path) # movemos hacia la carpeta padre
    def __str__(self):
        return self.caption