import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import re


def create_image(digits_list, width, height, resolution, font):
    text = ' '.join(digits_list)
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.text((500, 100), text, font=font, fill=0, anchor='mm', align='center')

    img = img.resize((width // resolution, height //
                     resolution), Image.Resampling.LANCZOS)
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    label = ''.join(digits_list)
    img.save(f"output/{label}_{resolution}.png")


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    width = 1000
    height = 200
    font = ImageFont.truetype('fonts/W_tahoma.ttf', 128)
    for i in range(10):
        digits_list = digits.copy()
        np.random.shuffle(digits_list)
        for resolution in range(1, 11):
            create_image(digits_list, width, height, resolution, font)
