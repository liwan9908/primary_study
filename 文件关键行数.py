counts={}
s=0
with open("latex.log","r",encoding="utf-8") as f:
    fi=f.readlines()
    for i in fi:
        counts[i]=counts.get(i,0)+1
    for value in counts.values():
        if value==1:
            s+=1
print("共{}关键行".format(s))
        
        
