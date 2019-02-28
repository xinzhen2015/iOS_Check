<p align="center">
<img src="https://raw.githubusercontent.com/onevcat/FengNiao/assets/logo.png" alt="FengNiao" title="FengNiao" width="468"/>
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
### 1、You just have to replace the project path in fengniao.sh.
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
### 2、run produce_html.py and you can get the report.
```
