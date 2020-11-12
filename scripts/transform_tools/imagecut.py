import cv2
import inspect
import numpy as np
import math
import os


def imagecut(ProcessBar, image_path, save_path, new_frame):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])
    """Solver Chinese path"""
    img_np = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)

    cropped = img_np[new_frame[2]: new_frame[3], new_frame[0]: new_frame[1]]
    new_height = cropped.shape[0]
    new_width = cropped.shape[1]
    resized_new_height = math.floor(new_height * 0.5)
    resized_new_width = math.floor(new_width * 0.5)
    resized_cropped = cv2.resize(cropped, (resized_new_width, resized_new_height))
    cv2.imshow(save_path, resized_cropped)
    # cv2.imwrite(save_path, cropped)
    save_path_suffix = os.path.splitext(image_path)[-1]
    """Solver Chinese path"""
    cv2.imencode(save_path_suffix, cropped)[1].tofile(save_path)



