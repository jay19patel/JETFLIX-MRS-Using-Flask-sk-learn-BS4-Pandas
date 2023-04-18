from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify
app = Flask(__name__)
#  DATA BASE :
from pymongo import MongoClient
database = MongoClient('localhost',27017)
myfolder = database["JetFlix"]
db = myfolder["Register_Database"]

class Login_Registration():
    @app.route("/Login_Page" ,methods=["GET","POST"])
    def Login():
        if request.method == "POST":
            username = request.form['username']
            user_password = request.form['password123']
            print(username)
            print(user_password)

            data =db.find_one({"Username":username})
            if data:
                if user_password ==data["Password1"]:
                    print(data)

                    session['user_name'] = data['Username']
                    session['log'] = "Login"
                    # return render_template('test.html',data=data)
                    return redirect(url_for('HomePage'))
                else:
                    print("password Not Match ")
            else:
                print(" User Not Found")
        return render_template('login.html')
    
    def Registration():
        if request.method == "POST":
            Name = request.form['my_name']
            Username = request.form['my_username']
            Email = request.form['my_email']
            Phone = request.form['my_phone']
            Password1 = request.form['my_psw1']
            Password2 = request.form['my_psw2']
            print(Name,Username,Email,Phone,Password1,Password2)
            if Password1==Password2:
                db.insert_one({"Name":Name,"Username":Username,"Email":Email,"Phone":Phone,"Password1":Password1})
                print("Save succesfuly")
                return redirect(url_for('Login_Page'))
            else:
                print(" Password Not Match   ")

        return render_template('Registration.html')
    

class Dashbord():
    pass