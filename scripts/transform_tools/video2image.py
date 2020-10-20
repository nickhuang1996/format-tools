import os
import cv2
import inspect


def video2image(ProcessBar, video_path, save_path):
    """set the func name on pbar text"""
    ProcessBar.set_Text(inspect.stack()[0][3])
    """select the video"""
    vc = cv2.VideoCapture(video_path)
    """image name save format"""
    image_format = '{:05d}{:s}.jpg'
    """basename"""
    video_name = os.path.basename(video_path)
    """image save folder"""
    image_save_folder = save_path + '/' + str(video_name.split('.')[0]) + '_' + str(video_name.split('.')[-1])
    if not os.path.exists(image_save_folder):
        os.mkdir(image_save_folder)
    assert os.path.exists(image_save_folder), 'Error: Invalid save path !'
    """the index of the image that has been processed"""
    image_index = 1
    """get the total frame number"""
    total_frame_number = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    """get fps"""
    fps = vc.get(cv2.CAP_PROP_FPS)
    """Start to write..."""
    print("\nStart to Write...\n")
    ProcessBar.set_zero()
    while (image_index - 1) < total_frame_number:
        ret, frame = vc.read()
        if ret:
            cv2.imwrite(image_save_folder + '/' + image_format.format(image_index, ''), frame)
            cv2.waitKey(1)
            print("image ", str(image_index), " has been processed.")
            image_index += 1
            ProcessBar.set_Value(image_index, total_frame_number)
        elif frame is None:
            print("Write process is at the end.\n")
            ProcessBar.set_zero()
            return
        else:
            print("Cannot process the image ", str(image_index), "! Write to the image failed! \n")
            ProcessBar.set_zero()
            return
    print("Write process has been finished!!\n")
    """the total number of the image"""
    print(video_name, ':', image_index - 1, ' images have been transformed.')
    """release"""
    vc.release()
    return image_save_folder, video_name, fps, image_index - 1
