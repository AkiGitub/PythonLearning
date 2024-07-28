from PIL import Image
from PIL import ImageFilter

import pathlib


curFolder = str(pathlib.Path(__file__).parent.resolve());

with Image.open(curFolder+'\\1.bmp') as image:
      img = image.rotate(90)
      img = img.filter(ImageFilter.FIND_EDGES)
      img.save(curFolder+'\\out.png')
