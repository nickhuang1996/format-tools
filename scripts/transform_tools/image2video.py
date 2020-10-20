import cv2
import os
from PIL import Image
import inspect


def image2video(ProcessBar, video_new_path, load_path, fps):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])
    fps = int(fps)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    """images path"""
    images = os.listdir(load_path)
    im = Image.open(load_path + '/' + images[0])
    vw = cv2.VideoWriter(video_new_path, fourcc, fps, im.size)
    """image name save format"""
    image_format = '{:05d}{:s}.jpg'
    """the index of the image that has been processed"""
    image_index = 1

    ProcessBar.set_zero()
    for image in range(len(images)):
        jpgfile = str(load_path + '/' + image_format.format(image_index, ''))
        try:
            frame = cv2.imread(jpgfile)
            vw.write(frame)
            print("image ", str(image_index), " has been processed.")
            image_index += 1
            ProcessBar.set_Value(image_index, len(images))

        except Exception as exc:
            print(jpgfile, exc)
    vw.release()
    print(video_new_path, 'Synthetic success!')
