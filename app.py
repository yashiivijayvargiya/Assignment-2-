from flask import Flask, render_template, request
from model import preprocess_and_predict  # Import the model's function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect input data from form
        input_data = {
            'Pregnancies': request.form['Pregnancies'],
            'Glucose': request.form['Glucose'],
            'BloodPressure': request.form['BloodPressure'],
            'SkinThickness': request.form['SkinThickness'],
            'Insulin': request.form['Insulin'],
            'BMI': request.form['BMI'],
            'DiabetesPedigreeFunction': request.form['DiabetesPedigreeFunction'],
            'Age': request.form['Age']
        }
        
        # Convert data to appropriate types
        input_data = {k: float(v) for k, v in input_data.items()}

        # Predict using the pre-trained model
        prediction = preprocess_and_predict(input_data)
        result = 'Diabetic' if prediction == 1 else 'Non-Diabetic'

        return render_template('index.html', prediction_text=f'Result: {result}')

if __name__ == '__main__':
    app.run(debug=True)
