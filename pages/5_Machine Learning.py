
import streamlit as st
import pandas as pd

df = pd.read_csv("training_score.csv", sep = ';')
num_cols = df.select_dtypes(include='float64').columns
models_linear = ["Linear Regression", "Ridge Default", "Lasso Default", "ElasticNet Default"]
df_linear = df[df['Model'].isin(models_linear)].sort_values(by = ["Type", "R2 TEST", "Model"], ascending = [True, False, True]).reset_index(drop=True)
df_nonlinear = df[(~df['Model'].isin(models_linear)) & (df['Type'] != 'Optimized')].sort_values(by = ["Type", "R2 TEST", "Model"], ascending = [True, False, True]).reset_index(drop=True)
df_optimized = df[df['Type'] == 'Optimized'].sort_values(by = ["R2 TEST", "Model"], ascending = [False, True]).reset_index(drop=True)
df_linear = df_linear.style.format({col: "{:.4f}" for col in num_cols})
df_nonlinear = df_nonlinear.style.format({col: "{:.4f}" for col in num_cols})
df_optimized = df_optimized.style.format({col: "{:.4f}" for col in num_cols})

st.title("Machine Learning")
st.markdown("""
- Trained default linear and non-linear regression models, then picked 4 best performing models for hyperparameter tuning
- Trained on full data set and feature reduced data set 
- Metrics
    - R² (coefficient of determination): Test data
    - MAE (mean absolute error): Test data
    - RMSE (root mean squared error): Test and Training data
    - 5-Fold CV RMSE: Training data
""")

# ===================== Training =====================
st.markdown("### Training")

# ===================== Linear Models ================
st.markdown("#### Linear Models")
st.markdown("""
- Linear Regression, Ridge, Lasso, Elastic Net
- Linear and Ridge Regression, higher R², lower MAE and RMSE 
- Residuals of Linear Regression: non-normal distribution -> non-linear models could perform better
""")
st.markdown("")

pic1, desc1 = st.columns([2, 1], vertical_alignment="center")  
with pic1:
    c1, c2, c3 = st.columns([0.5, 8, 1])  
    with c2:
        st.image("ResidualLinear.png")

# col1, col2, col3 = st.columns([2, 1, 0.5], vertical_alignment="center")  
# with col1:
#     c1, c2= st.columns([8, 0.2])  
#     with c1:
#         st.image("ResidualLinear.png")

with desc1:
    st.markdown("""
    **Residuals of Linear Regression**  

    - Q-Q Plot: Skewness: -1.63, Kurtosis: 9.08
    - Q-Q Plot: non-normal on left and right tails
    - Histogram: higher frequency at center, lower frequency at tails
    """)

st.markdown("")
with st.expander("Training Scores of Linear Models"):
    st.dataframe(df_linear, height = 200)
st.markdown("")

# ===================== Non-Linear Models ================
st.markdown("#### Non-Linear Models")
st.markdown("""
- Decision Tree, Random Forest, Gradient Boosting, LightGBM, XGBoost, CatBoost, MLP
- Best performing: CatBoost -> Random Forest -> XGBoost
""")
st.markdown("")
with st.expander("Training Scores of Non-Linear Models"):
    st.dataframe(df_nonlinear, height = 200)
st.divider()

# ===================== Optimization =====================
st.markdown("### Optimization")
data_table = pd.DataFrame(
    {
        "Ridge": ["RidgeCV", "alpha", ":yellow[No change]"],
        "Random Forest": ["BayesSearchCV", "n_estimators, max_depth, min_samples_split, min_samples_leaf, max_features", ":green[0.6463 -> 0.6484]"],
        "Catboost": ["BayesSearchCV", "learning_rate, depth, l2_leaf_reg, bagging_temperature", ":green[0.6974 -> 0.6996]"],
        "MLP": ["BayesSearchCV", "n_layers, n_units, alpha, learning_rate_init, batch_size, activation, solver", ":red[0.6447 -> 0.6300]"]
    },
    index=["Tuning Approach", "Tuned Hyper Parameters", "R²"],
)
st.table(data_table, width = "content")

st.markdown("")
with st.expander("Training Scores of Optimized Models"):
    st.dataframe(df_optimized, height = 200)
st.markdown("")

# ===================== Performance Evaluation =====================
st.markdown("### Performance Evaluation")
st.markdown("""
- Optimized CatBoost: R² = 0.70, RMSE = 82.66 seconds. Moderate to strong predictive performance.
- Model prediction is far off when the true attendance time is close to 0 or 800 - 1200 seconds.
""")
pic2, desc2 = st.columns([2, 1.5], vertical_alignment="center") 
with pic2:
    st.image("PerformanceEvaluation.png")