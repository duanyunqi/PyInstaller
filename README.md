# PyInstaller

## 安装PyInstaller
使用pip命令安装：`pip install pyinstaller`

## PyInstaller生成可执行程序

PyInstaller工具语法：`pyinstaller 选项 python源文件`

## 注意：
1、不管这个Python应用是单文件应用还是多文件应用，只要在使用pyinstaller命令时编译作为程序入口的python程序就行。  
2、PyInstaller是跨平台工具，既可以在Windows平台上使用，也可以在Mac OS X平台上使用，不同平台使用的方法是一样的，支持的选项也是一样的

## PyInstaller生成可执行程序步骤
1、创建python应用程序，如这里的k-means聚类实例。  
2、使用命令行工具进入到python应用程序目录下，执行命令：`pyinstaller -F data.py`。  
执行完后，会有详细的生成过程。同时，python应用程序目录下会多一个dist目录，该目录下会有一个data.exe，即是PyInstaller工具生成的exe程序。  
3、-F选项，指定生成单独的exe文件，-D选项（默认选项），指定生成一个目录（包含多个文件）作为程序，子目录包含了大量.dll文件和.pyz文件，都是exe程序的支撑文件。  
4、如果需要了解PyInstaller选项的详细信息，可以通过pyinstaller -h查看


## PyInstaller打包程序踩过的坑

1、报错信息：`No module named typedefs`  
解决方案：这个问题是因为程序中导入sklearn模块，需要在编译时加上：  
  `pyinstaller -F -c xxx.py --hidden-import sklearn.neighbors.typedefs`  
继续打包，如果出现最大递归深度的报错`“Maximum recursion depth error”`，需要在.spec文件中加入  
```
import sys
sys.setrecursionlimit(5000)
```
同时把.spec文件中的`hiddenimports=[]`  
修改为  
`hiddenimports=['cython','sklearn','sklearn.ensemble','sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils','scipy._lib.messagestream']`   
保存后运行  
`pyinstaller xxx.spec`  
2、报错信息：`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce in position`  
解决方案：在命令行中先输入：`chcp 65001`，然后再输入打包命令：`pyinstaller -F xxx.py`  
3、报错信息：`AttributeError: module 'enum' has no attribute 'IntFlag'`  
解决方案：卸载enum即可，`python -m pip uninstall enum34`
