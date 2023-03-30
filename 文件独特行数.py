f=open("latex.log")
counts={}
s=0
for line in f:
    counts[line]=counts.get(line,0)+1
for value in counts.values():
    if value!=0:
        s+=1
print("共{}行".format(s))

    

#记住：如果需要"去重"功能，请使用集合类型。

#ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现
