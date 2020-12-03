from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def sayname(name):
    print(name)
    return 'Hi,' + name + '!'

@app.route('/repeat/<int:num>/<word>')
def repeat(word, num):
    # for __ in range(0,num,1):
    #     print(word)  
    return word * num


if __name__ =="__main__":
    app.run(debug=True)