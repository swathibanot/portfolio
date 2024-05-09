from flask import Flask,render_template
app =Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return render_template('index.html',response='john')

@app.route("/contact",methods=['GET'])
def contact():
    return "<p>contact</p>"


if __name__ =='__main__':
     app.run(debug=True)    