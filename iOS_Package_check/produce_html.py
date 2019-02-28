# coding=utf-8

from bottle import template
from package_check import check

summary, detail = check()


"""
    使用bottle来动态生成html
"""

# 一些我们需要展示的文章题目和内容
ios_check = [("HuXiu APP", summary, detail, "https://github.com/xinzhen2015")]

# 定义想要生成的Html的基本格式
# 使用%来插入python代码
report = """

<html>
    <head><h1 style="text-align:center; color:#ffce37"> iOS Unused File Check </h1></head>
    <title>iOS_Check</title>
    
    <body bgcolor="#000000">
    
    % for title, detail0, detail1, link in items:
        <h2> {{title.strip()}} </h2>
        <p style="font-size:22;color:#2ccb39"> {{detail0}} </p>
        <PRE> <p style="font-size:18;color:#ff3d80"> {{detail1}} </p></PRE>    
        <a href={{link}}>Powered By XinZhen</a>
    %end
       
    </body>
</html>

"""

html = template(report, items=ios_check)

with open("report.html", 'w', encoding="utf-8") as f:

    f.write(html)



