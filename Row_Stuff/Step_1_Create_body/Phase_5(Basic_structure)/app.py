
from my_moduls.app import Data_analysis
from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify
# my Moduls 
app = Flask(__name__)


#  DATA BASE :
# from pymongo import MongoClient
# database = MongoClient('localhost',27017)
# myfolder = database["JetFlix"]
# db = myfolder["Register_Database"]



# ----------------------Home Page  ----------------

@app.route("/" ,methods=["GET","POST"])
def HomePage():
    return render_template('Home.html')

# ----------------------Search Movies ----------------

@app.route("/search_me" ,methods=["GET","POST"])
def Seach_me():
    if request.method == "POST":
        search_text = request.form["search_text"]
        top5_datas = Data_analysis.find_by_name(search_text)
        print(f"finding..{search_text}")
        print(top5_datas)
    return render_template('Home.html',data=top5_datas)


# ----------------------Movies details  ----------------

@app.route("/my_movie" ,methods=["GET","POST"])
def My_movie():
    data = "jay"
    return render_template('movie_details.html',data=data)


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


if __name__=='__main__':
    app.run(debug=True)

