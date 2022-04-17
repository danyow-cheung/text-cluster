import jieba
import glob
'''
    对原始数据进行预处理，包括去除空格，停用词的使用
    一次性全部处理
'''
files  = glob.glob("workspace/origin/*.txt")
#数据的读取和预处理
def get_content(file):
    with open(file,'r',encoding='utf-8') as f:
        # 变量content存储，预处理之后的内容
        content = ''
        for i in f:
            i = i.strip()
            i = i.replace(" ","")
            content += i
    return content


def stop_words(path):
    # 使用停用词语，对样本进行更准确的处理
    with open(path,encoding='utf-8') as f:
        return [l.strip() for l in f]

def split_main():
    # 循环遍历文件内容
    for i in range(len(files)):

        corpus = [get_content(x) for x in files]
        # 调用存储在utils工具文件夹的停用词文件

        split_words = [x for x in jieba.cut(corpus[i]) if x not in stop_words('utils/stop_words.utf8')]
        # print('样本分词效果：\n'+'/ '.join(split_words))
        
        split_words = str(split_words)
        # 保存经过数据处理的文件
        save_txt = "workspace/preprocessing/text%02d.txt"%i
        # 经过分词和停用词语处理之后再次写入文件
        with open (save_txt,"w",encoding="utf-8") as f:
                f.write(split_words)
    