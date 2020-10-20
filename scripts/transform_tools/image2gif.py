import os
import numpy as np
from PIL import Image, ImageDraw
import imageio
import inspect


def add_text_to_image(image, text, font=None):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)

    print(rgba_image)
    """set text location"""
    text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
    """set text color and transparency"""
    image_draw.text(text_xy, text, font=font, fill=(255, 0, 0, 800))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


def image2gif(ProcessBar, load_path, gif_name, fps):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])
    """int fps"""
    fps = int(fps)
    """image name save format"""
    image_format = '{:05d}{:s}.jpg'
    """gif basename"""
    gif_basename = os.path.basename(gif_name)
    images = os.listdir(load_path)
    """duration"""
    duration = 1/fps
    """the index of the image that has been processed"""
    image_index = 1
    """for store each frame image"""
    frames = []
    ProcessBar.set_zero()
    for image in range(len(images)):
        jpgfile = str(load_path + '/' + image_format.format(image_index, ''))
        frame = Image.open(jpgfile)
        frame = add_text_to_image(frame, gif_basename)
        frames.append(np.array(frame))
        print(image_index)
        image_index += 1
        ProcessBar.set_Value(image_index, len(images), ratio=90)
        if image_index == len(images):
            ProcessBar.set_Text("Please wait ... it may take a few minutes...")
    print("Please wait ... it may take a few minutes...")

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)  # duration = 1/fps
    ProcessBar.set_max()
    print(gif_basename, 'Synthetic success!')
