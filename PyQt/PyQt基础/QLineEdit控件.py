# @Time :2022/11/8 14:05
# @Author : Jerry Y
# @File  : QLineEdit控件.py
# @Info  :

'''
一、常用API
    QLineEdit.text()：返回输入框的当前文本。
    QLineEdit.addAction(Action,QLineEdit.ActionPosition)：添加动作到文本输入栏，上面已经举过例子了。
    QLineEdit.setAlignment(Qt.Alignment flag)：属性保存了输入框的对齐方式（水平和垂直方向。
    QLineEdit.setCompleter() ：输入栏的自动补全就是靠这个实现的。
    QLineEdit.deselect() ：取消选中任何已选中的文本。
    QLineEdit.displayText()：返回显示的文本。默认值为一个空字符串。
    setEchoMode（）：如果echoMode是Normal，和text()返回的一样；如果EchoMode是Password或PasswordEchoOnEdit，会返回平台相关的密码掩码字符；如果EchoMode是NoEcho，返回一个空字符串””。
    QLineEdit.selectedText()：返回选中的的文本。如果没有选中，返回一个空字符串。默认为一个空字符串。
    QLineEdit.setCursorPosition(QLineEdit.cursorPosition)：设置输入框当前光标的位置。
    QLineEdit.setMaxLength(int)：此属性包含文本的最大允许长度。如果文本太长，将从限制的位置截断。默认值为32767。
    QLineEdit.setReadOnly(bool)：此属性保存输入框是否为只读。在只读模式下，用户仍然可以将文本复制到剪贴板，但不能编辑它，且不显示光标。
    QLineEdit.setSelection(int start, int length) ：从位置start选择文本为length个字符，允许负长度。我们一启动程序是否设置setSelection的，效果如下：
    QLineEdit.setValidator()：设置输入框的验证器，将限制任意可能输入的文本
    QLineEdit.setPlaceholderText(str)：该属性包含行编辑的占位符文本。只要行编辑为空，设置此属性将使行编辑显示一个灰色的占位符文本。通常情况下，即使具有焦点，空行编辑也会显示占位符文本。但是，如果内容是水平居中的，则行编辑具有焦点时，占位符文本不会显示在光标下方。默认情况下，该属性包含一个空字符串。
    QLineEdit.isClearButtonEnabled(bool) ：是否设置清除内容的按钮。
    QLineEdit.setInputMask()：设置掩码，效果就是我们演示视频中的License输入。

二、信号
    selectionChanged() ：只要选择改变这个信号就会被发射。
    cursorPositionChanged(int old, int new) ：只要光标移动，这个信号就会发射。前面的位置old，新的位置是new。
    editingFinished()：按下返回或回车键或线条编辑失去焦点时发出此信号。
    returnPressed()：按下返回或回车键时发出此信号。
    textChanged(str)：只要文字发生变化就会发出此信号。文本参数是新文本。与textEdited()不同，当通过调用setText()以编程方式更改文本时，也会发出此信号。
    textEdited(str) ：无论何时编辑文本都会发出此信号。文本参数是新文本。与textChanged()不同，当以编程方式更改文本时，不会发出此信号，例如通过调用setText()。

三、函数
    clear() ：清除输入框内容
    copy()：如果echoMode()是Normal，将选中的文本复制到剪贴板。
    cut() ：如果echoMode()是Normal，将所选文本复制到剪贴板并删除它。 如果当前的验证不允许删除选定的文本，cut()将复制而不删除。
    paste() ：如果输入框不是只读的，插入剪贴板中的文本到光标所在位置，删除任何选定的文本。如果最终的结果不被当前的验证器接受，将没有任何反应。
    redo() ：重做上次操作，如果redo可用（isRedoAvailable() ）。
    selectAll() ：选中所有文本（即：高亮），并将光标移动到末尾。当一个默认值被插入时，这非常有用，因为如果用户在点击部件之前就输入，选中的文本将被删除。
    setText(str) ：设置输入框显示的文本。
    undo() ：撤消上次操作（如果撤销可用）
'''

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit-使用')
        self.resize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        ql_a = QLineEdit(self)
        ql_a.setPlaceholderText('测试。。。')
        action = QAction(self)
        action.setIcon(QIcon('xxx.png'))
        ql_a.addAction(action, QLineEdit.TrailingPosition)
        ql_a.setEchoMode(QLineEdit.Password)
        ql_a.move(100, 100)

        ql_b = QLineEdit(self)
        ql_b.move(100, 150)

        btn = QPushButton(self)
        btn.setText('复制')
        btn.move(100, 200)

        btn1 = QPushButton(self)
        btn1.setText('取消')
        btn1.move(200, 200)

        def cancel():
            # 取消选中
            ql_a.deselect()

        btn1.clicked.connect(cancel)

        def copy():
            text = ql_a.text()
            ql_a.setSelection(0, len(text))
            ql_b.setText(text)

        btn.clicked.connect(copy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
