f = open("latex.log")
cc = 0
d = {}#创建一个字典
for i in range(26):#遍历26次
    d[chr(ord('a')+i)] = 0#取26个字母的排序
for line in f:#遍历循环文件每行
    for c in line:#遍历循环每行中的每个字母
        d[c] = d.get(c, 0) + 1#字典中统计每个字母的个数\
        #每循环一个单词，记录一次并形成键值对
        cc += 1#记录所有字符个数，遍历循环了几次
print("共{}字符".format(cc), end="")#格式表达
for i in range(26):
    if d[chr(ord('a')+i)] != 0:#如果值不等于零
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")
        #打印出键和值
