import cv2
import PIL
from PIL import Image, ImageGrab
import inspect
import time
import numpy as np


def imagecut(ProcessBar, image_path, save_path, new_frame):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])

    img_np = cv2.imread(image_path, 1)

    cropped = img_np[new_frame[2]: new_frame[3], new_frame[0]: new_frame[1]]
    cv2.imshow("new", cropped)
    cv2.imwrite(save_path, cropped)


