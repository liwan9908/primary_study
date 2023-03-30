import jieba
txt = open ("三国演义.txt","r",encoding="utf-8").read()#读取txt
excludes={"将军","却说","荆州","二人","不可","不能","如此"}
words=jieba.lcut(txt)#用jieba库精确分词，然后返回列表
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word =="诸葛亮" or word =="孔明曰":
        reword="孔明"
    elif word =="关公" or word =="云长":
        reword="关羽"
    elif word =="玄德" or word =="玄德曰":
        reword="刘备"
    elif word =="孟德" or word =="丞相":
        reword="曹操"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{:<10}{:>5}".format(word,count))
    
