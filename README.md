# text-cluster
基于内容的文本聚类，使用Kmeans进行电影推荐

文件结构：
｜--js:网页js文件
｜--static:网页静态文件
｜--templates:可视化的前端页面
｜--utils:存放样本所属的簇文件，推荐电影文件和停用词文件
｜--workspace:存放相关语义分析的文件
｜--test_cluster.ipynb:对语料库进行训练，生成模型。产生电影名称对应的类别标签文件
｜--app.py:网页端入口
｜--text_cluster.py:导入名称标签文件，对应输入输出相应的电影
｜--calculate_sim.py:计算两段文本的相似度函数
｜--word_cut.py:对输入本文进行数据预处理函数


