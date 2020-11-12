import os

def set_cwd():
    cwd = os.getcwd()

    """path for each button"""
    images_folder = {}
    images_folder['images2gif'] = cwd
    images_folder['video2images'] = cwd
    images_folder['videos2images'] = cwd
    images_folder['images2video'] = cwd
    images_folder['imagecutload'] = cwd
    images_folder['imagecutsave'] = cwd

    gif_folder = {}
    gif_folder['images2gif'] = cwd

    video_folder = {}
    video_folder['video2images'] = cwd
    video_folder['videos2images'] = cwd
    video_folder['images2video'] = cwd
    video_folder['videoscreenshotload'] = cwd
    video_folder['videoscreenshotsave'] = cwd
    """The whole settings"""
    settings = {}
    settings['images_folder'] = images_folder
    settings['gif_folder'] = gif_folder
    settings['video_folder'] = video_folder

    return settings


if __name__ == '__main__':
    set_cwd()
