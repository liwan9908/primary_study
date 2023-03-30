f=open("latex.log")
s=0
c=0
for line in f:
    line=line.strip("\n")
    if line!="":
        c+=1
        l=len(line)
        s+=l
print(round(s/c))
    
        
    
