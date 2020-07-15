from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from .forms import InputForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "b'*3x0f0xf42x924ow5xdayxc8txacHfxc6qxb16x9efxe9h4xcb4wjxa0Xidxb0ix1dzox8ffdx03hxc98x90yxd2@qxfcgx14"

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def input():
    #form = InputForm(request.form)
    input_li = []
    if request.method == "POST":
        req = request.form
        input_li=list(req.values())
        print(input_li)
        return redirect('results')
    return render_template('home.html')

@app.route('/results', methods=['GET'])
def results():

    return render_template('results.html')
