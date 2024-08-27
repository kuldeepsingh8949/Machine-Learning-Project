from flask import Flask, render_template, url_for, request
import joblib 

model_file_path = r"C:\Users\kulde\OneDrive\Desktop\machine learning\Airline passenger prediction\models\logisticregre.lb"
model =  joblib.load(model_file_path)

app = Flask(__name__)

@app.route('/') #http://127.0.0.1:5000/
def home_page():
    return render_template('home_page.html')

@app.route('/userdata') #http://127.0.0.1:5000/userdata
def userdata():
    # return "Hey! this is url for project.html"
    return render_template('project.html')

@app.route('/prediction', methods=['GET','POST']) #http://127.0.0.1:5000/predict
def prediction():
    if request.method == 'POST':
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        inflight_entertainment = int(request.form['inflight_entertainment'])
        baggage_handling =int( request.form['baggage_handling'])
        cleanliness = int(request.form['cleanliness'])
        departure_delay = int(request.form['departure_delay'])
        arrival_delay = int(request.form['arrival_delay'])
        gender = int(request.form['gender'])
        customer_type = int(request.form['customer_type'])
        travel_type = int(request.form['travel_type'])
        class_type = request.form['class_type']

        economy = 0
        economy_plus = 0
        
        if class_type == "ECO":
            economy = 1
        elif class_type == "ECO_PLUS":
            economy_plus = 1

        unseen_data = [[age, flight_distance, inflight_entertainment, baggage_handling, cleanliness, departure_delay, arrival_delay, gender, customer_type, travel_type, economy, economy_plus]]
        
        PREDICTION = model.predict(unseen_data)[0]
        print(PREDICTION)
        labels = {'1':" 😎 SATISFIED",'0':" ☹️ DISATISFIED"}

        # return labels[str(prediction)]
        return render_template('output.html',output=labels[str(PREDICTION)])





if __name__ == "__main__":
    app.run(debug=True) 