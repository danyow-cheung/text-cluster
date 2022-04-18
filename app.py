from concurrent.futures import thread
from grpc import server
import numpy as np
from flask import Flask, request,render_template
from os import path
import matplotlib.pyplot as plt
from word_cut import split_main
from calculate_sim import simlaritycalu_main
from text_cluster import recommed_main
from gevent import monkey,pywsgi
from gevent.pywsgi import WSGIServer
import random

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
        print('捕捉消息')
        title = request.form['movie_title']
      
        print(title)
        print(type(title))
        # recommed_main(title)
        # file = open('utils/recommend.txt')
        # line = file.readline()
        # data = []
        # while line:
        #     data.append(line)
        #     line = file.readline()
        # print("type(data)",type(data))

        # random_output = random.sample(data,10) 
        return render_template("result.html")
        # return render_template("recommend.html",result=random_output)

    else:
        print("捕捉不到")
        return render_template("recommend.html")

@app.route('/result',methods=["POST","GET"])
def result_list():
    if request.method =='POST':
        '''
            实现功能：
                根据输入，输出相关的电影推荐
            '''
        title = request.form['movie_title']
        print(title)
        print(type(title))
        recommed_main(title)
        file = open('utils/recommend.txt')
        line = file.readline()
        data = []
        while line:
            data.append(line)
            line = file.readline()
        print("type(data)",type(data))

        random_output = random.sample(data,10) 
        return render_template("result.html",result= random_output)
    else:
        render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    # app.run(threaded=True)
    # server = pywsgi.WSGIServer(("0.0.0.0",8080),app)
    # server.serve_forever()
