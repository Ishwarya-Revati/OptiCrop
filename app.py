from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# ==========================
# Load Model
# ==========================

model = joblib.load("model/crop_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Prediction Route
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Read Input Values

        N = float(request.form.get("N"))
        P = float(request.form.get("P"))
        K = float(request.form.get("K"))

        temperature = float(request.form.get("temperature"))
        humidity = float(request.form.get("humidity"))
        ph = float(request.form.get("ph"))
        rainfall = float(request.form.get("rainfall"))

        # Create DataFrame

        input_data = pd.DataFrame([{
            "N": N,
            "P": P,
            "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }])

        # Prediction

        prediction = model.predict(input_data)

        crop = encoder.inverse_transform(prediction)[0]

        # Return JSON

        return jsonify({

            "success": True,

            "crop": crop,

            "summary": {

                "Nitrogen": N,

                "Phosphorus": P,

                "Potassium": K,

                "Temperature": temperature,

                "Humidity": humidity,

                "Soil pH": ph,

                "Rainfall": rainfall

            }

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        })


# ==========================
# Run Flask
# ==========================

if __name__ == "__main__":
    app.run(debug=True)