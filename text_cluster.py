# -*- coding: UTF-8 -*-
import jieba
import logging
import codecs
import traceback
import gensim
from sklearn.cluster import KMeans
from collections import Counter
from sklearn import metrics
import os
import matplotlib.pyplot as plt
import re 


# 接下來只需要捕獲到 輸入的名稱與语料库的内容，比较选出都是类别为same的名字就好了
rate_lst = []
# 导入经过label之后的电影标题txt文件
with codecs.open("utils/cluster_dockmResulttag.txt", 'r', encoding='UTF-8') as f:
    for i in f:
        rate_lst.append(i)
        # print(i)    
test_txt = ""
def recommed_main(test_txt):
    count = 0
    recommend_list = []
    label = ''
    for i in rate_lst:
        # type : i -> str
        
        if test_txt in i:
            # 该电影名称在数据库中
            print("电影存在于数据库中")
            test_txt_label = re.findall(r"\d",i)
            txt_label = str(test_txt_label)
            # print("该电影的类别为\n",test_txt_label) ['2']
        
            label = txt_label.replace("['","").replace("']","")      
            print("label:",label)

        if label  in i:
            count += 1
            recommend_list.append(i)

    print("匹配总数",count)
    # print("推荐电影",recommend_list)
    #逐行写入文件
    with open("utils/recommend.txt","w")as f:
        for i in recommend_list:
            f.write(str(i))

    return recommend_list