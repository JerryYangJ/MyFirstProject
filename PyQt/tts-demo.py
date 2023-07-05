"""
@author: JerryYang
@file: tts-demo.py
@time: 2023/4/13 22:24
@desc:
"""
VOICE = "zh-CN-YunjianNeural"

from PyQt5 import QtWidgets
import os


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        btn_chooseFolder = QtWidgets.QPushButton('选择目录', self)
        btn_chooseFolder.setFixedSize(100, 25)
        self.label_path = QtWidgets.QLabel('', self)
        self.folderPath = ''
        btn_run = QtWidgets.QPushButton('开始', self)
        btn_run.setFixedSize(60, 25)

        # 创建一个水平layout作为内部layout
        hl = QtWidgets.QHBoxLayout()
        hl.addWidget(btn_chooseFolder)
        hl.addWidget(self.label_path)
        hl.addWidget(btn_run)

        self.textEdit = QtWidgets.QPlainTextEdit(self)

        # 创建上级layout
        layout = QtWidgets.QVBoxLayout()
        # 添加 子layout
        layout.addLayout(hl)
        # 添加内部控件
        layout.addWidget(self.textEdit)

        # 指定容器控件自身使用的layout
        self.setLayout(layout)

        # 注册按钮点击处理
        btn_chooseFolder.clicked.connect(self.chooseFolder)
        btn_run.clicked.connect(self.run)

    def chooseFolder(self):

        filePath = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件所在目录")
        self.label_path.setText(filePath)
        self.folderPath = filePath

    def run(self):
        for (dirpath, dirnames, filenames) in os.walk(self.folderPath):
            for fn in filenames:
                # 把 dirpath 和 每个文件名拼接起来 就是全路径
                fpath = os.path.join(dirpath, fn)
                self.textEdit.appendPlainText(fpath + '\n')

                mp3Path = os.path.join(dirpath, fn.replace('.txt', '.mp3'))
                cmd = f'edge-tts --voice {VOICE} -f "{fpath}" --write-media "{mp3Path}"'
                print(cmd)
                os.system(cmd)


app = QtWidgets.QApplication([])
window = Window()
window.resize(400, 200)
window.show()
app.exec_()