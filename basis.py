from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/hi', methods=['GET', 'POST'])
# def hi():
#     return 'hi'
#
# @app.route('/index', methods=['GET', 'POST'])
# def index01():
#     return render_template('./templates/index.html')

@app.route('/nihao/<int:num>', methods=['POST', 'GET'])
def nihao(num):
    if num == 1:
        return 'this is 1'
    if num == 2:
        return 'this is 2'
    return 'nihao'


app.run()
