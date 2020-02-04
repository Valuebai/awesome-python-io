## Ptyhon创建虚拟环境

### 方法一：自带命令
1. 进入文件夹目录
2. python -m venv -h 可查看帮助信息
3. 下面的
```
Linux运行命令行
$ 创建默认环境：python3 -m venv my_venv 
$ 创建指定环境：python3.6 -m venv  my_venv,  python2 -m venv  my_venv(添加到系统环境变量中)
$ 激活环境：. my_venv/bin/activate  (. 或者 source )
$ 退出环境：deactivate 

Windows系统运行cmd，使用 "py" Python 启动器命令配合 "-m" 开关选项:
$ 创建环境：py -3 -m venv my_venv (或者python -m venv my_venv)
$ 创建指定环境：py -3.6 -m venv my_venv,  py -3.7 -m venv my_venv (添加到系统环境变量中)
$ 激活环境：my_venv\Scripts\activate.bat
$ 退出环境：deactivate

执行后，会在目录前方出现<my_venv>表明已进入虚拟环境

安装项目:
$ pip install -r requirements.txt
```

### 方法二：Windows在PyCharm下创建虚拟环境
1. 安装并激活PyCharm
这个请自行安装
官方地址：https://www.jetbrains.com/pycharm/

2. 在PyCharm下创建虚拟环境
第一步：点击New Project
第二步：选择下图的New environment
第三步：点击create即可
pycharm会为新创建的项目自动建立一个虚拟环境


### 方法三：conda创建虚拟环境

[anaconda中的常用操作](https://blog.csdn.net/CampusAmour/article/details/83215524)


Linux下启动其终端命令行 
$ source ~/anaconda3/bin/activate root
$ anaconda-navigator

- 创建虚拟环境，conda create -n env_name python=3.6

- 同时安装必要的包，conda create -n env_name numpy matplotlib python=3.6

- 激活虚拟环境
  - Linux：source activate your_env_name(虚拟环境名称)
  - Windows：activate your_env_name(虚拟环境名称)

- 退出虚拟环境： 
  - Linux：source deactivate your_env_name(虚拟环境名称)
  - Windows：deactivate your_env_name(虚拟环境名称)

- 删除虚拟环境，conda remove -n your_env_name(虚拟环境名称) --all
- 删除包使用命令，conda remove --name $your_env_name  $package_name（包名)


conda常用命令
- 查看已安装的包，conda list
- 安装包，conda install package_name(包名)
- 查看当前存在的虚拟环境，conda env list 或 conda info -e
- 检查更新当前conda，conda update conda
