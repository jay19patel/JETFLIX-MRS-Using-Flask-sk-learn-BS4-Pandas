

from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify
# my Moduls 
from My_Moduls.log_reg import Login_Registration
from My_Moduls.ML_Model import Analysis_Movies
app = Flask(__name__)


#  DATA BASE :
from pymongo import MongoClient
database = MongoClient('localhost',27017)
myfolder = database["JetFlix"]
db = myfolder["Register_Database"]




@app.route("/" ,methods=["GET"])
def HomePage():
    return render_template('Home.html')

@app.route("/Login_Page" ,methods=["GET","POST"])
def Login_Page():
    Log_Reg = Login_Registration()
    log_data = Login_Registration.Login()
    return log_data

@app.route("/Registration_Page" ,methods=["GET","POST"])
def Registration_Page():
    Log_Reg = Login_Registration()
    reg_data = Login_Registration.Registration()
    return reg_data


@app.route("/my_dashbord" ,methods=["GET","POST"])
def Dashbord():
    import csv
    if request.method == "POST":
            Movies_Index = request.form['Movies_Index']
            Movies_Name = request.form['Movies_Name']
            Movies_Image = request.form['Movies_Image']
            Movies_Trailer = request.form['Movies_Trailer']
            Movies_Tagline = request.form['Movies_Tagline']
            Movies_Small_Description = request.form['Movies_Small_Description']
            Movies_Small_Description
            movie_data = list([Movies_Index,Movies_Name,Movies_Image,Movies_Trailer,Movies_Tagline])
            print(movie_data)
            # write the data to a CSV file
            with open("CSV_files/rowdata.csv", mode='a', newline="") as f:
                writer = csv.writer(f)
                # writer.writerow(["Movies_Index", "Movies_Name", "Movies_Image", "Movies_Trailer","Movies_Tagline"])
                writer.writerows([movie_data])
    return render_template('Dashbord.html')


def prosessiong(m_name):
    M_data = Analysis_Movies
    top_movies=[]
    my_df = M_data.convert_words_row()
    sim = M_data.my_ml_model()

    movie_index = my_df[my_df['title'] == m_name].index[0] or my_df[my_df['title'] == m_name].index[0]
    movie_name = sorted(list(enumerate(sim[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_name:
        top_movies.append(my_df.iloc[i[0]].title)
    print(top_movies)
    return top_movies



@app.route("/Search_movies" ,methods=['GET','POST'])
def Search_movies():
    if request.method == "POST":
        movie_name = request.form['M_name']
        top_movies = prosessiong(movie_name)
        print("list type  ___________:",type(top_movies))
        return render_template('Home.html',data=top_movies)
        # return render_template('Test.html',data=top_movies)
    else:
        Movies_data = "Random Names "
        return render_template('Test.html',data= Movies_data)

if __name__=='__main__':
    app.run(debug=True)

