import os
import cv2
import inspect


def video_screen_shot(ProcessBar, video_path, video_new_path, new_frame):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])
    """select the video"""
    vc = cv2.VideoCapture(video_path)
    """basename"""
    video_name = os.path.basename(video_path)
    """judge the video is opened"""
    if vc.isOpened():
        print(video_name, "can be opened")
    else:
        print("video has been failed to open!")
        return

    """get fourcc"""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    """get fps"""
    fps = vc.get(cv2.CAP_PROP_FPS)
    """video width and height"""
    video_size = (int(new_frame[3] - new_frame[2]), int(new_frame[1] - new_frame[0]))
    """VideoWriter"""
    if os.path.exists(video_new_path):
        os.remove(video_new_path)
    vw = cv2.VideoWriter(video_new_path, fourcc, fps, video_size)
    """the index of the frame that has been processed"""
    image_index = 1
    """get the total frame number"""
    total_frame_number = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    """get the total video time"""
    total_time = vc.get(cv2.CAP_PROP_POS_MSEC)
    """Start to premiere..."""
    print("\nStart to premiere...\n")
    ProcessBar.set_zero()
    while (image_index - 1) < total_frame_number:
        ret, frame = vc.read()
        frame = frame[new_frame[0]:new_frame[1], new_frame[2]:new_frame[3]]
        vw.write(frame)
        print(image_index)
        image_index += 1
        ProcessBar.set_Value(image_index, total_frame_number)
    print("Screen Shot process has been finished!!\n")
    """the total number of the image"""
    print(video_name, ':', image_index - 1, ' images have been transformed.')
    """release"""
    vc.release()
    vw.release()
    return video_new_path, video_name, fps, image_index - 1
