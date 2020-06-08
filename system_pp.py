from flask import Flask, render_template, request, url_for
import os
import json
import csv
import re
import string
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump, load
from preprocess import predict_precess
import pandas as pd
from src.classification import *
from src.label_pre import *
from werkzeug.utils import secure_filename, redirect
from src.util import MySQLCon, get_label_count
from out_attention import get_han_result


label_list = ["Introductory", "How We Collect and Use Your Information", "Cookies and Similar Technologies",
              "Third Party Sharing and Collection", "What You Can Do", "How We Protect Your Information",
              "Data Retention", "International Data Transfer", "Specific Audiences", "Policy Change",
              "Contact Information"]
app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')
@app.route('/',methods=['POST', 'GET'])
def index():
    result = []
    label_num =[]
    result1 = []
    label_num1 =[]

    if request.method=='POST':
        f = request.files['file']
        basedir = os.path.abspath(os.path.dirname(__file__))  # 本项目所在目录
        # file_path ="F:\system_pp02\static/uploads"
        upload_path = os.path.join(basedir, 'static/uploads')  # 文件所要存放的目录
        # 因为filename是客户端post进来的，因此它视可以伪造的，
        # 故而，应该调用工具模块

        file = f.read()
        file_data= file.decode()
        f.save(os.path.join(upload_path, secure_filename(f.filename)))

        p, data, w_att_result = get_han_result(file_data)
        # p, data = get_SVM(file_data)

        con = MySQLCon(user='root', password='', host='localhost', port='3306', database='gplay')
        app_info = con.get_app_info(app_id=1)
        info = {"app_name": app_info['app_name'], "star": app_info["star"],
                "install_num": app_info['install_num'], "offer": app_info['offer'],
                "update_time": app_info['update_time'], "pp_link": app_info['privacy_policy_link'],
                "description": app_info['description']}

        category_info = get_label_count(user='root', password='', host='localhost', port='3306', database='gplay', category='all')
        for i, value in enumerate(p):
            result_dict = {'review': data[i].strip(), "label": str(value), "word_weight": str(w_att_result[i])}

            result.append(result_dict)
            label_num.append(str(value))

        # for i, value in enumerate(p1):
        #     result_dict = {'review': data1[i].strip(), "label": str(value)}
        #
        #     result1.append(result_dict)
        #     label_num1.append(str(value))

        label_set = set(label_num)
        print(label_set)
        dict_num ={}
        for item in label_num:
            dict_num.update({'label_'+item: round(label_num.count(item) / len(label_num), 2)})

        label00(dict_num)
        label01(dict_num)
        label02(dict_num)
        label03(dict_num)
        label04(dict_num)
        label05(dict_num)
        label06(dict_num)
        label07(dict_num)
        label08(dict_num)
        label09(dict_num)
        label10(dict_num)
        print((dict_num))
        return render_template('visualization.html', name=json.dumps(result), info=info, category_info=category_info, label_setnum=dict_num)
    return render_template('index.html')
@app.route('/data',methods=['POST', 'GET'])
def data():
    return render_template('data.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
