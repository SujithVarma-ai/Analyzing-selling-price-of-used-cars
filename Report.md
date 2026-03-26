# 🚗 Car Price Prediction System – Project Report

## 1. Introduction

The automobile market has seen rapid growth, especially in the used car segment. Determining the correct selling price of a used car is a complex task influenced by multiple factors such as age, mileage, fuel type, and ownership history.

This project aims to develop a **machine learning-based system** that predicts the selling price of used cars using historical data. Additionally, a **Streamlit web application** is built to provide an interactive interface for users.

---

## 2. Objectives

* To analyze factors affecting used car prices
* To build a machine learning model for price prediction
* To create an interactive web application using Streamlit
* To provide real-time price estimation

---

## 3. Dataset Description

The dataset used is **CarDekho Used Car Dataset**, which contains details of various used cars.

### Key Features:

* Year of manufacture
* Selling price
* Kilometers driven
* Fuel type
* Seller type
* Transmission
* Owner type

---

## 4. System Architecture

### Workflow:

```
Data Collection → Data Preprocessing → Model Training → Prediction → Web App Interface
```

### Components:

* **Frontend:** Streamlit
* **Backend:** Python
* **Model:** Linear Regression

---

## 5. Data Preprocessing

The dataset undergoes the following preprocessing steps:

* Removal of missing values
* Encoding categorical variables using LabelEncoder
* Selection of relevant features
* Splitting input (X) and output (y)

---

## 6. Model Development

### Algorithm Used:

* Linear Regression

### Reason:

* Simple and efficient for numerical prediction
* Works well with linear relationships

### Features Used:

* Year
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission
* Owner

---

## 7. Implementation

### Tools & Libraries:

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

### Application Features:

* User inputs car details
* Model predicts selling price
* Displays:

  * Estimated price
  * Price range
  * Depreciation

---

## 8. Results

The system successfully predicts the approximate selling price of used cars based on user inputs. The Streamlit interface allows real-time interaction and improves usability.

---

## 9. Advantages

* Easy to use interface
* Fast prediction
* Helps in decision-making
* Real-world application

---

## 10. Limitations

* Uses basic Linear Regression
* Accuracy depends on dataset quality
* Limited features considered

---

## 11. Future Enhancements

* Use advanced models (Random Forest, XGBoost)
* Add graphical analysis
* Improve UI/UX design
* Deploy with scalable backend
* Integrate real-time car market data

---

## 12. Conclusion

This project demonstrates how machine learning can be effectively applied to predict used car prices. By combining data analysis with a web interface, the system provides a practical and user-friendly solution for price estimation.

---

## 13. References

* Scikit-learn Documentation
* Streamlit Documentation
* CarDekho Dataset

---
