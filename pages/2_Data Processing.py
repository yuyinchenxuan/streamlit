import streamlit as st

st.set_page_config(layout="wide")
st.title("Data Processing")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Data Sources", "Data Enrichment", "Feature Engineering", "Outlier Handling", "Missing Value Handling", "Column Reduction"])
# ===================== 1. Data Sources =====================
with tab1:
    #st.markdown("### Data Sources")
    st.markdown("""
    Combined data from multiple sources:

    - **Incident Data** → fire incidents (location, type, pumps)  
    - **Mobilisation Data** → response details (timestamps, stations, pumps, delay codes)  
    - **Postcode Data** → latitude & longitude lookup  
    - **Station Data** → fire station locations  
    """)

# ===================== 2. DATA ENRICHMENT =====================
with tab2:
    #st.markdown("### Data Enrichment")

    col1, col2, col3 = st.columns([1.1, 1, 0.8], vertical_alignment="top", border = True)
    with col1:
        st.markdown("#### Incident Location")
        st.markdown("""
        - Use most precise postcode available  
        - Lookup missing coordinates from external datasets  
        """)
        st.code("Postcode_incident = Postcode_full else Postcode_district")

    with col2:
        st.markdown("#### Location Accuracy")
        st.code("LocationAccuracy = 0 if Postcode_full is NA else 1")

    with col3:
        st.markdown("#### Data Integration")
        st.markdown("""
        - Joined incident and mobilisation data  
        - Enriched with postcode and station datasets  
        """)

# ===================== 3. FEATURE ENGINEERING =====================
with tab3:
    #st.markdown("### Feature Engineering")

    col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top", border = True)
    with col1:
        st.markdown("#### Fallback Features")
        st.write("Used the granular columns when available and falled back to the less granular columns when it is missing")
        st.code("""UPRN_D      = UPRN else USRN   
Easting_D   = Easting_m else Easting_rounded    """)

    with col2:
        st.markdown("#### Time Features")
        st.code("""PumpMinutes_D = time difference
Extract: year, month, day, weekday, hour 
        from Mobilised timestamp""")

    with col3:
        st.markdown("#### Distance Feature")
        st.markdown("""
        Distance between incident and station coordinates
        (using geolocation)
        """)

# ===================== 4. OUTLIER HANDLING =====================
with tab4:
    #st.markdown("### Outlier Handling")

    st.markdown("""
    - Detected using distribution analysis (e.g., boxplots)  
    - Replaced extreme values with median  

    **Examples:**  
    - PumpCount > 200  
    - Distance > 100 or = 0  
    """)

# ===================== 5. MISSING VALUE HANDLING =====================
with tab5: 
    #st.markdown("### Missing Value Handling")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], vertical_alignment="top", border = True)
    with col1:
        st.markdown("#### Mode Imputation")
        st.markdown("""
        - NumCalls, DeployedFromLocation  
        """)
    with col2:
        st.markdown("#### Categorical Handling")
        st.markdown("""
        - DelayCodeId → missing = 0  
        """)

    with col3:
        st.markdown("#### Conditional Imputation")
        st.markdown("""
        - PumpMinutes_D →  
        incident mean → else global median  
        """)

    with col4:
        st.markdown("#### Row Removal")
        st.markdown("""
        - Applied where missing values were minimal  
        """)

# ===================== 6. COLUMN REDUCTION =====================
with tab6:
    #st.markdown("### Column Reduction")

    st.markdown("""
    - Removed duplicate fields
    - Kept more detailed features
    - Removed same information in different formats
    - Kept only relevant timestamp

    **Final Dataset**
    - Original: 63  
    - New Features: +18  
    - Removed: -47  
    - **Final: 33 features and 1 target**
    """)