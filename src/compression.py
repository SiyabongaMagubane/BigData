from PIL import Image
import numpy

image = Image.open('GPS.png')
ArrayImage = numpy.array(image)
print(ArrayImage)
