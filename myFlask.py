from flask import Flask,render_template,request
from mySql import select_admin

app = Flask(__name__)

@app.route('/index')
def index():
    return 'hello word'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        response = request.form
        username = response.get('username')
        password = response.get('password')

        bool = select_admin(username,password)

        if bool == 1:
            return render_template('ret.html',username=username,bool=bool)
        else:
            return '账号或密码不正确'

    if request.method == 'GET':
        return 'GET'


if __name__ == '__main__':
    app.run(debug=True)