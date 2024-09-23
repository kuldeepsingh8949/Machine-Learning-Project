from flask import Flask ,render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')
    # return "hey kese ho"

@app.route('/courses')
def courses():
    return render_template('courses.html')
    # return "hey kese ho"

@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')
    # return "hey kese ho"

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')
    # return "hey kese ho"

@app.route('/userdata',methods=['GET','POST'])
def userdata():
    if request.method == 'POST':
        username = request.form['username']
        useremail = request.form['useremail']
        usersubject = request.form['usersubject']
        usermessage = request.form['usermessage']
        user_recieved_data = [username,useremail,usersubject,usermessage]
        
        return user_recieved_data




if __name__ =="__main__":
    app.run(debug=True)
