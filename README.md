<p align="center">
<a href="https://travis-ci.org/onevcat/FengNiao"><img src="https://img.shields.io/travis/onevcat/FengNiao/master.svg"></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/swift-4.0-brightgreen.svg"/></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/SPM-ready-orange.svg"></a>
<a href="https://raw.githubusercontent.com/onevcat/Kingfisher/master/LICENSE"><img src="https://img.shields.io/cocoapods/l/Kingfisher.svg?style=flat"></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/platform-macos%20|%20Linux-blue.svg"/></a>
<a href="https://codecov.io/gh/onevcat/Hedwig"><img src="https://codecov.io/gh/onevcat/Hedwig/branch/master/graph/badge.svg"/></a>
</p>

<p align="center">
<img src="https://github.com/xinzhen2015/iOS_Check/blob/master/iOS_Package_check/WechatIMG18.png" alt="iOS_Check" title="iOS_Check"/>
</p>


## What

iOS_Check is a simple command-line util to deleting unused image resource files from you Xcode project and generate reports.

## How

### First installation

You need Swift Package Manager (as well as swift compiler) installed in your macOS, generally you are prepared if you have the latest Xcode installed.

Compile from source:

```shell
> git clone https://github.com/onevcat/FengNiao.git
> cd FengNiao
> ./install.sh
```
FengNiao should be compiled, tested and installed into the /usr/local/bin.

FengNiao supports some arguments, you could find it by:

```shell
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
```

### Usage

```markdown
# 1、You just have to replace the project path in 【fengniao.sh】.
```
```shell
#! /usr/bin/expect

spawn fengniao -p preject_path -r jpg JPG jpeg png gif imageset

expect {

 "(l)ist|(d)elete|(i)gnore" { send "l\n"}

 "you have no unused resources in path" {send "\n"}

        }

expect eof

exit
```

```markdown
# 2、run 【produce_html.py】 and you can get the report.
```
