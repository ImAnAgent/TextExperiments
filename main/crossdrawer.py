#This is taken almost directly from the pillow specification to draw a cross
import os
from PIL import Image, ImageDraw

with Image.open("text.jpg") as im:
        
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    
im.save(os.path.join("text2.jpg"))
