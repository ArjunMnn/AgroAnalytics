import base64
from PIL import Image
import sys

image_fullpath=sys.argv[1]
image_name=sys.argv[2]
img=Image.open(str(image_fullpath))
image_save_path=image_fullpath.replace(image_name,"temp.png")
img.rotate(90).convert("LA").save()

