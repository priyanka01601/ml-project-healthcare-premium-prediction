import streamlit as st
from prediction import predict

st.title("Health Insurance Prediction App")
st.write("Fill the details below and click Predict to estimate annual premium.")

# Predefined options for each column
category_options = {
    "gender": ["Male", "Female"],
    "region": ["Northwest", "Southeast", "Northeast", "Southwest"],
    "marital_status": ["Unmarried", "Married"],
    "bmi_category": ["Normal", "Obesity", "Overweight", "Underweight"],
    "smoking_status": ["No Smoking", "Regular", "Occasional"],
    "employment_status": ["Salaried", "Self-Employed", "Freelancer"],
    "income_level": ["<10L", "10L - 25L", "25L - 40L", "> 40L"],
    "medical_history": [
        "No Disease",
        "Diabetes",
        "Thyroid",
        "Heart disease",
        "High blood pressure",
        "Diabetes & High blood pressure",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease",
    ],
    "insurance_plan": ["Bronze", "Silver", "Gold"]
}


col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, 30)

with col2:
    gender = st.selectbox("Gender", category_options["gender"])

with col3:
    region = st.selectbox("Region", category_options["region"])

# ------------------------------------------------
# ROW 2: Marital, BMI, Smoking
# ------------------------------------------------
col4, col5, col6 = st.columns(3)

with col4:
    marital_status = st.selectbox("Marital Status", category_options["marital_status"])

with col5:
    bmi_category = st.selectbox("BMI Category", category_options["bmi_category"])

with col6:
    smoking_status = st.selectbox("Smoking Status", category_options["smoking_status"])

# ------------------------------------------------
# ROW 3: Employment, Income, Insurance Plan
# ------------------------------------------------
col7, col8, col9 = st.columns(3)

with col7:

    medical_history = st.selectbox("Medical History", category_options["medical_history"])

with col8:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)

with col9:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)


col10, col11, col12 = st.columns(3)
with col10:
    employment_status = st.selectbox("Employment Status", category_options["employment_status"])
with col11:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
with col12:
    insurance_plan = st.selectbox("Insurance Plan", category_options["insurance_plan"])


input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')