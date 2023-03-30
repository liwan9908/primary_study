import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals=[]
f=open("data.txt")
for line in f:
    #得到的是字符串
    line=line.replace("\n","")#吧换行符转换为空字符串
    datals.append(list(map(eval,line.split(","))))
#用，隔开，并生成一个列表，map,将第一个函数的功能作用于第二个参数的每一个元素
f.close()
#自动控制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    #设置当前画笔颜色
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
    
