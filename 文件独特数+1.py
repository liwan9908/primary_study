f = open("latex.log")
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))
#记住：如果需要"去重"功能，请使用集合类型。

l#s.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现
