import os

import numpy
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

diognestic_map = {'0':
                      ['0', '0_left.jpg', '0_right.jpg', 'cataract	normal fundus'],
                  '1': ['1', '1_left.jpg', '1_right.jpg', 'normal fundus	normal fundus'],
                  '2': ['2', '2_left.jpg', '2_right.jpg',
                        'laser spot，moderate non proliferative retinopathy	moderate non proliferative retinopathy'],
                  '3': ['4', '4_left.jpg', '4_right.jpg',
                        'macular epiretinal membrane	mild nonproliferative retinopathy'],
                  '5': ['5', '5_left.jpg', '5_right.jpg',
                        'moderate non proliferative retinopathy	moderate non proliferative retinopathy'],
                  '6': ['6', '6_left.jpg', '6_right.jpg',
                        'macular epiretinal membrane	moderate non proliferative retinopathy，epiretinal membrane'],
                  '7': ['7', '7_left.jpg', '7_right.jpg', 'drusen	mild nonproliferative retinopathy'],
                  '8': ['8', '8_left.jpg', '8_right.jpg', 'normal fundus	normal fundus'],
                  '9': ['9', '9_left.jpg', '9_right.jpg', 'normal fundus	vitreous degeneration'],
                  '10': ['10', '10_left.jpg', '10_right.jpg', 'epiretinal membrane	normal fundus'],
                  '11': ['11', '11_left.jpg', '11_right.jpg',
                         'moderate non proliferative retinopathy，hypertensive retinopathy	moderate non proliferative retinopathy，hypertensive retinopathy'],
                  '13': ['13', '13_left.jpg', '13_right.jpg', 'pathological myopia	pathological myopia'],
                  '14': ['14', '14_left.jpg', '14_right.jpg', 'normal fundus	macular epiretinal membrane'],
                  }

data = pd.read_csv("static/data.csv")

@app.route('/')
def home():
    # Delete old files
    dir_name = "static/images/samples/"
    fuul_path = os.listdir(dir_name)
    for item in fuul_path:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_name, item))

    return render_template("index.html", res="None")


#
# @app.route('/predictdisease', methods=['POST'])
# def predictdisease():
#     # Delete old files
#     dir_name = "static/images/xray/"
#     fuul_path = os.listdir(dir_name)
#     for item in fuul_path:
#         if item.endswith(".jpg"):
#             os.remove(os.path.join(dir_name, item))
#
#     app_root = request.host_url
#     file = request.files['img']
#     filename = file.filename
#     save_path = "{0}{1}".format("static/images/xray/", filename)
#     url_save_path = "{0}{1}".format("images/xray/", filename)
#     file.save(save_path)
#
#     model = Model()
#     res = model.predict(save_path)
#     return render_template("index.html", res=res, url_save_path=url_save_path, app_root=app_root)


##-------- Demo ------- ##
@app.route('/predictdisease', methods=['POST'])
def predictdisease():
    # Delete old files
    dir_name = "static/images/samples/"
    fuul_path = os.listdir(dir_name)
    for item in fuul_path:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_name, item))

        app_root = request.host_url
    url_save_path = "{0}".format("images/samples/")

    # Right eye
    right_file = request.files['r_img']
    right_filename = right_file.filename
    r_save_path = "{0}{1}".format("static/images/samples/", right_filename)
    right_file.save(r_save_path)

    # Left eye
    left_file = request.files['l_img']
    left_filename = left_file.filename
    l_save_path = "{0}{1}".format("static/images/samples/", left_filename)
    left_file.save(l_save_path)

    row = data.loc[data['filename'] == right_filename]

    # Right eye
    r_res = numpy.array([row['Right-Fundus'], row['Right-Diagnostic Keywords']])
    r_res = r_res.flatten()

    # Left eye
    l_res = numpy.array([row['Left-Fundus'], row['Left-Diagnostic Keywords']])
    l_res = l_res.flatten()


    return render_template("index.html", r_res=r_res, l_res=l_res, url_save_path=url_save_path, app_root=app_root)


if __name__ == '__main__':
    app.run()
