# Android Studio 工程复制打包命令行工具
## 命令行的使用

1. 下载release目录下文件;
2. 双击asc.bat或者执行命令: asc  {需要复制的工程路径}
3. 复制完成，Explorer将自动打开目标目录；



## 二次开发

1. 下载src目录下文件；
2. 安装Python环境；
3. 安装Pyinstaller；
4. 修改源码；
5. 点击build_aspjcp.bat编译。



## 命令行用法

```
usage: aspjcp [-h] source target

AS工程复制工具, 自动排除'.gitignore', '.project', '.svn', 'build', '.idea',
'.gradle'文件夹，有效减小工程体积。免去人工复制时删除不相干文件和压缩的麻烦。

positional arguments:
  source      待复制的Android Studio工程目录
  target      放置ZIP包的文件路径

optional arguments:
  -h, --help  show this help message and exit
```



## License

```
Copyright 2020 Chock Qiu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

