# -*- coding: utf-8 -*-
import argparse
import File
import os


def copy(source, target):
        target_dir = target
        root_name = os.path.basename(source)
        print('目标工程名称:' + root_name)
        print('源目录:' + source)
        jump_name = ['.gitignore', '.project', '.svn', 'build', '.idea', '.gradle']
        if target[-1:] != '\\':
            target = target+'\\'
        target = target + root_name
        print('目标目录:' + target)
        root_file = File.File(source)
        target_root_file = File.File(target)
        if not target_root_file.exists():
            target_root_file.makedirs()
        else:
            target_root_file.delete()
            target_root_file.makedirs()
        for child in root_file.listFile():
            name = child.getName()
            if name in jump_name:
                continue
            if child.isFile():
                t = target + '\\' + name
                print(t)
                child.copyFile(target + '\\' + name)
            else:
                for n2 in child.listFile():
                    name2 = n2.getName()
                    if name2 in jump_name:
                        continue
                    chi = File.File(target + '\\' + name)
                    if not chi.exists():
                        chi.makedirs()
                    t = target + '\\' + name + '\\' + name2
                    print(t)
                    if n2.isFile():
                        n2.copyFile(t)
                    else:
                        n2.copyTree(t)
        File.pack(target, 'zip', target)
        target_root_file.delete()
        # print("target:" + 'explorer /e,/select,"' + target + '.zip"')
        # 直接选中目标文件, 但经常被安全软件误报是风险操作
        # os.system('explorer /e,/select,"' + target + '.zip"')
        print("target: explorer " + target_dir)
        os.system('explorer ' + target_dir)
        print(('-' * 15) + 'Finish' + ('-' * 15))


def main():
    parser = argparse.ArgumentParser(
        prog="aspjcp", description="AS工程复制工具, 自动排除'.gitignore', "
                                  "'.project', '.svn', 'build', "
                                  "'.idea', '.gradle'文件夹，有效减小工程体积。免去人工复制时删除不相干文件和压缩的麻烦。")
    parser.add_argument("source", type=str, help="待复制的Android Studio工程目录")
    parser.add_argument("target", type=str, help="放置ZIP包的文件路径")
    args = parser.parse_args()
    root_file = File.File(args.source)
    if not root_file.exists():
        print('待复制的Android Studio工程目录:%s' % args.source)
        exit(-1)
    root_file = File.File(args.target)
    if not root_file.exists():
        root_file.mkdirs()
    copy(args.source, args.target)


if __name__ == '__main__':
    main()
