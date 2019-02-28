# coding = utf-8

"""

https://github.com/onevcat/FengNiao

① 使用此脚本前，运行机首先需要安装 FengNiao。


> fengniao --help

  -p, --project:
      Root path of your Xcode project. Default is current folder.
  --force:
      Delete the found unused files without asking.
  -e, --exclude:
      Exclude paths from search.
  -r, --resource-extensions:
      Resource file extensions need to be searched. Default is 'imageset jpg png gif'
  -f, --file-extensions:
      In which types of files we should search for resource usage. Default is 'm mm swift xib storyboard'
  --version:
      Print version.
  -h, --help:
      Print this help message.


A more daily-work usage under a project could be:

> fengniao --project . --exclude Carthage Pods


How it works:

1、Extract resource file names (default file type: ["imageset", "jpg", "png", "gif"])
    in these folders ["imageset", "launchimage", "appiconset", "bundle”].

2、Use regular expression to search all string names
    in files (default files type: ["m", "mm", "swift", "xib", "storyboard", "plist"]).

3、Exclude all used string names from resources files, we get all unused resources files.

"""

import os


# 需要根据项目位置修改路径，默认过滤图片类型包括 gif、jpg、png
# project_path 可在 shell 脚本中修改

def check():

    check_result = os.popen("/Users/william/PycharmProjects/System/Mobile/iOS/iOS_Package_Check/fengniao.sh")\
        .readlines()

    if "you have no unused resources" in check_result[2]:

        print("you have no unused resources!")
        return "Congratulations, you have no unused resources!!!", " "
    else:
        # 未使用的图片总数
        unused_file_num = int(check_result[2].split()[0])
        # Check 概要
        print(check_result[2])
        # 图片位置详情
        # print(check_result[4:4+unused_file_num])
        # 对 check_result[4: 4+unused_file_num] 元素进行累加
        unused_path = " ".join(check_result[4: 4+unused_file_num])

        return check_result[2], unused_path


if __name__ == '__main__':

    check()
