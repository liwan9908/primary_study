import jieba
txt = open ("三国演义.txt","r",encoding="utf-8").read()#读取txt
words=jieba.lcut(txt)#用jieba库精确分词，然后返回列表
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{:<10}{:>5}".format(word,count))
    
