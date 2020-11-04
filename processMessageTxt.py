# -*- coding: utf-8 -*- 
# @Time : 2020/10/31 10:35 
# @Author : byp 
# @File : processMessageTxt.py

import sys
messageDir = "./data/messageDir/"


def processI4(input_filename):
    fin = open(messageDir + input_filename, "r", encoding='utf8')
    fout = open(messageDir + "__" + input_filename, "w", encoding='utf8')

    nCol=0  #计数器--行数
    for line in fin.readlines():
        if line[0] == '-' and line[1] == '-' or nCol == 0:
            nCol += 1
            pass
        else:
            str = line[55:].lstrip()
            fout.write(str)
            nCol += 1




def processQQ(input_filename):
    fin = open(messageDir + input_filename, "r", encoding='utf8')
    fout = open(messageDir + "__" + input_filename, "w", encoding='utf8')
    for line in fin.readlines():
        if len(line) > 0:
            if line[0] == '2' and line[1] == '0' or (line[:4] == "http") or (line == "[图片]"):
                pass
            else:
                fout.write(line)



def processLouyue(input_filename):
    fin = open(messageDir + input_filename, "r", encoding='utf8')
    fout = open(messageDir + "__" + input_filename, "w", encoding='utf8')
    # 通过空格来筛选
    for line in fin.readlines():
        if line[0] == " ":
            fout.write(line.lstrip())
        else:
            pass


def test():
    # txt = "李小玉_20201103_222047.txt"
    # processWechat(txt)
    txt="Aurora_20201104_113135.txt"
    processI4(txt)

if __name__ == '__main__':
    test()
    if len(sys.argv) == 2:
        processI4(sys.argv[1])
    else:
        print('[usage] <input>')