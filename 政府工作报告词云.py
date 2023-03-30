import jieba
import wordcloud
from imageio import imread
mask = imread("fivestar.png")
f=open("新时代中国特色社会主义.txt","r",encoding="utf-8")#打开文件，并转格式
t=f.read()#读取文件
f.close()#关闭文件
ls=jieba.lcut(t)#结巴分词
txt="".join(ls)#加入txt列表
w=wordcloud.WordCloud(  font_path ="msyh.ttc",mask=mask,width=1000,height=700,\
                      background_color="white",max_words=200)
w.generate(txt)#对txt列表进行词云操作
w.to_file("3.png")
