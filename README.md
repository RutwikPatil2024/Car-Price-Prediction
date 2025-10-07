# 🚗 Car Price Prediction using Machine Learning

## 📘 Overview
This project predicts the **selling price of used cars** based on multiple features such as brand, model, manufacturing year, mileage, fuel type, and transmission.

It uses **Machine Learning (Linear Regression / Random Forest)** for prediction and is integrated with a **Flask web application** for real-time user interaction.

The model was trained and tested using data collected during an internship at **IGAP Technologies**.

---

## 🧠 Project Workflow

1. **Data Collection**
   - The dataset (`Data.xlsx` / `clean_data.xlsx`) contains car features and their corresponding prices.

2. **Data Preprocessing**
   - Cleaning missing values  
   - Encoding categorical variables  
   - Scaling numerical values  

3. **Model Building**
   - Several regression algorithms were tested.  
   - The final model was saved as `MLR.pkl` (Machine Learning Regression Model).

4. **Deployment**
   - A simple **Flask-based web app (`app.py`)** allows users to enter car details and get an estimated price instantly.

---

## 📂 Folder Structure


## 📂 Folder Structure
```
CarPricePrediction/
├── app.py                  # Flask backend script
├── templates/              # HTML templates for frontend
├── static/                 # CSS, JS, and images
├── CarPricePrediction.ipynb # Model training notebook
├── ProjectWork.ipynb       # Extended project analysis
├── clean_data.xlsx         # Cleaned dataset
├── Data.xlsx               # Original dataset
├── MLR.pkl                 # Trained ML model file
├── .gitignore              # Ignored files for GitHub
└── README.md               # Project documentation
```
---

## ⚙️ Installation and Setup

### Steps 
```bash
Step 1️⃣ – Clone the Repository
git clone https://github.com/<your-username>/CarPricePrediction.git
cd CarPricePrediction

Step 2️⃣ – Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # Linux/Mac

Step 3️⃣ – Install Dependencies
pip install -r requirements.txt

Step 4️⃣ – Run the Flask App
python app.py

Now open your browser and visit 👉 http://127.0.0.1:5000/
