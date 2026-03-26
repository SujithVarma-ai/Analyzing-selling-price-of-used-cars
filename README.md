# Car Price Prediction System

🔗 **Live App:**
https://analyzing-selling-price-of-used-cars-ktb8wptbebpbktbedtneml.streamlit.app/

## Overview

This project predicts the **selling price of used cars** using Machine Learning.
Users can input car details and instantly get an estimated resale price.

## Features

* 📊 Real-time car price prediction
* 🧠 Machine Learning model (Linear Regression)
* 🎯 Interactive UI using Streamlit
* 💰 Price range estimation
* 📉 Depreciation calculation

---

## App Screenshot

![App Screenshot](https://github.com/SujithVarma-ai/Analyzing-selling-price-of-used-cars/blob/main/Screenshot%202026-03-26%20231235.png)

## Input Parameters

* Manufacturing Year
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission
* Number of Previous Owners

## Model Used

* Linear Regression
* Label Encoding for categorical features

## Project Structure

```
├── app.py
├── requirements.txt
├── CAR DETAILS FROM CAR DEKHO.csv
├── README.md
├── screenshot.png
```

## Installation (Run Locally)

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment

Deployed using **Streamlit Cloud**

## Future Improvements

* Use advanced ML models (Random Forest, XGBoost)
* Add more features (car brand, engine, etc.)
* Improve UI/UX
* Add model evaluation metrics

