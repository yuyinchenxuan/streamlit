import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Introduction")
st.write("### Introduction and Context")

st.markdown("""
- Fire has played a crucial role in human civilization, offering major benefits while remaining a persistent threat, especially in urban settings.
- To minimize damage such as infrastructure loss, environmental harm, and human casualties, modern societies invest heavily in firefighting strategies.
- A key factor in reducing these costs is response time—the speed between detecting and addressing a fire.
- This project analyzes historical response times from the London Fire Brigade to develop a predictive model aimed at improving response efficiency and reducing fire-related impacts.
""")

# - Fire has been deeply connected to human civilization—initially dangerous but later controlled to enable major innovations (e.g., steel, steam engines, rockets).
# - Despite its benefits, fire has remained a destructive force, sometimes used strategically in warfare.
# - Urban fires have long posed serious threats as humans built permanent settlements and cities.
# - Modern societies invest significant resources in firefighting strategies to reduce fire-related risks and costs.
# - Response time (from detection to firefighting) is a critical factor influencing the severity of fire damage.


st.write("### Objective")
st.markdown("""
- Develop a predictive model to estimate fire attendance times (from mobilization to arrival) leveraing historical data from the London Fire Brigade (one of the world's largest fire services).
- Enable efficient allocation of firefighting resources.
- Support long-term planning and preventive measures to reduce fire-related costs.
- Improve public safety and create a more cost-efficient firefighting system.
""")

# This project develops a predictive model using historical data from the London Fire Brigade to estimate fire attendance times from mobilization to arrival. 
# The model supports efficient resource allocation, informs long-term planning and preventive measures, \
# and ultimately aims to enhance public safety while reducing fire-related costs.