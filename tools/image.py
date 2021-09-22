import PIL.Image
import numpy as np


def convert_image(file):
    image = PIL.Image.open(file)
    image = image.convert('RGB')
    re_image = np.array(image)
    print(re_image.shape)


if __name__ == '__main__':
    convert_image("../files/image.png")