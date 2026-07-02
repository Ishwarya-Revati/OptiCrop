# 🌱 OptiCrop AI

### Smart Agricultural Production Optimization Engine

OptiCrop AI is a Machine Learning-based crop recommendation system that
helps identify the most suitable crop based on soil nutrients and
environmental conditions. The application combines a trained Random
Forest model with a user-friendly Flask web interface to deliver quick
and accurate crop recommendations.

> **Status:** ✅ Live & Deployed\
> **Model:** Random Forest Classifier\
> **Deployment:** Vercel

------------------------------------------------------------------------

## 📌 Project Overview

Selecting the right crop is one of the most important decisions in
agriculture. OptiCrop AI analyzes key soil and weather parameters and
recommends the most appropriate crop using a trained Machine Learning
model.

The goal of this project is to demonstrate how Artificial Intelligence
can support data-driven agricultural decisions through an easy-to-use
web application.

------------------------------------------------------------------------

## ✨ Features

-   Intelligent crop recommendation
-   Machine Learning prediction using Random Forest
-   Simple and responsive web interface
-   Real-time prediction
-   Displays the entered input values with the recommendation
-   Clean dashboard-style user interface
-   Mobile-friendly design

------------------------------------------------------------------------

## 🛠️ Tech Stack

**Frontend** - HTML5 - CSS3 - Bootstrap Icons

**Backend** - Python - Flask

**Machine Learning** - Scikit-learn - Pandas - NumPy - Joblib

------------------------------------------------------------------------

## 📊 Input Parameters

The model uses the following parameters:

-   Nitrogen (N)
-   Phosphorus (P)
-   Potassium (K)
-   Temperature
-   Humidity
-   Soil pH
-   Rainfall

------------------------------------------------------------------------

## 🌾 Output

The application predicts the most suitable crop based on the provided
values.

Example:

    Recommended Crop:
    Rice

------------------------------------------------------------------------

## 📂 Project Structure

``` text
OptiCrop/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── vercel.json
│
├── model/
│   ├── crop_model.pkl
│   └── label_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── images/
│
└── dataset/
```

------------------------------------------------------------------------

## 🚀 Running the Project Locally

1.  Clone the repository

``` bash
git clone https://github.com/Ishwarya-Revati/OptiCrop.git
```

2.  Install dependencies

``` bash
pip install -r requirements.txt
```

3.  Run the application

``` bash
python app.py
```

4.  Open your browser

```{=html}
<!-- -->
```
    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📈 Machine Learning Workflow

1.  Load the dataset
2.  Preprocess the data
3.  Train the Random Forest model
4.  Save the trained model using Joblib
5.  Load the model in Flask
6.  Predict the crop based on user inputs

------------------------------------------------------------------------

## 🎯 Future Enhancements

-   Fertilizer recommendation
-   Weather API integration
-   Crop yield prediction
-   Crop disease detection
-   User authentication
-   Multi-language support

------------------------------------------------------------------------

## 👩‍💻 Developer

**Pranati Sai Lakshmi Iswarya Revati**

B.Tech -- Artificial Intelligence & Machine Learning

Aditya College of Engineering and Technology

------------------------------------------------------------------------

## 📜 License

This project was developed for educational and learning purposes as part
of an AI/ML academic project.

------------------------------------------------------------------------

⭐ If you found this project useful, consider giving the repository a
star.
