from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("model/crop_model.pkl", mmap_mode=None)
encoder = joblib.load("model/label_encoder.pkl", mmap_mode=None)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Make prediction
        prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

        # Convert prediction back to crop name
        crop = encoder.inverse_transform(prediction)[0]

        return render_template(
            "index.html",
            prediction_text=f"🌱 Recommended Crop: {crop}",
            N=N,
            P=P,
            K=K,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)