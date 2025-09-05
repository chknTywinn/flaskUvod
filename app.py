from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/calcLove", methods = ["POST"])
def calclove():

    d = request.form
    ime1 = d.get("ime1").lower()
    ime2 = d.get("ime2").lower()
    rez = f"{ime1} + {ime2} = {random.randint(0,100)}%"
    if len(ime1)==0 or len(ime2)==0:
         rez = f"{ime1} + {ime2} = 0%"
    if ime1=="blaž" or ime2=="blaž":
         rez = f"{ime1} + {ime2} = {random.randint(0,5)}" 
    if ime1=="modest" or ime2=="modest":
         rez = f"{ime1} + {ime2} = {random.randint(90,100)}"

           
    return render_template("index.html", rez=rez)

app.run(debug=True) 