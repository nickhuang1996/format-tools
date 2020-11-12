import cv2
import inspect
import numpy as np
import math


def imagecut(ProcessBar, image_path, save_path, new_frame):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])

    img_np = cv2.imread(image_path, 1)

    cropped = img_np[new_frame[2]: new_frame[3], new_frame[0]: new_frame[1]]
    new_height = cropped.shape[0]
    new_width = cropped.shape[1]
    resized_new_height = math.floor(new_height * 0.5)
    resized_new_width = math.floor(new_width * 0.5)
    resized_cropped = cv2.resize(cropped, (resized_new_width, resized_new_height))
    cv2.imshow("new", resized_cropped)
    cv2.imwrite(save_path, cropped)


