import numpy as np
from flask import Flask, request,render_template
from os import path
import matplotlib.pyplot as plt
from word_cut import split_main
from calculate_sim import simlaritycalu_main
from text_cluster import recommed_main


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diy",methods=["POST","GET"])
def diy_txt():
    if request.method == "POST":
        '''
        实现功能：
            输入两段文本 进行相似度计算
        '''
        text01 = request.form['text1']
        text02 = request.form['text2']

        print("1:\n",text01)
        print("2:\n",text02)
        
        # 捕捉到的内容写入workspace的原始数据文件夹下
        with open ("workspace/origin/text01.txt","w") as a,open("workspace/origin/text02.txt","w") as b:
            a.write(text01)
            b.write(text02)
        
        # 调用预处理函数, 处理原始数据
        split_main()

        # 调用计算相似度函数
        similarity_needed = simlaritycalu_main()

        # print("【app】相似度为 ",similarity_needed)
        
        return render_template("diy.html",result=similarity_needed)
    else:
        return render_template("diy.html")


@app.route('/recommend',methods=["POST","GET"])
def movie_recommend():

    if request.method == "POST":
        title = request.form['title']
        print(type(title))
        print(title)
        recommed_main(title)
        return render_template("result.html")

    else:
         return render_template("recommend.html")

@app.route('/result',methods=["POST","GET"])
def result_list():
    if request.method =='POST':
        '''
            实现功能：
                根据输入，输出相关的电影推荐
            '''
        file = open('utils/recommend.txt')
        line = file.readline()
        data = []
        while line:
            data.append(line)
            line = file.readline()
        print("type(data)",type(data))
        return render_template("result.html",result= data[:10])
    else:
        render_template("index.html")

if __name__ == "__main__":
    
    # app.secret_key = "super secret key"
    # app.config['SESSION_TYPE'] = 'filesystem'
    # # sess.init_app(app)
    app.run(debug=True)