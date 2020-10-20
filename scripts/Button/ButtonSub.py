from scripts.Button.ButtonBase import ButtonBase

"""Choose images2gif"""
class Button_images2gif(ButtonBase):

    def get_btn(self):
        self.btn.setObjectName("btn_chooseDir")
        self.btn.setText("images2gif")
        return self.btn


"""Choose video2images"""
class Button_video2images(ButtonBase):

    def get_btn(self):
        self.btn.setObjectName("btn_chooseFile")
        self.btn.setText("video2images")
        return self.btn


"""Choose videos2image"""
class Button_videos2image(ButtonBase):

    def get_btn(self):
        self.btn.setObjectName("btn_chooseMutiFile")
        self.btn.setText("videos2image")
        return self.btn


"""Choose images2video"""
class Button_images2video(ButtonBase):

    def get_btn(self):
        self.btn.setObjectName("btn_saveFile")
        self.btn.setText("images2video")
        return self.btn

"""Choose videoscreenshot"""
class Button_videoscreenshot(ButtonBase):

    def get_btn(self):
        self.btn.setObjectName("btn_VideoScreenShot")
        self.btn.setText("videoscreenshot")
        return self.btn