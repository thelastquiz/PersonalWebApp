from flask import Flask, render_template, request

app = Flask(__name__)

#alright now lets try to download and run flask once we have a bit more of the cosmetics
#HOLY FUCK FLASK INSTALLED FIRST GO ok so now that we have it we can just copy everything over
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/pagetwo")
def pagetwo():
    return render_template('pagetwo.html')
@app.route("/myprojects")
def myprojects():
    return render_template('myprojects.html')
