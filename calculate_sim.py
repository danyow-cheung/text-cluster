import codecs
import numpy as np
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
import jieba 

'''
为词向量相似度计算代码
    simlaritycalu(x1,x2) :通过【余弦距离】计算两个向量的相似度
'''
def simlarityCalu(vector1,vector2):
    # np.sqrt : 按元素返回数组的非负平方根。
    vector1Mod = np.sqrt(vector1.dot(vector1))
    print("1",vector1Mod)
    vector2Mod = np.sqrt(vector2.dot(vector2))
    print("2",vector2Mod)
    if vector2Mod != 0 and vector1Mod != 0:
        # 余弦公式计算代码
        simlarity = (vector1.dot(vector2)) / (vector1Mod*vector2Mod)
    else:
        simlarity = 0
    return simlarity


'''
文档向量化  
    参考于官网Doc2Vec模型
'''
def doc2vec(file_name):
    '''
    获得原始文件
    '''
    # codecs :一种编解码器 类似于open
    doc = [w for x in codecs.open(file_name,'r','utf-8').readlines() for w in jieba.cut(x.strip())]
    print("原始样本为:\n",doc)
    
    '''
    初始化和训练模型：对原始数据进行标签化
    '''    
    # TaggedDocument : 遍历包含文档的文件：
    #  预计单词已经过预处理并由空格分隔。文档标签是根据文档行号自动构建的
    # （每个文档都有一个唯一的整数标签）。
    documents  = [TaggedDocument(doc,[i]) for i ,doc in enumerate(doc)]

    # print("documents\n",documents)

    
    # Doc2Vec : 
    #   documents :     可迭代的taggedDocument列表
    #   vector_size :   特征向量的维度
    #   window:         句子中当前单词和预测单词之间的最大距离。
    #   min_count :     忽略总频率低于此值的所有单词
    #   workers :       使用这些n个工作线程来训练模型

    #   dm:             定义训练算法。如果dm=1，则使用“分布式内存”（PV-DM）。
    #                   否则，使用分布式词袋（PV-DBOW）
    model = Doc2Vec(documents,dm=1,vector_size=5,window=2,min_count = 1,workers=4)
    
    model.build_vocab(documents, update=False)


    # infer_vector:     为给定的批量训练文档推断向量。
    # return：          新文档的推断段落向量
    doc_vec_all = model.infer_vector(doc)
    
    return doc_vec_all
    # return documents


def simlaritycalu_main():
    # 导入数据
    p1 = 'workspace/preprocessing/text00.txt'
    p2 = 'workspace/preprocessing/text01.txt'
    # 生成词向量
    p1_doc2vec = doc2vec(p1)
    p2_doc2vec = doc2vec(p2)
   

    # 
    similarity_needed = simlarityCalu(p1_doc2vec,p2_doc2vec)
    print("sim 相似度为：",similarity_needed)

    return similarity_needed

