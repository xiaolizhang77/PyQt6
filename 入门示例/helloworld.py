#   QApplication管理应用
#   QWidget管理控件
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建应用
print(sys.argv)   #  sys.argv是列表:[python文件的目录,一些参数,……]
print(app.arguments())    #同上

window = QWidget()
window.setWindowTitle("pyqt6实战")
window.resize(400, 300)  # 窗口大小
window.show()  # 创建窗口
window.move(100, 300)  # 窗口位置

label = QLabel()  #
label.setText("这是标签")
label.setParent(window)  # 设置父组件
label.move(80, 80)  # 换个位置
label.resize(150, 50)  # 大小
label.setStyleSheet("background-color:yellow;padding:10px") #   设置样式    padding边距
label.show()

sys.exit(app.exec())  # 开始执行程序，并进行消息等待
