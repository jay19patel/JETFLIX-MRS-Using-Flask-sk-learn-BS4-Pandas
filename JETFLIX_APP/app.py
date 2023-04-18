
from My_Moduls.app import Data_analysis
from My_Moduls.csv_manupilation import CSV_Manupilation
from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify,Blueprint
from pymongo import MongoClient # mongodb 
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required,JWTManager,set_access_cookies,unset_jwt_cookies
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'jaypateltopsecret789654123'
app.config["JWT_SECRET_KEY"] = "jaypateltopsecret789654123" 
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=60) 
jwt = JWTManager(app)

# ---------------------- Database Connection   ----------------

database = MongoClient('localhost',27017)
myfolder = database["JetFlix"]
db = myfolder["Users_Database"]




# ---------------------- JWT   ----------------
# expire token 
@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return redirect(url_for('LoginPage'))  


@jwt.unauthorized_loader
def custom_unauthorized_response(_err):
    return redirect(url_for('LoginPage'))


# ---------------------- Login Registration  ----------------


@app.route('/Login_Page',methods=['GET','POST'])
def LoginPage():
    error =None
    if request.method == "POST":
        email=request.form['loginemail']
        pwd=request.form['loginpss']
        userdata=db.find_one({'email':email})
        if not userdata:
            flash("Email id not Founed Please Check Email id ")
            return redirect(url_for('LoginPage'))
        else:
            newpwd = pwd[::-1]+pwd[::-1]+pwd
            if userdata['password'] == newpwd:
                print("login done ....")
                access_token = create_access_token(identity=(
                    {'name':userdata['name'],
                     'email':userdata['email'],
                     'phone':userdata['phone'],
                     'password':userdata['password'],
                     'checkbox':userdata['checkbox']}
                     )
                    )
                res = redirect(url_for('HomePage'))
                set_access_cookies(res, access_token) 
                session['log'] = "login"
                session['in_auther'] = userdata['name']
                print("login sucsessfull ......")     
                return res
               

            else:
                flash('Email & Password not match')
                return redirect(url_for('LoginPage'))

    
    return render_template('LoginPage.html')


@app.route('/Log_out',methods=['GET','POST'])
@jwt_required()
def Logout():
    res = jsonify({"message":"logout"})
    unset_jwt_cookies(res)
    session.clear()
    session['log']='logout'
    print("loged out...")
    flash("You are logout Login New ID ")
    return redirect(url_for('HomePage'))


@app.route('/Registration_Page',methods=['GET','POST'])
def RegistrationPage():
    if request.method == "POST":
        name=request.form['my_name']
        email=request.form['my_email']
        phone=request.form['my_phone']
        pwd1=request.form['my_psw1']
        pwd2=request.form['my_psw2']
        checkbox = request.form.getlist('my-checkbox')
        if pwd1==pwd2:
            newpwd = pwd1[::-1]+pwd1[::-1]+pwd1
            senddata = db.insert_one({
                "name":name,
                "email":email,
                "phone":phone,
                "password":newpwd,
                'checkbox':checkbox
            })
            flash('You were successfully Register Your Data')
            print("Registration Successhull......")  
            return redirect(url_for('LoginPage'))


        else:
            flash('Some kind of MisMatch Please Check Data')
            return redirect(url_for('RegistrationPage'))

    return render_template('RegistrPage.html')


# ----------------------Home Page  ----------------

@app.route("/" ,methods=["GET","POST"])
@jwt_required()
def HomePage():
    data = get_jwt_identity()
    filter_criteria = {"email": data['email'],"password": data['password']}
    user_data = db.find_one(filter_criteria)
    if session.get('log'):
        if session['log'] == 'login':
            name = session['in_auther']
            email = data['email']
            checkbox = user_data['checkbox']
            Gen_data = []
            for gen in checkbox:
                Gen_data_row = CSV_Manupilation.get_gen_data(gen)
                for i in Gen_data_row:
                    Gen_data.append(i)
            if request.method == "POST":
                search_text = request.form["M_name"]
                this_movie = Data_analysis.this_movie(search_text)
                try:
                    top5_datas = Data_analysis.find_by_name(search_text)
                    print(f"finding..{search_text}")
                    return render_template('Home.html',user=name,subs=checkbox,data=top5_datas,Gen_data=Gen_data,this_movie = this_movie)
                except:
                        flash(" Movie Not Found ")
            return render_template('Home.html',user=name,subs=checkbox,Gen_data=Gen_data)
    return render_template('Home.html')

# ----------------------Profile Page  ----------------

@app.route("/Profile_Page" ,methods=["GET","POST"])
@jwt_required()
def Profile_Page():
    user_data_jwt = get_jwt_identity()
    filter_criteria = {"email": user_data_jwt['email'],"password": user_data_jwt['password']}
    user_data = db.find_one(filter_criteria)
    if request.method == "POST":
        name1=request.form['my_name']
        email1=request.form['my_email']
        phone=request.form['my_phone']
        pwd1=request.form['my_psw2']
        checkbox = request.form.getlist('my-checkbox')
        print("data update")
        result = db.update_many(filter_criteria, {"$set": {'name': name1, 'email': email1,'phone':phone,'password':pwd1,'checkbox':checkbox}},upsert=True)
        return redirect(url_for('HomePage'))
    name = session['in_auther']
    
    return render_template('My_Profile.html',user_data=user_data,user = name)


# ---------------------- Subscribe Movies  ----------------

@app.route("/Movie_Details_Page" ,methods=["GET","POST"])
@jwt_required()
def Movie_Details_Page():
    if request.method == "POST":
        user_data = get_jwt_identity()
        username = user_data['name']
        search_text = request.form['find_movie_details']
        this_movie = Data_analysis.this_movie(search_text)
        top5_datas = Data_analysis.find_by_name(search_text)
        print(f"finding..{search_text}")
        return render_template('Movie-Details.html',user=username,data=top5_datas,this_movie = this_movie)
    return render_template('Movie-Details.html')


# ---------------------- Subscribe Movies  ----------------

@app.route("/save_movie" ,methods=["GET","POST"])
@jwt_required()
def Save_movie():
    from collections import Counter
    user_data = get_jwt_identity()
    email = user_data['email']
    password12 = user_data['password']
    if request.method == "POST":
        print("Savd Movies data ")
        filter_criteria = {"email": email,"password": password12}
        
        save_title = request.form['save_title']
        save_genres = request.form['save_genres']
        result = db.update_many(filter_criteria, {"$set": {'save_title': save_title, 'save_genres': save_genres}})

    return redirect(url_for('HomePage'))

# ---------------------- Movies Recomandation ----------------




if __name__=='__main__':
    app.run(debug=True)

