import sys
from PIL import Image

if len(sys.argv) == 2:
  nombre_fichero = sys.argv[1]
  img = Image.open(nombre_fichero).convert('1')
  size = 64, 64
  img.thumbnail(size)
  img.save(nombre_fichero + ".jpg","JPEG")
  img.save(nombre_fichero + ".pbm", "PPM")
else:
  print("python conversor.py nombre_fichero")
        
