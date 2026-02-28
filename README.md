📊 ContentMonetizationModeler

🎥 YouTube Video Revenue Analytics & Prediction

📌 Project Overview
---
ContentMonetizationModeler analyzes YouTube video performance across categories, devices, and countries to uncover key drivers of ad revenue and audience engagement.

The project combines Exploratory Data Analysis (EDA), Feature Engineering, and Machine Learning modeling to predict ad revenue and extract actionable business insights.

The goal is to transform raw engagement metrics into strategic intelligence for creators, advertisers, and media companies.
---
📁 Dataset Overview

The dataset captures YouTube video performance metrics, including:
```bash
📺 Views

👍 Likes

💬 Comments

⏱ Watch Time (Minutes)

📏 Video Length

👥 Subscribers

🌍 Country

📱 Device Type

🎭 Category

💰 Ad Revenue (Target Variable)
```
Key Characteristics:
---
Covers multiple content categories and audience segments

Includes monetization data (ad revenue)

Minimal missing values

Structured for predictive modeling and business analysis
---
🎯 Project Objectives
---
Analyze trends and correlations affecting ad revenue

Engineer engagement-based features

Apply preprocessing & outlier handling

Compare multiple regression models

Identify key revenue-driving factors

Save and deploy a trained revenue prediction model
---
🔍 Exploratory Data Analysis (EDA)
---
EDA was conducted to:

Identify missing values

Examine revenue distribution

Detect skewness

Analyze correlation between engagement metrics and revenue

Compare revenue across categories and devices
---
Key Insights:
```bash
📈 Watch Time is the strongest driver of ad revenue

👍 Likes and comments positively influence revenue

📱 Device type impacts monetization patterns

🌍 Country-level differences affect revenue performance
```
🛠 Feature Engineering
---
New features were created to enhance predictive power:

Engagement Rate

(likes + comments) / views

Watch Time per Minute

watch_time_minutes / video_length_minutes

These features capture viewer interaction quality and content efficiency.
---
🧹 Data Preprocessing
---
Missing value handling (Median for numeric, Mode for categorical)

Percentile-based outlier capping (1%–99%)

Feature scaling using StandardScaler

Categorical encoding using OneHotEncoder

Train-Test Split (80–20)

A Pipeline + ColumnTransformer was implemented to ensure:

Consistent preprocessing

Prevention of data leakage

Production-ready workflow
---
🤖 Model Training & Evaluation
---
Multiple regression models were evaluated:

Linear Regression

Ridge Regression

Lasso Regression

ElasticNet

Random Forest Regressor
---
Models were compared using:
---
📊 R² Score

📉 RMSE

📏 MAE
---
Final Model:
---
Lasso Regression was selected for:

Feature selection capability

Model simplicity

Strong performance stability
---
🧠 Feature Importance (Lasso Insights)

Top Revenue Drivers:
---
⏱ Watch Time (Strongest impact)

👍 Likes

💬 Comments

👀 Views
---
📱 Device Type (TV & Desktop variations)
```bash
Lasso automatically eliminated non-impactful features by shrinking coefficients to zero.
```
💾 Model Deployment
---
The trained pipeline was saved using:

joblib.dump(lasso_pipeline, "lasso_ad_revenue_model.joblib")

This allows:

Integration into a Streamlit app

Real-time revenue prediction

Deployment without retraining
----
🎯 Business Use Cases
📈 Content Strategy Optimization
---
Identify high-performing categories and device combinations.

Example:
Lifestyle videos on tablets in the UK generate superior revenue.
---
💸 Revenue Forecasting
---
Predict earnings for new video uploads based on engagement metrics.

Example:
Estimate ad revenue for a 10-minute Entertainment video targeting desktop users in the US.
---
🧰 Creator Support Tools
---
Build dashboards that recommend content improvements.

Example:
Flag low engagement videos and suggest optimal upload strategies.
---
📊 Ad Campaign Planning
---
Assist advertisers in selecting high-ROI audience segments.

Example:
Target Gaming videos viewed on TVs in high-revenue countries.
---
🛠 Technologies Used
---
Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

Joblib

Git & GitHub
---
🚀 Future Improvements
---
Hyperparameter tuning

Cross-validation

Advanced ensemble modeling

Streamlit UI enhancement

Real-world dataset integration
---
📌 Conclusion
---
ContentMonetizationModeler demonstrates how engagement metrics can be transformed into revenue intelligence through structured analysis and machine learning.

The project highlights:

Strong relationship between watch time and revenue

Importance of feature engineering

Benefits of L1 regularization for feature selection

Production-ready ML pipeline implementation
---
