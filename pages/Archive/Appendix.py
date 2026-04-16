import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.header("Data Processing")
########################List of Contents########################
with st.expander("Table of Contents"):
    st.markdown("""
    1. [Original Datasets](#1-original-datasets)
    2. [Data Enrichment](#2-data-enrichment)
    3. [Feature Engineering](#3-feature-engineering)
    4. [Outlier Handling](#4-outlier-handling)
    5. [NAN Handling](#5-nan-handling)
    6. [Column Removal](#6-column-removal)
    """)

########################Original Datasets########################
st.subheader("1. Original Datasets")
data_table = pd.DataFrame(
    {
        "Description": ["Fire incident attended by the London Fire Brigade since 2009", "Details of every fire engine sent to an incident since January 2009", "UK full postcodes", "UK postcode outcodes", "London fire stations"],
        "File Name": ["LFB Incident data from YYYY - YYYY.csv", "LFB Mobilisation data from YYYY - YYYY.csv", "ukpostcodes.csv", "postcode-outcodes.csv", "LondonFireStation.csv"],
        "Number of Files": [3, 3, 1, 1, 1],
        "Info": ["Incident Type, Postcode, Lat & Long, Property Type, Number of Pumps Attending", "Timestamps of Mobilization/ Arrival/ Return, Deployed Fire Station, Pump Order, Delay Code", "Postcode, Latitude, Longitude", "Postcode, Latitude, Longitude", "Station Name, Postcode"],
        "Features": [39, 22, 3, 3, 3],
        "Records": [1895667, 2513176, 1800000, 2952, 118]
    },
    index=["Incident Data", "Mobilisation Data", "UK Postcodes Full", "UK Postcodes Outcodes", "London Fire Stations"],
)
st.table(data_table, width = "content")
st.divider()

########################Data Enrichment########################
st.markdown("""
            ### 2. Data Enrichment
            ##### 1) Filling Missing Coordinates of Incidents
""")
st.markdown("""
1. **Create `Postcode_incident`**: use `Postcode_full` if available, else `Postcode_district`  
2. **Fill missing coordinates**: lookup `Postcode_incident` in `ukpostcodes.csv` and `postcode-outcodes.csv`  
3. **Output final dataset** with `Latitude_incident` and `Longitude_incident`
""")
st.markdown("##### 2) New Column - LocationAccuracy")
st.code("""
LocationAccuracy  = 0 if Postcode_full is NA else 1
""")

st.markdown("##### 3) Merge the Datasets")
st.graphviz_chart("""
digraph {
    rankdir=TB;  // top to bottom
    node [shape=box, style=filled, color=lightblue];

    Incident -> df [label="join on IncidentNumber = IncidentNumber"];
    Mobilisation -> df;
    LondonFireStations -> df [label="join on DeployedFromStation_Name = Station\n => Postcode_station"];
    UKPostcodes_Full -> df_pc [label="concatenate"];
    UKPostcodes_Outcodes -> df_pc;
    df_pc -> df [label="join on Postcode_incident = postcode
                  => Latitude_incident, Longitude_incident
join on Postcode_station = postcode
            => Latitude_station, Longitude_station"];
}
""")
st.divider()

########################Feature Engineering########################
st.markdown("### 3. Feature Engineering")
st.write("Created derived columns by using the granular columns when available \
         and falling back to the less granular columns when it is missing (e.g., for “Dwelling” in PropertyCategory).")
st.markdown("##### 1) Derived Columns")
st.code("""
UPRN_D           = UPRN if UPRN != 0 else USRN
Easting_D        = Easting_m if not NA else Easting_rounded
Northing_D       = Northing_m if not NA else Northing_rounded
IncidentGroup_D  = SpecialServiceType if not NA else IncidentGroup
""")
st.markdown("##### 2) Time-Based Metric")
st.code("""
PumpMinutes_D    = DateAndTimeLeft - DateAndTimeArrived
""")
st.markdown("""##### 3) Date-Time Features 
Extracted from `DateAndTimeMobilised`
""")
st.code("""
call_year, call_month, call_day, call_weekday, call_hour
""")
st.markdown("""##### 4) Calculated Feature 
Computed using **`geopy.distance`** from:  
- `Latitude_incident`, `Longitude_incident`  
- `Latitude_station`, `Longitude_station`
""")
st.code("""
Distance
""")
st.divider()

########################Outlier Handling########################
st.markdown("### 4. Outlier Handling")
st.write("Identified outliers based on box plots and replaced them with the median value of the respective feature.")
st.code("""
PumpCount                           where PumpCount > 200
NumCalls                            where NumCalls > 200
NumStationsWithPumpsAttending       where NumStationsWithPumpsAttending > 20
Notional Cost (£)                   where Notional Cost (£) > 500000
Distance                            where Distance > 100 or Distance == 0
""")
st.divider()

########################NAN Handling########################
st.markdown("### 5. NAN Handling")
st.markdown("##### 1) Mode Imputation")
st.code("""
NumCalls                = mode(NumCalls)
DeployedFromLocation    = mode(DeployedFromLocation)
""")
st.markdown("##### 2) Categorical Encoding")
st.code("""
DelayCodeId             = 0 if NA else DelayCodeId
""")
st.markdown("##### 3) Conditional Imputation")
st.code("""
PumpMinutes_D             = mean of pumps within the same incident 
                            else overall median
""")
st.markdown("""##### 4) Row Removal (Listwise Deletion)
For certain features, rows with missing values were removed to ensure data quality.
""")
st.code("PropertyCategory, PropertyType, IncGeo_WardCode, IncidentStationGround, DeployedFromStation_Code, \
Latitude_incident, Longitude_incident, Postcode_station, Latitude_station, Longitude_station, UPRN_D, IncidentGroup_D")
st.divider()

########################Column Removal########################
st.subheader("6. Column Removal")
st.write("Removed columns that were redundant, or used for deriving new features.")
st.write("Final column count: 63 (original) + 18 (new) - 47 (redundant) = 34")
st.markdown("##### 1) Dropped Columns from Incident Data")
st.code("""IncidentNumber, DateOfCall, CalYear, TimeOfCall, HourOfCall, IncGeo_BoroughName, ProperCase, IncGeo_WardName, \
IncGeo_WardNameNew, Easting_m, Northing_m, FirstPumpArriving_AttendanceTime, FirstPumpArriving_DeployedFromStation, \
SecondPumpArriving_AttendanceTime, SecondPumpArriving_DeployedFromStation, Latitude, Longitude, Postcode_full, \
FRS, SpecialServiceType, UPRN, USRN, IncidentGroup, Easting_rounded, Northing_rounded, Postcode_district, NumPumpsAttending, PumpMinutesRounded.
""")
st.markdown("##### 2) Dropped Columns from Mobilisation Data")
st.code("IncidentNumber, ResourceMobilisationId, TurnoutTimeSeconds, TravelTimeSeconds, DateAndTimeLeft, DateAndTimeReturned, \
DeployedFromStation_Name, CalYear, HourOfCall, BoroughName, WardName, DateAndTimeMobile, DateAndTimeArrived, DelayCode_Description, \
PlusCode_Description, PerformanceReporting, DateAndTimeMobilised.")

