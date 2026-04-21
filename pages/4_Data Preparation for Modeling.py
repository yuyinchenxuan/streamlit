import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
df = pd.read_csv("feature_selection.csv", sep = ';')

st.title("Data Preparation for Modeling")

tab1, tab2, tab3, tab4 = st.tabs(["Data Split", "Encoding", "Scaling", "Feature Selection"])
# ===================== 1. Split Data =====================
with tab1:
    # st.markdown("### Data Split")
    st.markdown("""
    - Used 20% of the whole dataset (2.3 million records) for acceptable training time
    - 80% training data, 20% test data  
    """)

# ===================== 2. Encoding =====================
with tab2:
    # st.markdown("### Encoding")
    # st.write("Encoded categorical features into numerical values for modeling")
    col1, col2, col3 = st.columns([1, 0.2, 1], vertical_alignment="top")
    with col1:
        st.markdown("#### One-Hot Encoding")
        st.markdown("""
        - Features with 10-15 categories
        - IncidentGroup_D (23 categories) and IncGeo_BoroughCode (33 categories).   
        Better model performance than Target and Binary Encoding.
        - Cyclical features derived from Mobilised timestamp.   
        Better model performance than Repeating Basis Function.
        """)

    with col3:
        st.markdown("#### Target/Binary Encoding")
        st.markdown("""
        - Used for the rest of the categorical features (more than 100 categories)
        - Decision between the two based on model performance
        """)

# ===================== 3. Scaling =====================
with tab3:
    # st.markdown("### Scaling")
    # st.write("Numerical features were scaled to ensure uniformity and optimal model performance")
    col1, col2, col3 = st.columns([1, 0.2, 1], vertical_alignment="top")
    with col1:
        st.markdown("#### Robust Scaling")
        st.markdown("""
        - Applied to most numerical features
        - Features with non-normal distribution and outliers (e.g., Distance, PumpCount)
        """)

    with col3:
        st.markdown("#### Standard Scaling")
        st.markdown("""
        - Applied to numerical features with normal distribution
        - Lat/Long of incident and station
        """)

# ===================== 4. Feature Selection =====================
with tab4:
    # st.markdown("### Feature Selection")
    # st.write("To reduce the dimensionality")
    section = st.radio(
    "",
    ["OLS Regression", "Mutual Information", "Outcome"],
    horizontal=True
    )
    if section == "OLS Regression":
        # st.markdown("#### Ordinary Least Squares (OLS) Regression")
        col1, col2, col3 = st.columns([1, 0.2, 1], vertical_alignment="top")
        with col1:
            st.markdown("""
            ##### Categorical Features
            - ANOVA OLS (F-test) 
            - Statistical significance (p-value < 0.05)
            - Effect size (partial eta squared $\\eta_p^2$ >= 0.01)
            """)

        with col3:        
            st.markdown("""
            ##### Numerical Features
            - OLS (T-test) 
            - Statistical significance (p-value < 0.05)
            - Effect size (standardized regression coefficients >= 0.05)           
            """)

    elif section == "Mutual Information":
        # st.markdown("#### Mutual Information")
        st.markdown("""
        - Applied to both categorical and numerical features
        - Ranked features based on MI scores
        - Kept the features with MI scores >= 1% of the highest score
        """)

    elif section == "Outcome":
        # st.markdown("#### Outcome")
        st.markdown("""
        - Kept the features that were retained by both OLS and MI
        - 33 features -> 15 features
        """)

        with st.expander("ANOVA and MI Results"):
            st.dataframe(df, height = 200)