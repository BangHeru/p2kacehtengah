from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageResize(object):
    
    def __init__(self,  foto, lebar, tinggi):
        self.foto = foto
        self.lebar = lebar
        self.tinggi = tinggi


    
    def proses(self):
        #Opening the uploaded image
        # im = Image.open(self.foto1)
        im = Image.open(self.foto)

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (self.lebar, self.tinggi) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        return InMemoryUploadedFile(
                        output,
                        'ImageField', "%s.jpg" %self.foto.name.split('.')[0], 
                        'image/jpeg', sys.getsizeof(output), 
                        None)

