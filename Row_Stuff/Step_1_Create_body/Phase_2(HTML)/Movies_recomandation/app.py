

from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify,Blueprint
from Data_analysis.main import Analysis_Movies
app = Flask(__name__)

M_data = Analysis_Movies



def prosessiong(m_name):
    top_movies=[]
    my_df = M_data.convert_words_row()
    sim = M_data.my_ml_model()

    movie_index = my_df[my_df['title'] == m_name].index[0]
    movie_name = sorted(list(enumerate(sim[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_name:
        top_movies.append(my_df.iloc[i[0]].title)
    print(top_movies)
    return top_movies


@app.route("/" ,methods=['GET','POST'])
def HomePage():
    if request.method == "POST":
        movie_name = request.form['M_name']
        top_movies = prosessiong(movie_name)
        print("list type  ___________:",type(top_movies))
        return render_template('Home.html',data=top_movies)

    else:
        Movies_data = "Random Names "
        return render_template('Home.html',data= Movies_data)

 
# _______run_________________
if __name__=='__main__':
    app.run(debug=True)