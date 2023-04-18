
from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify
from My_Moduls.app import Data_analysis
from My_Moduls.log_reg import Login_Registration

# my Moduls 
app = Flask(__name__)
app.secret_key = 'jaypatel1234'




# ----------------------Home Page  ----------------

@app.route("/" ,methods=["GET","POST"])
def HomePage():
    if session.get('log'):
        if session['log'] == "LogOut":
            user =  " You are log outed resent "
        else:
            user = session['user_name']
            subs = session['Subs']
            return render_template('Home.html',user = user,subs = subs)
    else:
        user = " unkonwn"
    return render_template('Home.html',user = user)

# ----------------------Search Movies ----------------

@app.route("/search_me" ,methods=["GET","POST"])
def Seach_me():
    if request.method == "POST":
        search_text = request.form["search_text"]
        top5_datas = Data_analysis.find_by_name(search_text)
        print(f"finding..{search_text}")
    return render_template('Home.html',data = top5_datas)

# ----------------------Login & Registration  ----------------
@app.route("/Login_Page" ,methods=["GET","POST"])
def Login_Page():
    log_data = Login_Registration.Login()
    return log_data

@app.route("/Registration_Page" ,methods=["GET","POST"])
def Registration_Page():
    reg_data = Login_Registration.Registration()
    return reg_data

@app.route("/Logout" ,methods=["GET","POST"])
def Logout():
    session.clear()
    session['log'] = "LogOut"
    return redirect('Login_Page')
# ----------------------Movies details  ----------------







if __name__=='__main__':
    app.run(debug=True)

