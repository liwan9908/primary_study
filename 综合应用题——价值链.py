#
# 请在此文件作答
#
import jieba
dict_words = {}
with open('data3.txt', 'r', encoding='GBK') as f:
    txt=f.read()
    words=jieba.cut(txt)
    for word in words:
        if len(word)<2:
            continue
        else:
            dict_words[word]=dict_words.get(word,0)+1
    st=list(dict_words.items())
    st.sort(key=lambda x:x[1],reverse=True)
    for i in range(10):
        k,v=st[i]
        print("{}:{}".format(k,v))
            
