#IMPROTING
from flask import Flask,render_template,request
#INTERACTION
web=Flask(__name__)
#MAPPING
#INPUTS
@web.route('/')
@web.route('/register')
def homepage():
    return render_template("register.html")
@web.route("/confirmation",methods=['GET','POST'])
def register():
    if request.method =="POST":
        n=request.form.get("name")
        c=request.form.get("city")
        p=request.form.get("phone number")
        return render_template("confirm.html",name=n,city=c,phonenumber=p)

app = Flask(__name__)

@app.route("/")
def first():
        return render_template("home.html")

@app.route('/second')
def second():
        return 'welcome to second page'
from flask import Flask,render_template

if __name__== "__main__":
    web.run(debug=True)