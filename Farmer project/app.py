from flask import Flask, render_template, request
import pandas as pd
import joblib
import certifi
from pymongo import MongoClient

# Load pre-trained models and data
std_scaler = joblib.load('./models/std_scaler.lb')
kmeans_model = joblib.load('./models/kmeans_model.lb')
df = pd.read_csv("./models/filter_crops.csv")

app = Flask(__name__)

# MongoDB connection setup
connection_string = "mongodb+srv://kuldeepraika64:WytraroLR6dtkhmL@farmer.pqlvj.mongodb.net/?retryWrites=true&w=majority&appName=farmer"
client = MongoClient(connection_string, tlsCAFile=certifi.where())  
database = client["Farmer2"]
collection = database['FarmerData1']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    suggestion_crops = []
    crop_images = {}
    
    if request.method == 'POST':
        try:
            N = int(request.form['N'])
            PH = float(request.form['PH'])
            P = int(request.form['P'])
            K = int(request.form['K'])
            humidity = float(request.form['humidity'])
            rainfall = float(request.form['rainfall'])
            temperature = float(request.form['temperature'])

            UNSEEN_DATA = [[N, P, K, temperature, humidity, PH, rainfall]]

            # Transform the data
            transformed_data = std_scaler.transform(UNSEEN_DATA)
            # Predict using KMeans model
            cluster = kmeans_model.predict(transformed_data)[0]

            # Get suggested crops and their images
            suggestion_crops = list(df[df['cluster_no'] == cluster]['label'].unique())
            crop_images = {crop: f"/static/images/{crop.lower()}.jpg" for crop in suggestion_crops}

            # Insert data into MongoDB
            data = {
                "N": N, "P": P, "K": K, "temperature": temperature,
                "humidity": humidity, "PH": PH, "rainfall": rainfall
            }
            data_id = collection.insert_one(data).inserted_id
            print(f"Your data is inserted into MongoDB. Your record ID is: {data_id}")

        except Exception as e:
            print(f"An error occurred: {e}")
            suggestion_crops = ["Error processing your request."]
            crop_images = {}

    return render_template('output.html', suggestion_crops=suggestion_crops, crop_images=crop_images)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            feedback_message = f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n"
            
            with open('feedback.txt', 'a') as file:
                file.write(feedback_message)
            
            print("Feedback received and saved.")
            return render_template('feedback.html', success="Your feedback has been submitted successfully.")

        except Exception as e:
            print(f"An error occurred while saving feedback: {e}")
            return render_template('feedback.html', error="There was an error saving your feedback. Please try again.")

    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True)
