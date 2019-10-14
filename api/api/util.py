import random
from io import BytesIO

from PIL import Image, ImageColor


def gen_image(filename=None, format="png"):
    color = random.choice(list(ImageColor.colormap))
    width = random.randrange(200, 300)
    height = random.randrange(200, 300)
    image = Image.new("RGB", (width, height), color=color)

    bio = BytesIO()
    bio.name = f"random_image.{format}"
    if filename:
        bio.name = filename

    image.save(bio, format)
    bio.seek(0)
    return bio
