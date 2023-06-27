#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from PIL import Image, ImageFilter
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import  QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QListWidget, QFileDialog
import os

from PIL.ImageFilter import (
    BLUR,
    CONTOUR,
    DETAIL,
    EDGE_ENHANCE,
    EDGE_ENHANCE_MORE,
    EMBOSS,
    FIND_EDGES,
    SMOOTH,
    SMOOTH_MORE,
    SHARPEN,
    GaussianBlur,
    UnsharpMask,
)


# original = Image.open('original.jpg')

# print(original.size)
# print(original.format)
# print(original.mode)

# original.show()
# #сделай оригинал изображения чёрно-белым
# pic_wb = original.convert('L')
# pic_wb.save('gray.jpg')
# pic_wb.show()
# #сделай оригинал изображения размытым
# pic_blured = original.filter(ImageFilter.BLUR)
# pic_blured.save('blured.jpg')
# pic_blured.show()

# #поверни оригинал изображения на 180 градусов
# pic_rot = original.transpose(Image.ROTATE_180)
# pic_rot.save('up.jpg')
# pic_rot.show()

# # Отзеркаливание
# pic_mirror = original.transpose(Image.FLIP_LEFT_RIGHT)
# pic_mirror.save('mirrow.jpg')
# pic_mirror.show()

# # Увеличение контраста

# pic_contrast = ImageEnhance.Contrast(original)
# pic_contrast = pic_contrast.enhance(1.5)
# pic_contrast.save('contr.jpg')
# pic_contrast.show()

# chooseWorkdir
def click_folder():
    # global workdir
    # workdir = QFileDialog.getExistingDirectory()

    # if workdir != '':
            
    #     files = os.listdir(workdir)
    #     list_names.clear()

    #     res = filter(files, ['jpg', 'png', 'jpeg', 'bmp', 'gif'])
    #     list_names.addItems(res)

    #     if not (os.path.isdir(workdir+ "\modification")):
    #         # print('Создание папки modification')
    #         os.mkdir(workdir + '\modification')

    #     else:
    #         files = os.listdir(workdir + '\modification')
    #         res = filter(files, ['jpg', 'png', 'jpeg', 'bmp'])
    #         list_names.addItems(res)
    workimage.workdir = QFileDialog.getExistingDirectory()

    if workimage.workdir != '':
        workimage.show_files()


def filter(files, extension):
    result = []
    
    for elem in files:
        for ext in extension:
            if elem.endswith(ext):
                result.append(elem)
                break

    return result



def showFilenamesList():
    files = os.listdir(workimage.workdir)

    list_names.clear()

    res = filter(files, ['jpg', 'png', 'jpeg', 'bmp'])

    list_names.addItems()




def showChosenImage():
    
    if list_names.currentRow() >= 0:

        filename = list_names.currentItem().text()

        workimage.current_image_name = filename

        workimage.path = os.path.join(workimage.workdir, filename)

        workimage.loadimage()
        workimage.showimage()


def do_bw():
    pic_gray = ImageProcessor()
    pic_gray.loadimage(workimage.name_image)
    # pic_gray.image = ip.image.convert('L')
    workimage.new_image = workimage.image.convert('L') # * так приерно?
    workimage.showimage()
    print('1') 
    # * Чтобы не переписывать оригинал

def do_left():
    workimage = workimage.image.transpose(Image.FLIP_LEFT_RIGHT)
    # pic_mirror.save('mirrow.jpg')
    # pic_mirror.show()

def do_right():
    right = ImageProcessor()
#     right.loadimage = workimage.loadimage
#     filename = list_names.currentItem().text()
#     workimage.loadimage(os.path.join(workdir, filename))
#     right.loadimage(os.path.join(workdir, filename))
#     # Сохранить right.path как название и отправиить и # ? бдыщ
#     pic_mirror.save('mirrow.jpg')
#     pic_mirror.show()
# # join

#     filename = list_names.currentItem().text()
#     right.loadimage(filename)
#     test = right.image.transpose(Image.FLIP_LEFT_RIGHT)
#     # right.showimage()
#     # test.save('test.png')
#     test.save('копия-' + filename)
#     right.loadimage('копия-' + filename)
#     right.showimage()

def do_mirror():
    pass

def do_contrast():
    pass

def do_save():
    print('save')
    if workdir != None:
        path = workdir + '\modification'
        if not (os.path.isdir(path)):
            print('Создание папки modification')
            os.mkdir(path)
    
    fullname = os.path.join(path, 'mod_' + workimage.name_image)

    self.name_image.loadimage(fullname)


class ImageProcessor():
    def __init__(self):

        self.current_image = None
        self.pixmap = None
        # self.image = None
        self.name_image = None
        self.path = None
        self.folder = 'modification'


    def loadimage(self):

        # self.name_image = filename
        # self.path = os.path.join(workdir, filename)
        self.current_image = Image.open(self.path)
        self.pixmap = self.get_pixmap(0)

        print(f'{self.name_image} короткое имя')
        print(f'{self.path} длинное имя') 

    def showimage(self):
        label_picture.hide()
        # pixmap = QPixmap(self.name_image)
        # label_picture.setScaledContents(True)
        # label_picture.setPixmap(pixmap)
        w = label_picture.width()
        h = label_picture.height()


         
        # self.pixmap = QPixmap(self.path)
        self.pixmap = self.pixmap.scaled(w,h, Qt.KeepAspectRatio)
        label_picture.setPixmap(self.pixmap)
        label_picture.show()

    
    def get_pixmap(self, code: int):
        if code == 0:
            return QPixmap(self.path)

        if code == 1:
            qim = ImageQt(self.current_image)
            return QPixmap.fromImage(qim).copy()


    def save_image(self):
        print('save')
        if self.workdir != None:
            path = self.workdir + '\modification'
            if not (os.path.isdir(path)):
                print('Создание папки modification')
                os.mkdir(path)
        
            fullname = os.path.join(path, workimage.current_image_name)

            self.current_image.save(
                fullname, None
            )
        self.show_files()


    def show_files(self):
        files = os.listdir(self.workdir)

        list_names.clear()

        res = filter(files, ['jpg', 'png', 'bmp', 'jpeg'])

        list_names.addItems(res)

        if not (os.path.isdir(workimage.workdir + '\modification')):
            os.mkdir(self.workdir + '\modification')

        else:
            
            files = os.listdir(self.workdir + '\modification')
            res = filter(files, ['jpg', 'png', 'jpeg', 'bmp'])
            list_names.addItems(res)
  

    def filter_right(self):
        if self.current_image != None:
            self.current_image = self.current_image.transpose(Image.ROTATE_90).copy()
            self.pixmap = self.get_pixmap(1)
            self.showimage()
        
    
    def filter_left(self):
        if self.current_image != None:
            self.current_image = self.current_image.transpose(Image.ROTATE_270).copy()
            self.pixmap = self.get_pixmap(1)
            self.showimage()

    def filter_mirror(self):
        if self.current_image != None:
            self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT).copy()
            self.pixmap = self.get_pixmap(1)
            self.showimage()

    def filter_bw(self):
        if self.current_image != None:
            self.current_image = self.current_image.convert('L').copy()
            self.pixmap = self.get_pixmap(1)
            self.showimage()

    def filter_blur(self):
        if self.current_image != None:
            self.current_image = self.current_image.filter(ImageFilter.BLUR).copy()
            self.pixmap = self.get_pixmap(1)
            self.showimage()

    






# App
app = QApplication([])

# Window
main_win = QWidget()
main_win.resize(800,600)
main_win.show()
main_win.setWindowTitle('Easy Edit')


# Layouts
# -Main layout
main_h_layout = QHBoxLayout()
main_win.setLayout(main_h_layout)

# - Left and Right Layout
left_v_layout = QVBoxLayout()
right_v_layout = QVBoxLayout()

# help layout
help_h_layout = QHBoxLayout()

# add Layouts
main_h_layout.addLayout(left_v_layout)
main_h_layout.addLayout(right_v_layout)


# Widgets
# -Lists 
list_names = QListWidget()
# -Label
label_picture = QLabel('Картинка')


# -Button
button_folder = QPushButton('Папка')
button_left = QPushButton('Лево')
button_right = QPushButton('Право')
button_mirror = QPushButton('Зеркало')
button_blur = QPushButton('Размытость')
button_bw = QPushButton('Ч/Б') 
button_save = QPushButton('Сохранить')


# LEFT
left_v_layout.addWidget(button_folder, alignment = Qt.AlignLeft)
left_v_layout.addWidget(list_names, alignment = Qt.AlignLeft)


# RIGHT
right_v_layout.addWidget(label_picture)
# label_picture.setStyleSheet('background: #1F000F')

right_v_layout.addLayout(help_h_layout)
help_h_layout.addWidget(button_left )
help_h_layout.addWidget(button_right)
help_h_layout.addWidget(button_mirror)
help_h_layout.addWidget(button_blur)
help_h_layout.addWidget(button_bw )
help_h_layout.addWidget(button_save)


workimage = ImageProcessor()


button_left.clicked.connect(workimage.filter_left)
button_right.clicked.connect(workimage.filter_right)
button_folder.clicked.connect(click_folder)
list_names.clicked.connect(showChosenImage)
button_bw.clicked.connect(workimage.filter_bw)
button_mirror.clicked.connect(workimage.filter_mirror)
button_blur.clicked.connect(workimage.filter_blur)
button_save.clicked.connect(workimage.save_image)










app.exec_()




