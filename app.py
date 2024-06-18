# write a simple flask app
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def render():
    data = {  # dict
        'path_img0':'/static/image/GanCao.png',
        'path_img1':'/static/image/ChuanXiong.png',
        'path_img2':'/static/image/FangFeng.png',
        'prob0_0':'97',
        'prob0_1':'2',
        'prob0_2':'1',
        'prob1_0':'4',
        'prob1_1':'95',
        'prob1_2':'1',
        'prob2_0':'5',
        'prob2_1':'0',
        'prob2_2':'95',
    }
    return render_template('index.html', data=data)