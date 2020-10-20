import os


def check_jpg_dir(video_dir_choose):
    frames = os.listdir(video_dir_choose)
    frames_number = 0
    for frame in frames:
        if frame.endswith('jpg'):
            frames_number += 1
    if frames_number == 0:
        check_flag = True
    elif frames_number == 1:
        check_flag = True
    else:
        check_flag = False
        print(frames_number, " images has been chosen.")
    return check_flag, frames_number
