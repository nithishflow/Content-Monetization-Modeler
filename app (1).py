import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="YouTube Monetization Modeler",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("lasso_ad_revenue_model.joblib")

model = load_model()

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🎯 Revenue Prediction", "📊 Model Insights"]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if page == "🏠 Home":

    st.title("📊 Content Monetization Modeler")
    st.image(
    "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
    width=300
    )
    st.markdown("---")

    st.markdown("""
    ### 🚀 Project Overview
    This interactive machine learning application predicts **YouTube ad revenue**
    using engagement metrics and contextual video features.

    The model was built using **Lasso Regression**, trained on historical performance data.
    """)

    st.markdown("### 🧠 What This App Demonstrates")
    st.markdown("""
    - Real-time revenue prediction  
    - Feature importance insights  
    - Interactive model deployment using Streamlit  
    - End-to-end ML pipeline integration  
    """)

    st.markdown("---")
    st.info(
        "Navigate using the sidebar to test revenue predictions or explore model insights."
    )

# ---------------------------------------------------
# PREDICTION PAGE
# ---------------------------------------------------
elif page == "🎯 Revenue Prediction":

    st.title("🎯 Predict YouTube Ad Revenue")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        views = st.number_input("Views", min_value=0, value=10000, step=1000)
        likes = st.number_input("Likes", min_value=0, value=500, step=50)
        comments = st.number_input("Comments", min_value=0, value=50, step=10)
        subscribers = st.number_input("Channel Subscribers", min_value=0, value=50000, step=1000)

    with col2:
        watch_time_minutes = st.number_input(
            "Watch Time (minutes)", min_value=0.0, value=3000.0, step=100.0
        )
        video_length_minutes = st.number_input(
            "Video Length (minutes)", min_value=0.1, value=10.0, step=0.5
        )
        category = st.selectbox(
            "Video Category",
            ["Music", "Gaming", "Tech", "Education", "Entertainment"]
        )
        device = st.selectbox(
            "Primary Device",
            ["Mobile", "Desktop", "TV", "Tablet"]
        )
        country = st.selectbox(
            "Primary Audience Country",
            ["US", "IN", "DE", "UK", "CA"]
        )

    # Feature engineering
    engagement_rate = (likes + comments) / views if views > 0 else 0
    watch_time_per_min = watch_time_minutes / video_length_minutes

    input_df = pd.DataFrame({
        "views": [views],
        "likes": [likes],
        "comments": [comments],
        "watch_time_minutes": [watch_time_minutes],
        "video_length_minutes": [video_length_minutes],
        "subscribers": [subscribers],
        "engagement_rate": [engagement_rate],
        "watch_time_per_min": [watch_time_per_min],
        "category": [category],
        "device": [device],
        "country": [country]
    })

    st.markdown("---")

    if st.button("🚀 Predict Revenue"):
        prediction = model.predict(input_df)[0]

        st.success(f"💰 Estimated Ad Revenue: **${prediction:,.2f} USD**")

        st.caption(
            "Prediction generated using a trained Lasso Regression pipeline."
        )

# ---------------------------------------------------
# MODEL INSIGHTS PAGE
# ---------------------------------------------------
elif page == "📊 Model Insights":

    st.title("📊 Model Insights & Feature Importance")
    st.markdown("---")

    # Extract coefficients
    coefficients = model.named_steps['model'].coef_

    num_features = model.named_steps['preprocessor'].transformers_[0][2]
    cat_features = model.named_steps['preprocessor'] \
        .named_transformers_['cat'] \
        .get_feature_names_out(
            model.named_steps['preprocessor'].transformers_[1][2]
        )

    all_features = np.concatenate([num_features, cat_features])

    coef_df = pd.DataFrame({
        "Feature": all_features,
        "Coefficient": coefficients
    })

    coef_df = coef_df[coef_df["Coefficient"] != 0]
    coef_df["Abs"] = coef_df["Coefficient"].abs()
    coef_df = coef_df.sort_values("Abs", ascending=False).head(10)

    st.subheader("🔝 Top Revenue Drivers")
    st.bar_chart(coef_df.set_index("Feature")["Coefficient"])

    st.markdown("""
    ### 🧠 Key Findings
    
    - **Watch Time** is the strongest predictor of ad revenue.
    - Engagement metrics (likes & comments) significantly increase monetization.
    - Views matter, but retention matters more.
    - Country and device influence revenue due to CPM differences.
    """)

    st.markdown("---")
    st.success("This confirms revenue is driven more by engagement quality than raw reach.")