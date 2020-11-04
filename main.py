# -*- coding: utf-8 -*- 
# @Time : 2020/11/2 7:55 
# @Author : byp 
# @File : main.py
import sys
from processMessageTxt import processI4,processQQ,processLouyue
from wordCloud import generateWC


# 输入

sInputInfo='''
请按如下方式输入：
1.选择是通过何种工具生成的聊天记录，PC版QQ输入0，I4导出输入1，楼月导出输入2
2.消息文件名称，储存于messageDir
3.mask_name，即生成词云的底图，最好选择边界清晰、且大小较小（不宜超过100k）的图片，例如白底、黑底之类的，储存于maskDir
4.output_name，指定输出文件的名称，储存于outputDir
5.font_path='C:/Windows/Fonts/msyh.ttc' 字体设置，默认为微软雅黑
xin
'''

if __name__ == "__main__":
    if len(sys.argv) == 6:
        if sys.argv[1]=="0":
            processQQ(sys.argv[2])
            generateWC("__"+sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        else:
            if sys.argv[1]=="1":
                processI4(sys.argv[2])
                generateWC("__"+sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            else:
                processLouyue(sys.argv[2])
                generateWC("__" + sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif len(sys.argv) == 5:
        if sys.argv[1]=="0":
            processQQ(sys.argv[2])
            generateWC("__"+sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            if sys.argv[1] == "1":
                processI4(sys.argv[2])
                generateWC("__"+sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                processLouyue(sys.argv[2])
                generateWC("__"+sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(sInputInfo)