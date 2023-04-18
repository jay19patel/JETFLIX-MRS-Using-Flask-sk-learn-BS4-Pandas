
from my_moduls.app import Data_analysis
from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify

from my_moduls.log_reg import Login_Registration

# my Moduls 
app = Flask(__name__)
app.secret_key = 'jaypatel1234'

#  DATA BASE :
# from pymongo import MongoClient
# database = MongoClient('localhost',27017)
# myfolder = database["JetFlix"]
# db = myfolder["Register_Database"]



# ----------------------Home Page  ----------------

@app.route("/" ,methods=["GET","POST"])
def HomePage():
    if session.get('log'):
        if session['log'] == "LogOut":
            user =  " You are log outed resent "
        else:
            user = session['user_name']
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
    return render_template('Home.html',data=top5_datas)

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

@app.route("/my_movie" ,methods=["GET","POST"])
def My_movie():
    return render_template('movie_details.html')

# ---------------------- My Profile  ----------------

@app.route("/my_profile" ,methods=["GET","POST"])
def My_Profile():
    user_data = session['user_name']
    list_of_movies = ["avtar", "avangers"]
    return render_template('My_profile.html',data=user_data,m_list=list_of_movies)


# ----------------------find by Genraas ----------------

@app.route("/action" ,methods=["GET","POST"])
def genres_action ():
    movies = Data_analysis.find_by_genre("Action",'CSV/action.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Action")


@app.route("/adventure" ,methods=["GET","POST"])
def genres_adventure ():
    movies = Data_analysis.find_by_genre("Adventure",'CSV/adventure.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Adventure")


@app.route("/animation" ,methods=["GET","POST"])
def genres_animation ():
    movies = Data_analysis.find_by_genre("Animation",'CSV/animation.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Animation")


@app.route("/crime" ,methods=["GET","POST"])
def genres_crime ():
    movies = Data_analysis.find_by_genre("Crime",'CSV/crime.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Crime")


@app.route("/horror" ,methods=["GET","POST"])
def genres_horror ():
    movies = Data_analysis.find_by_genre("Horror",'CSV/horror.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Horror")


@app.route("/sci_fi" ,methods=["GET","POST"])
def genres_sci_fi ():
    movies = Data_analysis.find_by_genre("Sci-Fi",'CSV/scifi.csv')
    print("Fetchin Data ....")
    return render_template('Home.html',movies=movies,title="Sci")


if __name__=='__main__':
    app.run(debug=True)

