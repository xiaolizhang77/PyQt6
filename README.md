# PyQt6——PyQt6笔记和demo
### 一、安装及配置
#### 安装PyQt6:
    pip install PyQt6 -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install PyQt6-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
#### 配置QTDesigner和pyuic

##### QTDesigner

![图1](image/md_img_1.png "image1")
路径:

    D:\anaconda3\envs\MwaEnv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe
##### pyuic
![图2](image/md_img_2.png "image2")
program:Python路径\
arguments:-m PyQt6.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py\
working directory:$FileDir$

#### 效果
![图3](image/md_img_3.png "image3")

QTDesigner工具：
![图4](image/md_img_4.png "image4")

pyuic将ui文件自动变python文件：
![图5](image/md_img_5.png "image5")
