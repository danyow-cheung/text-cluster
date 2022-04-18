# text-cluster
基于内容的文本聚类，使用Kmeans进行电影推荐

**注意事项**
解决windows乱码情况：
1. text_cluster.py中的recommend_main（）函数中的codes.open()添加参数 [encoding="utf-8"]
2. app.py 中的diy_txt（）函数with open()添加参数 [encoding="utf-8"]
