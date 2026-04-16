import streamlit as st
import pandas as pd

df = pd.read_csv("feature_selection.csv", sep = ';')

st.title("Data Preparation for Modeling")
# ===================== 1. Split Data =====================
st.markdown("### Data Split")

st.markdown("""
- Used 20% of the whole dataset (2.3 million records) for acceptable training time
- 80% training data, 20% test data  
""")
st.divider()

# ===================== 2. Encoding =====================
st.markdown("### Encoding")
# st.write("Encoded categorical features into numerical values for modeling")

st.markdown("#### One-Hot Encoding")
st.markdown("""
- Features with 10-15 categories
- IncidentGroup_D (23 categories) and IncGeo_BoroughCode (33 categories). Better model performance than Target and Binary Encoding
- Cyclical features derived from Mobilised timestamp. Better model performance than Repeating Basis Function
""")

st.markdown("#### Target/Binary Encoding")
st.markdown("""
- Used for the rest of the categorical features (more than 100 categories)
- Decision between the two based on model performance
""")
st.divider()

# ===================== 3. Scaling =====================
st.markdown("### Scaling")
# st.write("Numerical features were scaled to ensure uniformity and optimal model performance")

st.markdown("#### Robust Scaling")
st.markdown("""
- Applied to most numerical features
- Features with non-normal distribution and outliers (e.g., Distance, PumpCount)
""")

st.markdown("#### Standard Scaling")
st.markdown("""
- Applied to numerical features with normal distribution
- Lat/Long of incident and station
""")
st.divider()

# ===================== 4. Feature Selection =====================
st.markdown("### Feature Selection")
# st.write("To reduce the dimensionality")

st.markdown("#### Ordinary Least Squares (OLS) Regression")
st.markdown("""
##### Categorical Features
- ANOVA OLS (F-test) 
- Statistical significance (p-value < 0.05)
- Effect size (partial eta squared $\\eta_p^2$ >= 0.01)
            
##### Numerical Features
- OLS (T-test) 
- Statistical significance (p-value < 0.05)
- Effect size (standardized regression coefficients >= 0.05)           
""")

st.markdown("#### Mutual Information")
st.markdown("""
- Applied to both categorical and numerical features
- Ranked features based on MI scores
- Kept the features with MI scores >= 1% of the highest score
""")

st.markdown("#### Outcome")
st.markdown("""
- Kept the features that were retained by both OLS and MI
- 33 features -> 15 features
""")

st.dataframe(df, height = 200)
st.divider()