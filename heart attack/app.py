from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model_file_path = r"C:\Users\kulde\OneDrive\Desktop\machine learning\heart attack\models\logisticregre.lb"
model = joblib.load(model_file_path)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract form data from the HTML form
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            cp = int(request.form['cp'])
            trestbps = int(request.form['trestbps'])
            chol = int(request.form['chol'])
            fbs = int(request.form['fbs'])
            restecg = int(request.form['restecg'])
            thalach = int(request.form['thalach'])
            exang = int(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = int(request.form['slope'])
            ca = int(request.form['ca'])
            thal = int(request.form['thal'])

            # Prepare the input data as a NumPy array
            input_data = np.array([[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            # Predict using the trained model
            prediction = model.predict(input_data)[0]

            # Interpret the result
            if prediction == 0:
                result = "No heart disease detected."
            else:
                result = "Heart disease detected. Please consult a doctor."

            # Render the result page with the prediction result
            return render_template('result.html', prediction=result)

        except Exception as e:
            return f"An error occurred: {e}", 400

    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)
