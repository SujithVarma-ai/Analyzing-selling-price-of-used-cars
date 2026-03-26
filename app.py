import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Car Price Prediction", layout="wide")

st.title("🚗 Car Price Prediction System")
st.markdown("### Get Instant Valuation for Your Used Car")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\nraja\Downloads\archive\CAR DETAILS FROM CAR DEKHO.csv")    
    return df

df = load_data()

# -------------------------------
# DATA PREPROCESSING
# -------------------------------
df = df.dropna()

le_fuel = LabelEncoder()
le_seller = LabelEncoder()
le_trans = LabelEncoder()
le_owner = LabelEncoder()

df['fuel'] = le_fuel.fit_transform(df['fuel'])
df['seller_type'] = le_seller.fit_transform(df['seller_type'])
df['transmission'] = le_trans.fit_transform(df['transmission'])
df['owner'] = le_owner.fit_transform(df['owner'])

X = df[['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']]
y = df['selling_price']

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# SIDEBAR INPUT
# -------------------------------
st.sidebar.header("Car Details")

year = st.sidebar.slider("Manufacturing Year", 2000, 2026, 2015)
present_price = st.sidebar.number_input("Current Ex-Showroom Price (Lakhs)", 1.0, 50.0, 6.0)
kms_driven = st.sidebar.number_input("Kilometers Driven", 1000, 200000, 30000)

fuel = st.sidebar.selectbox("Fuel Type", le_fuel.classes_)
seller = st.sidebar.selectbox("Seller Type", le_seller.classes_)
transmission = st.sidebar.selectbox("Transmission", le_trans.classes_)
owner = st.sidebar.selectbox("Number of Previous Owners", le_owner.classes_)

predict_btn = st.sidebar.button("Get Price Estimate")

# -------------------------------
# PREDICTION
# -------------------------------
if predict_btn:

    fuel_val = le_fuel.transform([fuel])[0]
    seller_val = le_seller.transform([seller])[0]
    trans_val = le_trans.transform([transmission])[0]
    owner_val = le_owner.transform([owner])[0]

    input_data = np.array([[year, kms_driven, fuel_val, seller_val, trans_val, owner_val]])

    prediction = model.predict(input_data)[0]
    prediction_lakh = prediction / 100000

    depreciation = present_price - prediction_lakh

    # -------------------------------
    # RESULTS SECTION
    # -------------------------------
    st.markdown("## 💰 Price Estimation Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Estimated Selling Price", f"₹{prediction_lakh:.2f} Lakhs")
    col2.metric("Current Showroom Price", f"₹{present_price:.2f} Lakhs")
    col3.metric("Total Depreciation", f"₹{depreciation:.2f} Lakhs")

    # -------------------------------
    # PRICE ANALYSIS
    # -------------------------------
    st.markdown("## 📊 Price Analysis")

    lower = prediction_lakh * 0.9
    upper = prediction_lakh * 1.1

    st.success(f"Expected Price Range: ₹{lower:.2f}L - ₹{upper:.2f}L")

    st.markdown("### Price Factors:")
    st.write("- Moderate age impacts value")
    st.write("- Mileage affects resale price")
    st.write("- Transmission influences pricing")
    st.write("- Fuel type impacts demand")
    st.write("- Seller type affects trust")

    # -------------------------------
    # CAR DETAILS DISPLAY
    # -------------------------------
    st.markdown("## 🚘 Your Car Details")

    col1, col2 = st.columns(2)

    col1.write(f"**Manufacturing Year:** {year}")
    col1.write(f"**Kilometers Driven:** {kms_driven}")

    col2.write(f"**Fuel Type:** {fuel}")
    col2.write(f"**Transmission:** {transmission}")
    col2.write(f"**Seller Type:** {seller}")
    col2.write(f"**Previous Owners:** {owner}")