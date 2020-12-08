from flask import Flask, render_template    
app = Flask(__name__)
@app.route('/play')
def level1():
    return render_template('playground.html', number=3)
@app.route('/play/<int:number>')
def level2(number):
    return render_template('playground.html', number=number)
@app.route('/play/<int:number>/<color>')
def level3(number,color):
    return render_template('playground.html', number=number, color=color)
if __name__ =="__main__":
    app.run(debug=True)