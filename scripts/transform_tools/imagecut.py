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
    # cv2.imwrite(save_path, cropped)
    save_path_suffix = os.path.splitext(image_path)[-1]
    """Solver Chinese path"""
    cv2.imencode(save_path_suffix, cropped)[1].tofile(save_path)



