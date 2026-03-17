from flask import Flask,render_template
import os
app=Flask(__name__)
picfolder=os.path.join("static")
app.config['UPLOAD_FOLDER']=picfolder

@app.route("/")
def first():
    pic=os.path.join(app.config['UPLOAD_FOLDER'],"waterfall.png")
    return render_template("home.html",user_image=pic)
@app.route('/second')
def second():
    return render_template("second.html")
if __name__=="__main__":
    app.run(debug=True)