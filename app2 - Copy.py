import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Late Delivery Risk Prediction", layout="wide")

st.title("🚚 Late Delivery Risk Prediction")
st.write("Machine Learning Based Late Delivery Risk Prediction")

# Load model
model = joblib.load("late_delivery_risk_model.pkl")

st.sidebar.header("Enter Order Details")

shipping_mode = st.sidebar.selectbox(
    "Shipping Mode",
    ["Standard Class", "Second Class", "First Class", "Same Day"]
)

scheduled_days = st.sidebar.number_input(
    "Days for Shipment (Scheduled)",
    min_value=1,
    value=4
)

benefit = st.sidebar.number_input(
    "Benefit per Order",
    value=20.0
)

sales_customer = st.sidebar.number_input(
    "Sales per Customer",
    value=300.0
)

quantity = st.sidebar.number_input(
    "Order Quantity",
    min_value=1,
    value=2
)

discount = st.sidebar.number_input(
    "Discount",
    value=10.0
)

discount_rate = st.sidebar.number_input(
    "Discount Rate",
    value=0.10
)

product_price = st.sidebar.number_input(
    "Product Price",
    value=150.0
)

sales = st.sidebar.number_input(
    "Sales",
    value=300.0
)

profit = st.sidebar.number_input(
    "Order Profit",
    value=40.0
)

profit_ratio = st.sidebar.number_input(
    "Profit Ratio",
    value=0.20
)

shipping_pressure = quantity / (scheduled_days + 1)
profit_margin = profit / (sales + 1)
average_item_value = sales / (quantity + 1)
discount_percentage = discount_rate * 100

# Input dataframe
input_data = pd.DataFrame({

    "Type":["DEBIT"],

    "Days for shipment (scheduled)":[scheduled_days],

    "Benefit per order":[benefit],

    "Sales per customer":[sales_customer],

    "Category Id":[1],

    "Category Name":["Sporting Goods"],

    "Customer City":["New York"],

    "Customer Country":["USA"],

    "Customer Id":[1001],

    "Customer Segment":["Consumer"],

    "Customer State":["NY"],

    "Customer Zipcode":[10001],

    "Department Id":[1],

    "Department Name":["Fitness"],

    "Latitude":[40.7],

    "Longitude":[-74.0],

    "Market":["USCA"],

    "Order City":["New York"],

    "Order Country":["USA"],

    "Order Customer Id":[1001],

    "Order Item Discount":[discount],

    "Order Item Discount Rate":[discount_rate],

    "Order Item Product Price":[product_price],

    "Order Item Profit Ratio":[profit_ratio],

    "Order Item Quantity":[quantity],

    "Sales":[sales],

    "Order Item Total":[sales],

    "Order Profit Per Order":[profit],

    "Order Region":["West"],

    "Order State":["NY"],

    "Product Name":["Sample Product"],

    "Product Price":[product_price],

    "Shipping Mode":[shipping_mode],

    "Profit_Margin":[profit_margin],

    "Discount_Percentage":[discount_percentage],

    "Average_Item_Value":[average_item_value],

    "Shipping_Pressure":[shipping_pressure]

})

if st.button("Predict"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction")

    st.metric(
        "Late Delivery Probability",
        f"{probability*100:.2f}%"
    )

    if prediction == 1:
        st.error("⚠️ High Risk of Late Delivery")
    else:
        st.success("✅ Low Risk of Late Delivery")