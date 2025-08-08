from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('youtube_revenue_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    views = float(request.form['views'])
    subscribers = float(request.form['subscribers'])
    likes = float(request.form['likes'])
    shares = float(request.form['shares'])
    comments = float(request.form['comments'])
    
    # Engagement Rate formula
    engagement_rate = (likes + shares + comments) / views * 100

    # Format input for model
    input_data = np.array([[views, subscribers, likes, shares, comments, engagement_rate]])
    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', result=f"Predicted Revenue: ${prediction}")

if __name__ == '__main__':
    app.run(debug=True)
