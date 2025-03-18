import streamlit as st

# Styling
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e3f;
        color: #f0f4f8;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .stButton>button {
        background: linear-gradient(45deg, #e41de4, #0b5394);
        color: black;
        font-size: 18px;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.6);
        cursor: pointer;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #0bf522, #e100ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        padding: 15px;
        border-radius: 10px;
        background-color: rgba(0, 255, 255, 0.1);
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
        opacity: 0.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1>⚓ Universal Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select the conversion type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])

# Input field
value = st.number_input("Enter Value", value=0.0 if conversion_type != "Temperature" else None, step=0.1)

# Columns for input fields
col1, col2 = st.columns(2)

# Conversion Logic
if conversion_type == "📏 Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches", "Millimeters", "Centimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches", "Millimeters", "Centimeters"])
elif conversion_type == "⚖️ Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "🌡️ Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Inches": 39.3701,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5 / 9) if to_unit == "Celsius" else ((value - 32) * 5 / 9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9 / 5 + 32) if to_unit == "Fahrenheit" else value

# Button for Conversion
if st.button("⏳ Convert"):
    if from_unit == to_unit:
        result = f"{value} {from_unit} = {value:.4f} {to_unit}"
    else:
        if conversion_type == "📏 Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "⚖️ Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "🌡️ Temperature":
            result = temperature_converter(value, from_unit, to_unit)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by <a href='https://github.com/mujahidshaikh18'>@mujahidshaikh18</a></div>", unsafe_allow_html=True)
