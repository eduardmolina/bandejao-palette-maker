import sys

import colorgram

from PIL import Image


if __name__ == '__main__':
    dish = Image.open(sys.argv[1]).resize((897, 567))

    img = Image.new('RGB', (960, 791), '#FFFFFF')

    colors = colorgram.extract(sys.argv[1], 10)
    colors.sort(key=lambda c: c.rgb.r)

    img.paste(dish, (34, 34))

    for i in range(10):
        img.paste(colors[i].rgb, (34 + (i * 93), 610, 94 + (i * 93), 751))

    img.save('result.png')
