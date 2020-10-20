from scripts.Form.MainForm import *
from scripts.Form.VideoScreenShotForm import VideoScreenShotForm
from scripts.transform_tools.video2image import video2image
from scripts.transform_tools.image2video import image2video
from scripts.transform_tools.image2gif import image2gif
from scripts.Button.ButtonSub import *
from scripts.utils.ProcessBar import ProcessBar
from scripts.utils.set_cwd import set_cwd
from scripts.utils.check_jpg_dir import check_jpg_dir


class SelectForm(MainForm):
    def __init__(self, name='SelectForm', settings=set_cwd()):
        super(SelectForm, self).__init__(name)
        """default fps"""
        self.fps = 25
        """VideoScreenShotForm"""
        self.VideoScreenShotForm = None

        """ProcessBar"""
        self.ProcessBar = ProcessBar()
        """path for button"""
        self.images_folder = settings['images_folder']
        self.gif_folder = settings['gif_folder']
        self.video_folder = settings['video_folder']

        """btn images2gif"""
        self.btn_images2gif = Button_images2gif(self).get_btn()

        """btn video2images"""
        self.btn_video2images = Button_video2images(self).get_btn()

        """btn videos2images"""
        self.btn_videos2images = Button_videos2image(self).get_btn()

        """btn images2video"""
        self.btn_images2video = Button_images2video(self).get_btn()

        """btn VideoScreenShot"""
        self.btn_videoscreenshot = Button_videoscreenshot(self).get_btn()
        """layout"""
        layout = QVBoxLayout()
        layout.addWidget(self.btn_images2gif)
        layout.addWidget(self.btn_video2images)
        layout.addWidget(self.btn_videos2images)
        layout.addWidget(self.btn_images2video)
        layout.addWidget(self.btn_videoscreenshot)
        layout.addWidget(self.ProcessBar.get_pbar_text())
        layout.addWidget(self.ProcessBar.get_pbar())
        self.setLayout(layout)

        """signal"""
        self.btn_images2gif.clicked.connect(self.slot_btn_images2gif)
        self.btn_video2images.clicked.connect(self.slot_btn_video2images)
        self.btn_videos2images.clicked.connect(self.slot_btn_videos2images)
        self.btn_images2video.clicked.connect(self.slot_btn_images2video)
        self.btn_videoscreenshot.clicked.connect(self.slot_btn_videoscreenshot)

    """transform images to gif"""
    def slot_btn_images2gif(self):
        QMessageBox.information(self,
                                'Choose the frames directory',
                                "Choose the frames folder.")
        check_flag = True
        video_dir_choose = None
        while check_flag:
            video_dir_choose = QFileDialog.getExistingDirectory(self,
                                                                "select the load path",
                                                                self.images_folder['images2gif'])
            self.images_folder['images2gif'] = video_dir_choose

            if video_dir_choose == "":
                print("\nCancel Select load directory")
                return
            """check direction whether exists jpg files"""
            check_flag = self.check_load_jpg_dir(video_dir_choose, "gif")

        gifname_choose, file_type = QFileDialog.getSaveFileName(self,
                                                                "choose video path",
                                                                self.gif_folder['images2gif'],
                                                                "All Files (*);;"
                                                                "gif Files (*.gif);;")
        self.gif_folder = os.path.abspath(gifname_choose)

        if gifname_choose == "":
            print("\nCancel Select video")
            return

        print("\nThe chosen images is:")
        print(gifname_choose)

        """input fps"""
        ok_pressed = True
        while ok_pressed:
            fps, ok_pressed = QInputDialog.getText(self,
                                                   "Fps Setting",
                                                   "Please input fps:",
                                                   QLineEdit.Normal,
                                                   str(self.fps))
            if ok_pressed and fps.strip():  # erase head and tail blank

                image2gif(self.ProcessBar,
                          video_dir_choose,
                          gifname_choose,
                          fps)

                self.reset_pbar()
                QMessageBox.information(self,
                                        'Synthetic success!',
                                        os.path.basename(gifname_choose) + ' Synthetic success!')

                return

            elif ok_pressed is False:
                return
            else:
                QMessageBox.critical(self, 'Error', "please input fps and try again!")

    """transform video to images"""
    def slot_btn_video2images(self):
        QMessageBox.information(self,
                                'Choose the video',
                                "Choose the video")
        videoname_choose, file_type = QFileDialog.getOpenFileName(self,
                                                                  "choose video path",
                                                                  self.video_folder['video2images'],
                                                                  "All Files (*);;"
                                                                  "Video Files (*.mp4);;"
                                                                  "Video Files (*.avi);;"
                                                                  "Video Files (*.mkv);;")
        self.video_folder['video2images'] = os.path.abspath(videoname_choose)
        if videoname_choose == "":
            print("\nCancel Select video")
            return
        QMessageBox.information(self,
                                'Choose the save path',
                                "Choose the frames save path")
        video_dir_choose = QFileDialog.getExistingDirectory(self,
                                                            "select the save path",
                                                            self.images_folder['video2images'])
        self.images_folder['video2images'] = video_dir_choose
        if video_dir_choose == "":
            print("\nCancel Select save directory")
            return

        print("\nThe chosen video is:")
        print(videoname_choose)
        """Select video and transform to images"""
        image_save_folder, video_name, fps, total_finish_frame_number = video2image(self.ProcessBar,
                                                                                    videoname_choose,
                                                                                    video_dir_choose)
        """check direction whether exists jpg files"""
        video_information = self.check_save_video_dir(image_save_folder,
                                                      video_name,
                                                      fps,
                                                      total_finish_frame_number)

        self.reset_pbar()
        QMessageBox.information(self, 'Save Results',
                                "video2images" + " has been finished!\n" +
                                video_information
                                )

    """transform videos to images"""
    def slot_btn_videos2images(self):
        QMessageBox.information(self,
                                'Choose the videos',
                                "Choose the videos")
        videoname_chooses, file_type = QFileDialog.getOpenFileNames(self,
                                                                    "choose videos path",
                                                                    self.video_folder['videos2images'],
                                                                    "All Files (*);;"
                                                                    "Video Files (*.mp4);;"
                                                                    "Video Files (*.avi);;"
                                                                    "Video Files (*.mkv);;")
        self.video_folder['videos2images'] = os.path.abspath(videoname_chooses[0])
        if len(videoname_chooses) == 0:
            print("\nCancel Select videos")
            return
        QMessageBox.information(self,
                                'Choose the save path',
                                "Choose the frames save path")
        video_dir_choose = QFileDialog.getExistingDirectory(self,
                                                            "select the save path",
                                                            self.images_folder['videos2images'])
        self.images_folder['videos2images'] = video_dir_choose
        if video_dir_choose == "":
            print("\nCancel Select save directory")
            return
        print("\nThe chosen videos are:")

        """Select videos and transform to images"""
        video_informations = ''
        for videoname_choose in videoname_chooses:
            print(videoname_choose)

            image_save_folder, video_name, fps, total_finish_frame_number = video2image(self.ProcessBar,
                                                                                        videoname_choose,
                                                                                        video_dir_choose)
            """check direction whether exists jpg files"""
            video_information = self.check_save_video_dir(image_save_folder,
                                                          video_name,
                                                          fps,
                                                          total_finish_frame_number)
            video_informations += video_information

        self.reset_pbar()
        QMessageBox.information(self, 'Save Results',
                                "video2images" + " has been finished!\n" +
                                video_informations
                                )

    """transform images to video"""
    def slot_btn_images2video(self):
        QMessageBox.information(self,
                                'Choose the frames directory',
                                "Choose the frames folder.")
        check_flag = True
        video_dir_choose = None
        while check_flag:
            video_dir_choose = QFileDialog.getExistingDirectory(self,
                                                                "select the load path",
                                                                self.images_folder['images2video'])
            self.images_folder['images2video'] = video_dir_choose
            if video_dir_choose == "":
                print("\nCancel Select load directory")
                return
            """check direction whether exists jpg files"""
            check_flag = self.check_load_jpg_dir(video_dir_choose, "video")

        videoname_choose, file_type = QFileDialog.getSaveFileName(self,
                                                                  "choose video path",
                                                                  self.video_folder['images2video'],
                                                                  "All Files (*);;"
                                                                  "Video Files (*.mp4);;"
                                                                  "Video Files (*.avi);;"
                                                                  "Video Files (*.mkv);;")
        self.video_folder['images2video'] = os.path.abspath(videoname_choose)
        if videoname_choose == "":
            print("\nCancel Select video")
            return

        print("\nThe chosen images is:")
        print(videoname_choose)

        """input fps"""
        ok_pressed = True
        while ok_pressed:
            fps, ok_pressed = QInputDialog.getText(self,
                                                   "Fps Setting",
                                                   "Please input fps:",
                                                   QLineEdit.Normal,
                                                   str(self.fps))
            if ok_pressed and fps.strip():  # erase head and tail blank

                image2video(self.ProcessBar,
                            videoname_choose,
                            video_dir_choose,
                            fps)

                self.reset_pbar()
                QMessageBox.information(self,
                                        'Synthetic success!',
                                        os.path.basename(videoname_choose) + ' Synthetic success!')
                return

            elif ok_pressed is False:
                return
            else:
                QMessageBox.critical(self, 'Error', "please input fps and try again!")

    """video screen shot"""
    def slot_btn_videoscreenshot(self):
        self.VideoScreenShotForm = VideoScreenShotForm()
        self.VideoScreenShotForm.show()
        print("VideoScreenShotForm Start...\n")
        return




    def check_load_jpg_dir(self, video_dir_choose, target):
        """check direction whether exists jpg files"""
        check_flag, frames_number = check_jpg_dir(video_dir_choose)
        if check_flag is True and frames_number is 0:
            QMessageBox.critical(self, 'Error', "No jpg file was found, please choose the right folder!!")
        elif check_flag is True and frames_number is 1:
            QMessageBox.critical(self, 'Error', "Only 1 jpg file was found, please choose the right folder!!")
        else:
            check_flag = False
            QMessageBox.information(self, 'Frames Number',
                                    str(frames_number) + " jpg file were found, continue to choose " + target + " path.")
        return check_flag

    def check_save_video_dir(self, image_save_folder, video_name, fps, total_finish_frame_number):
        """check direction whether exists jpg files"""
        _, video_number = check_jpg_dir(image_save_folder)
        video_information = video_name + ':\n' + \
                            str(total_finish_frame_number) + ' images have been transformed.\n' + \
                            "fps :" + str(fps) + '\n' + '\n'
        return video_information

    def reset_pbar(self):
        self.ProcessBar.reset_pbar()
