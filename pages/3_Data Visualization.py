import streamlit as st

st.title("Data Visualization")
st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["General Analysis", "Target Variable", "Numerical Variable", "Categorical Variable"])

######## General Analysis ##########
with tab1:
    #st.subheader("General Analysis")
    pic1, desc1 = st.columns([2, 1], vertical_alignment="center")  

    with pic1:
        c1, c2, = st.columns([1.5, 1])  
        c1.image("NumberofIncidents.png")
        c2.image("IncidentDistributionbyGroup.png")

    with desc1:
        st.markdown("""
        **Incident Count**
                    
        - 2009 - 2014, declining trend 
        - 2014 - 2020, stable 
        - 2020 - 2024, increasing trend
        - Mean: 111K, Std: 12K
        - Roughly 50% of all the incidents are False Alarms
        """)

######## Target Variable ##########
with tab2:
    #st.subheader("Target Variable")
    pic2, desc2 = st.columns([2, 1], vertical_alignment="center")  
    with pic2:
        c1, c2, c3 = st.columns([1.5, 6, 1])  
        with c2:
            st.image("AttendanceTime1.png")

    with desc2:
        st.markdown("""
        **Attendance Time**  

        - Skewed to the right with outliers of up to 1200 seconds
        - Predefined threshold of 1200 seconds could be applied.
        - Attendance time close to 0 second could be due to cancellation of the incident, false alarms or data error.
        """)

######## Numberical Variable Analysis ##########
with tab3:
    sections = st.radio(
    "",
    ["Correlation with Target", "Distance"],
    horizontal=True
    )
    
    ######## Correlation with Target ##########
    if sections == "Correlation with Target":
        pic3, desc3 = st.columns([2, 1], vertical_alignment="center")  
        with pic3:
            c1, c2, c3 = st.columns([1, 6, 1])  
            with c2:
                st.image("CorrelationwithTarget.png")

        with desc3:
            st.markdown("""
            - Significance (descending order): DelayCodeId, Distance, PumpOrder, NumStationsWithPumpsAttending, PumpCount
            - High Correlation: Longitude_incident - Longitude_station, Latitude_incident - Latitude_station
            """)

    ############### Distance ##################
    elif sections == "Distance":
        pic4, desc4 = st.columns([2, 1], vertical_alignment="center")  
        with pic4:
            c1, c2, c3 = st.columns([0.95, 1, 0.1])  
            c1.image("DistancevsAttendance.png")
            c2.image("Distance.png")

        with desc4:
            st.markdown("""
            - Non-linear relationship with Attendance Time
            - Short distance with long Attendance Time indicates Distance is not the only factor
            - Distribution skewed to the right with outliers of 120 - 140 km
            """)

######## Categorical Variable Analysis ##########
with tab4:
    #st.subheader("Categorical Variable")
    pic5, desc5 = st.columns([2, 1], vertical_alignment="center")  
    with pic5:
        c1, c2, c3 = st.columns([1.5, 6, 1])  
        with c2:
            st.image("DelayCodeId.png")

    with desc5:
        st.markdown("""
        **Delay Code ID**  

        - DelayCodeId 5 (Address incomplete/wrong): highest median Attendance Time and high variability (IQR)
        - DelayCodeId 8 (Traffic calming) and 12 (Not held up): lowest median Attendance Time and longest tails - faster Attendance Time
        """)