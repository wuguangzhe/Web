from time import *

"""
   前景色            背景色            颜色
   --------------------------------------------
     30                40              黑色
     31                41              红色
     32                42              绿色
     33                43              黃色
     34                44              蓝色
     35                45              紫色
     36                46              青色
     37                47              白色
     90                100             亮黑
     91                101             亮红
     92                102             亮绿
     93                103             亮黃
     94                104             亮蓝
     95                105             亮紫
     96                106             亮青
     97                107             亮白
     
   显示方式         清除代码           意义
   --------------------------------------------
      0                --              终端默认设置
      4                24              使用下划线
      7                27              反白显示
      8                28              不可见
    
    
    光标设置 格式:\\033[数字+字母,数字、字母如下所示
    
    字母              数字             意义
   --------------------------------------------
     A                 x               光标上移x行
     B                 x               光标下移x行
     C                 x               光标左移x列
     D                 x               光标右移x列
     H                 y,x             光标设置为(x,y)(注意顺序)
     K                 无              清除从光标到行尾的内容
     s                 无              保存光标位置
     u                 无              回复光标位置
     l                 ?25             隐藏光标
     h                 ?25             显示光标
     J                 2               清屏(但不会恢复光标)
"""


def replace(strname, *w):
    for x in w:
        strname = strname.replace(x[0], x[1])
    return strname


def print(*w, t=0.05, end="\n", sepr=" "):
    import sys
    import time
    str_all = ""

    for x in w:

        if w.index(x) == len(w) - 1:
            str_all += str(x)
        else:
            str_all += str(x) + sepr
    str_all = replace(str_all, ("\\黑", "\033[30m"),
                      ("\\红", "\033[31m"),
                      ("\\绿", "\033[32m"),
                      ("\\黄", "\033[33m"),
                      ("\\蓝", "\033[34m"),
                      ("\\紫", "\033[35m"),
                      ("\\青", "\033[36m"),
                      ("\\白", "\033[37m"),
                      ("\\b红", "\033[41m"),
                      ("\\b绿", "\033[42m"),
                      ("\\b黄", "\033[43m"),
                      ("\\b蓝", "\033[44m"),
                      ("\\b紫", "\033[45m"),
                      ("\\b青""\033[46m"),
                      ("\\b白", "\033[47m"),
                      ("\\b黑", "\033[40m"),
                      ("\\", "\033[0m"))

    for y in str_all:
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write(end)


def print_lines(*w, t=0.05, line_end="\n", sepr="", line_t=0.1):
    import sys
    import time
    for x in w:
        if w.index(x) == len(w) - 1:
            print(str(x), t=t, end=line_end)
        else:
            print(str(x), t=t, end=line_end)
            sys.stdout.write(sepr)
            time.sleep(line_t)


def show_img(url, prin="正在显示文件（没看见的去任务栏找）", inpu=" 看/运行 完点【ENTER】键："):
    print(prin)
    import os
    os.system(url)
    input(inpu)


print("欢迎来到《爆笑课文改编（1）》")
sleep(0.8)
print("即将开始，请不要吃饭或喝水，以免呛到\n")
sleep(0.8)
print("原文：")
sleep(0.8)
print("两个黄鹂鸣翠柳，一行白鹭上青天。\n窗含西岭千秋雪，门泊东吴万里船。", t=0.05)
print("\n\n")
print("改编：")
sleep(0.8)
print("两个黄鹂谈恋爱，一行白鹭来捣蛋。\n黄鹂拿出手榴弹，所有白鹭全完蛋。\n", t=0.05)
sleep(8)
print("原文：")
sleep(0.8)
print("马宝玉抢前一步，夺过手榴弹插在腰间，猛地举起一块大石头，大声喊道：“同志们！用石头砸！”顿时，石头像雹子一样，带着五位壮士的决心，带着中国人民的仇恨，向敌人头上砸去。\n\n", t=0.03)
sleep(0.8)
print("改编：")
sleep(0.8)
print("学渣抢前一步，夺过作业插在腰间，猛地举起一个大书包，大声喊道：“同学们！用书包砸！”顿时，书包像雹子一样，带着所有同学的决心，带着中国学生的仇恨，向老师头上砸去。\n", t=0.03)
sleep(20)
print("原文：")
sleep(0.8)
print("老汉沙哑地喊话：“桥窄！排成一队，不要挤！党员排在后边！” 有人喊了一声：“党员也是人。” 老汉冷冷地说：“可以退党，到我这儿报名。”\n\n", t=0.03)
sleep(0.8)
print("改编：")
sleep(0.8)
print("老师沙哑地喊话：“校门窄！排成一队，不要挤！学生排在后边！”有人喊了一声：“学生也是人。” 老师冷冷地说：“可以退学，到我这儿报名。”“我要退学！我要退学！”\n", t=0.03)
sleep(15)
print("《爆笑课文改编(1)》结束了，如果你觉得好笑，请点个赞并在评论区回复“我笑了”")
