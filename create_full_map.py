from PIL import Image
from glob import glob
import re
import os
import numpy as np
import PIL



def start():
    for x in range(39, 65):
        os.chdir("C:/Users/Brok/mapgen/gen map")
        l = []
        p = re.compile(f"0_\d\d_{x}.png")
        for images in glob("*.png"):
            if re.match(p, images):
                l.append(images)


        images = [Image.open(x) for x in l]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            print(im)
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]

        new_im.save(f'C:/Users/Brok/Pictures/map/{x}.png')


start()
t = []
for i in glob("C:/Users/Brok/Pictures/map/*.png"):
    t.append(i)

# for x in range(39, 65):
#     os.chdir("C:/Wiki07/mapgen/versions/2022-03-23_a/tiles/base")
#     l = []
#     p = re.compile(f"0_\d\d_{x}.png")
#     for images in glob("*.png"):
#         if re.match(p, images):
#             l.append(images)


imgs    = [ PIL.Image.open(i) for i in reversed(t) ]

# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save that beautiful picture
    # imgs_comb = PIL.Image.fromarray( imgs_comb)
    # imgs_comb.save(f'E:/Pictures/map rows/{x}.png' )

# for a vertical stacking it is simple: use vstack

imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'C:/Users/Brok/Pictures/map/map.png' )
