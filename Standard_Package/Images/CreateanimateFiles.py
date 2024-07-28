import sys
from PIL import Image

images = [] 

print(sys.argv)
for arg in sys.argv[1:]:
      image = Image.open(arg)
      images.append(image)

#image1 = Image.open('')

images[0].save(
     'a.gif',sava_all = True, append_images=[images[1]] ,duration = 200, loop=0
 )