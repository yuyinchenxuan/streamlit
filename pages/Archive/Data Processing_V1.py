import streamlit as st

st.title("Data Processing")
# ===================== 1. Data Sources =====================
st.markdown("### Data Sources")
st.markdown("""
Combined data from multiple sources:

- **Incident Data** → fire incidents (location, type, pumps)  
- **Mobilisation Data** → response details (timestamps, stations, pumps)  
- **Postcode Data** → latitude & longitude lookup  
- **Station Data** → fire station locations  
""")
st.divider()

# ===================== 2. DATA ENRICHMENT =====================
st.markdown("### Data Enrichment")

st.markdown("#### Incident Location")
st.markdown("""
- Use most precise postcode available  
- Lookup missing coordinates from external datasets  
""")

st.code("Postcode_incident = Postcode_full else Postcode_district")

st.markdown("#### Location Accuracy")
st.code("LocationAccuracy = 0 if Postcode_full is NA else 1")

st.markdown("#### Data Integration")
st.markdown("""
- Joined incident and mobilisation data  
- Enriched with postcode and station datasets  
""")

st.divider()

# ===================== 3. FEATURE ENGINEERING =====================
st.markdown("### Feature Engineering")

st.markdown("""#### Fallback Features \

Used the granular columns when available and falled back to the less granular columns when it is missing
""")
st.code("""
UPRN_D      = UPRN else USRN
Easting_D   = Easting_m else Easting_rounded
""")

st.markdown("#### Time Features")
st.code("""
PumpMinutes_D = time difference
Extract: year, month, day, weekday, hour from Mobilised timestamp
""")

st.markdown("#### Distance Feature")
st.markdown("""
Distance between incident and station coordinates
(using geolocation)
""")

st.divider()

# ===================== 4. OUTLIER HANDLING =====================
st.markdown("### Outlier Handling")

st.markdown("""
- Detected using distribution analysis (e.g., boxplots)  
- Replaced extreme values with median  

**Examples:**  
- PumpCount > 200  
- Distance > 100 or = 0  
""")

st.divider()

# ===================== 5. MISSING VALUE HANDLING =====================
st.markdown("### Missing Value Handling")

st.markdown("""
#### Mode Imputation
- NumCalls, DeployedFromLocation  

#### Categorical Handling
- DelayCodeId → missing = 0  

#### Conditional Imputation
- PumpMinutes_D → incident mean → else global median  

#### Row Removal
- Applied where missing values were minimal  
""")

st.divider()

# ===================== 6. COLUMN REDUCTION =====================
st.markdown("### Column Reduction")

st.markdown("""
- Removed redundant and intermediate columns  

**Final Dataset**
- Original: 63  
- New Features: +18  
- Removed: -47  
- **Final: 33 features and 1 target**
""")