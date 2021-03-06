from scripts.Form.MainForm import *
from scripts.utils.set_cwd import set_cwd
from scripts.transform_tools.imagecut import imagecut
from scripts.utils.ProcessBar import ProcessBar


class ImageCutForm(MainForm):
    def __init__(self, name='ImageCutForm', settings=set_cwd()):
        super(ImageCutForm, self).__init__(name)

        """path for button"""
        self.images_folder = settings['images_folder']
        """ProcessBar"""
        self.ProcessBar = ProcessBar()
        """grid layout"""
        grid = QGridLayout()
        self.grid = grid
        self.setLayout(self.grid)

        """location contents set"""
        screen_shot_set =[
            'left-up-x', 'right-bottom-x',
            ' ', ' ',
            'left-up-y', 'right-bottom-y',
            ' ', ' ',
            'OK', '',
            'process:', '',
            'pbar', ''
        ]

        LineEdit_index = 0
        LineEdit_content = ['left-up-x', 'right-bottom-x', 'left-up-y', 'right-bottom-y']
        """locations set"""
        positions = [(i, j) for i in range(7) for j in range(2)]
        for pos, name in zip(positions, screen_shot_set):
            if name == '':
                continue
            elif name is 'OK':
                btn = QPushButton(name)
                btn.setObjectName(name)
                btn.clicked.connect(self.slot_btn_image_cut)
                grid.addWidget(btn, *pos, 1, 2)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            elif name is 'process:':
                pbar_text = self.ProcessBar.get_pbar_text()
                pbar_text.setObjectName(name)
                grid.addWidget(pbar_text, *pos, 1, 2)
                pbar_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            elif name is 'pbar':
                pbar_loc = self.ProcessBar.get_pbar()
                pbar_loc.setObjectName(name)
                grid.addWidget(pbar_loc, *pos, 1, 2)
                pbar_loc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            elif name is ' ':
                loc = QLineEdit()
                loc.setObjectName(LineEdit_content[LineEdit_index])
                grid.addWidget(loc, *pos)
                LineEdit_index += 1
            else:
                loc_label = QLabel(name)
                loc_label.setObjectName(name)
                grid.addWidget(loc_label, *pos)

        self.left_up_x = self.findChild(QLineEdit, 'left-up-x')
        self.left_up_y = self.findChild(QLineEdit, 'left-up-y')
        self.right_bottom_x = self.findChild(QLineEdit, 'right-bottom-x')
        self.right_bottom_y = self.findChild(QLineEdit, 'right-bottom-y')
        """default 1920x1080"""
        self.left_up_x.setText("0")
        self.left_up_y.setText("0")
        self.right_bottom_x.setText("1920")
        self.right_bottom_y.setText("1080")

        self.new_frame = [[], [], [], []]

    def slot_btn_image_cut(self):
        self.new_frame = self.get_new_frame()
        QMessageBox.information(self,
                                'Choose the image',
                                "Choose the image")
        imagename_choose, file_type = QFileDialog.getOpenFileName(self,
                                                                  "choose image path",
                                                                  self.images_folder['imagecutload'],
                                                                  "All Files (*);;"
                                                                  "Image Files (*.jpg);;"
                                                                  "Image Files (*.png);;"
                                                                  "Image Files (*.bmp);;")
        self.images_folder['imagecutload'] = os.path.abspath(imagename_choose)
        if imagename_choose == "":
            print("\nCancel Select image")
            return
        QMessageBox.information(self,
                                'Choose the new image name',
                                "Choose the new image name")
        imagenewname_choose, file_type = QFileDialog.getSaveFileName(self,
                                                                     "choose image path",
                                                                     self.images_folder['imagecutsave'],
                                                                     "All Files (*);;"
                                                                     "Video Files (*.jpg);;"
                                                                     "Video Files (*.png);;"
                                                                     "Video Files (*.bmp);;")
        self.images_folder['imagecutsave'] = os.path.abspath(imagename_choose)
        if imagenewname_choose == "":
            print("\nCancel Select new image")
            return

        print("\nThe chosen video is:")
        print(imagename_choose)
        """Select video and screen shot"""
        imagecut(self.ProcessBar,
                 imagename_choose,
                 imagenewname_choose,
                 self.new_frame)
        self.reset_pbar()
        QMessageBox.information(self, 'Save Result',
                                "image cut" + " has been finished!\n"
                                )
        self.close()
        return

    def get_new_frame(self):
        self.new_frame[0] = int(self.left_up_y.text())
        self.new_frame[1] = int(self.right_bottom_y.text())
        self.new_frame[2] = int(self.left_up_x.text())
        self.new_frame[3] = int(self.right_bottom_x.text())
        return self.new_frame

    def reset_pbar(self):
        self.ProcessBar.reset_pbar()