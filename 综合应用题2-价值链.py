#
# 请在此文件作答
#

import jieba    #加载jieba库
import re       #加载re正则库
dict_words = {} #创建字典
with open('data3.txt', 'r', encoding='GBK') as f: #打开文件为可读，并赋值给f
    senses =  re.sub('([，。\n])', '|' , f.read())
    #在一个字符串中替换所有
    #匹配正则表达式的字串，返回替换后的字符串
k = jieba.cut(senses)
for i in k:
    if len(i) >= 2:
        dict_words[i] = dict_words.get(i, 0) + 1
data = sorted(dict_words.items(), key=lambda x:x[1], reverse=True)
with open('out.txt', 'w') as f:
    for sense in senses.split('|'):
        if data[0][0] in sense:
            f.write(sense+ '\n')
