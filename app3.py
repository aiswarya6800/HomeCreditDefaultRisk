import streamlit as st
import pandas as pd
import pickle

# ========================================
# 1. Page config
# ========================================
st.set_page_config(page_title="Loan Default Prediction", layout="wide")

# ========================================
# 2. Load model & scaler
# ========================================
@st.cache_resource
def load_files():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_files()

# ========================================
# 3. Feature list & humanized labels
# ========================================
full_feature_list = [
    'SK_ID_CURR', 'NAME_CONTRACT_TYPE', 'CODE_GENDER', 'FLAG_OWN_CAR',
    'FLAG_OWN_REALTY', 'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AMT_CREDIT',
    'AMT_ANNUITY', 'AMT_GOODS_PRICE', 'NAME_TYPE_SUITE', 'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE',
    'REGION_POPULATION_RELATIVE', 'DAYS_BIRTH', 'DAYS_EMPLOYED',
    'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'FLAG_MOBIL', 'FLAG_EMP_PHONE',
    'FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE', 'FLAG_PHONE', 'FLAG_EMAIL',
    'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS', 'REGION_RATING_CLIENT',
    'REGION_RATING_CLIENT_W_CITY', 'WEEKDAY_APPR_PROCESS_START',
    'HOUR_APPR_PROCESS_START', 'REG_REGION_NOT_LIVE_REGION',
    'REG_REGION_NOT_WORK_REGION', 'LIVE_REGION_NOT_WORK_REGION',
    'REG_CITY_NOT_LIVE_CITY', 'REG_CITY_NOT_WORK_CITY',
    'LIVE_CITY_NOT_WORK_CITY', 'EXT_SOURCE_2', 'EXT_SOURCE_3',
    'OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE',
    'OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE',
    'DAYS_LAST_PHONE_CHANGE', 'FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_3',
    'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_5', 'FLAG_DOCUMENT_6',
    'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_8', 'FLAG_DOCUMENT_9',
    'FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_11', 'FLAG_DOCUMENT_12',
    'FLAG_DOCUMENT_13', 'FLAG_DOCUMENT_14', 'FLAG_DOCUMENT_15',
    'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_18',
    'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_20', 'FLAG_DOCUMENT_21',
    'AMT_REQ_CREDIT_BUREAU_HOUR', 'AMT_REQ_CREDIT_BUREAU_DAY',
    'AMT_REQ_CREDIT_BUREAU_WEEK', 'AMT_REQ_CREDIT_BUREAU_MON',
    'AMT_REQ_CREDIT_BUREAU_QRT', 'AMT_REQ_CREDIT_BUREAU_YEAR'
]

humanized_labels = {
    'SK_ID_CURR': "Customer ID",
    'NAME_CONTRACT_TYPE': "Loan Contract Type",
    'CODE_GENDER': "Gender",
    'FLAG_OWN_CAR': "Owns a Car",
    'FLAG_OWN_REALTY': "Owns Property",
    'CNT_CHILDREN': "Number of Children",
    'AMT_INCOME_TOTAL': "Annual Income",
    'AMT_CREDIT': "Credit Amount",
    'AMT_ANNUITY': "Loan Annuity",
    'AMT_GOODS_PRICE': "Goods Price",
    'NAME_TYPE_SUITE': "Accompanied By",
    'NAME_INCOME_TYPE': "Income Type",
    'NAME_EDUCATION_TYPE': "Education Level",
    'NAME_FAMILY_STATUS': "Family Status",
    'NAME_HOUSING_TYPE': "Housing Type",
    'REGION_POPULATION_RELATIVE': "Region Population Relative",
    'DAYS_BIRTH': "Age in Days",
    'DAYS_EMPLOYED': "Days Employed",
    'DAYS_REGISTRATION': "Days Since Registration",
    'DAYS_ID_PUBLISH': "Days Since ID Publish",
    'FLAG_MOBIL': "Has Mobile",
    'FLAG_EMP_PHONE': "Has Work Phone",
    'FLAG_WORK_PHONE': "Work Phone Flag",
    'FLAG_CONT_MOBILE': "Mobile Reachable",
    'FLAG_PHONE': "Has Phone",
    'FLAG_EMAIL': "Has Email",
    'OCCUPATION_TYPE': "Occupation Type",
    'CNT_FAM_MEMBERS': "Number of Family Members",
    'REGION_RATING_CLIENT': "Region Rating (Client)",
    'REGION_RATING_CLIENT_W_CITY': "Region Rating with City",
    'WEEKDAY_APPR_PROCESS_START': "Application Weekday",
    'HOUR_APPR_PROCESS_START': "Application Hour",
    'REG_REGION_NOT_LIVE_REGION': "Region Not Live Region Flag",
    'REG_REGION_NOT_WORK_REGION': "Region Not Work Region Flag",
    'LIVE_REGION_NOT_WORK_REGION': "Live Region Not Work Region Flag",
    'REG_CITY_NOT_LIVE_CITY': "City Not Live City Flag",
    'REG_CITY_NOT_WORK_CITY': "City Not Work City Flag",
    'LIVE_CITY_NOT_WORK_CITY': "Live City Not Work City Flag",
    'EXT_SOURCE_2': "External Source 2",
    'EXT_SOURCE_3': "External Source 3",
    'OBS_30_CNT_SOCIAL_CIRCLE': "Obs 30 Social Circle",
    'DEF_30_CNT_SOCIAL_CIRCLE': "Def 30 Social Circle",
    'OBS_60_CNT_SOCIAL_CIRCLE': "Obs 60 Social Circle",
    'DEF_60_CNT_SOCIAL_CIRCLE': "Def 60 Social Circle",
    'DAYS_LAST_PHONE_CHANGE': "Days Since Last Phone Change",
    'FLAG_DOCUMENT_2': "Document 2 Flag",
    'FLAG_DOCUMENT_3': "Document 3 Flag",
    'FLAG_DOCUMENT_4': "Document 4 Flag",
    'FLAG_DOCUMENT_5': "Document 5 Flag",
    'FLAG_DOCUMENT_6': "Document 6 Flag",
    'FLAG_DOCUMENT_7': "Document 7 Flag",
    'FLAG_DOCUMENT_8': "Document 8 Flag",
    'FLAG_DOCUMENT_9': "Document 9 Flag",
    'FLAG_DOCUMENT_10': "Document 10 Flag",
    'FLAG_DOCUMENT_11': "Document 11 Flag",
    'FLAG_DOCUMENT_12': "Document 12 Flag",
    'FLAG_DOCUMENT_13': "Document 13 Flag",
    'FLAG_DOCUMENT_14': "Document 14 Flag",
    'FLAG_DOCUMENT_15': "Document 15 Flag",
    'FLAG_DOCUMENT_16': "Document 16 Flag",
    'FLAG_DOCUMENT_17': "Document 17 Flag",
    'FLAG_DOCUMENT_18': "Document 18 Flag",
    'FLAG_DOCUMENT_19': "Document 19 Flag",
    'FLAG_DOCUMENT_20': "Document 20 Flag",
    'FLAG_DOCUMENT_21': "Document 21 Flag",
    'AMT_REQ_CREDIT_BUREAU_HOUR': "Credit Bureau Requests (Hour)",
    'AMT_REQ_CREDIT_BUREAU_DAY': "Credit Bureau Requests (Day)",
    'AMT_REQ_CREDIT_BUREAU_WEEK': "Credit Bureau Requests (Week)",
    'AMT_REQ_CREDIT_BUREAU_MON': "Credit Bureau Requests (Month)",
    'AMT_REQ_CREDIT_BUREAU_QRT': "Credit Bureau Requests (Quarter)",
    'AMT_REQ_CREDIT_BUREAU_YEAR': "Credit Bureau Requests (Year)"
}

# ========================================
# 4. Step 1 — Paste data
# ========================================
st.title("🏦 Loan Default Probability Predictor")
st.write("Step 1: Paste all feature values in **comma-separated** format.")

input_text = st.text_area("Paste feature values:", height=200)

if st.button("Fill Form"):
    raw_values = input_text.split(",")
    raw_values = [v.strip() for v in raw_values if v.strip() != ""]

    if len(raw_values) == len(full_feature_list) - 1:
        raw_values.insert(0, "0")  # Auto SK_ID_CURR

    if len(raw_values) != len(full_feature_list):
        st.error(f"❌ Expected {len(full_feature_list)} values, but got {len(raw_values)}.")
    else:
        st.session_state["filled_values"] = raw_values
        st.session_state["form_ready"] = True

# ========================================
# 5. Step 2 — Show filled form
# ========================================
if "form_ready" in st.session_state and st.session_state["form_ready"]:
    st.subheader("Step 2: Review Entered Data")
    for feat, val in zip(full_feature_list, st.session_state["filled_values"]):
        st.markdown(f"**{humanized_labels.get(feat, feat)}:** {val}")

    if st.button("Predict"):
        df = pd.DataFrame([st.session_state["filled_values"]], columns=full_feature_list)

        # Convert numeric-looking columns
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                pass

        # Encode categoricals
        for c in df.select_dtypes(include=['object']).columns:
            df[c] = df[c].astype('category').cat.codes

        # Scale without SK_ID_CURR
        scaler_features = [col for col in full_feature_list if col != 'SK_ID_CURR']
        df_scaled_values = scaler.transform(df[scaler_features])

        # Combine SK_ID_CURR back
        df_scaled = pd.concat(
            [df[['SK_ID_CURR']].reset_index(drop=True),
             pd.DataFrame(df_scaled_values, columns=scaler_features)],
            axis=1
        )

        # Predict
        probability = model.predict_proba(df_scaled)[:, 1][0]
        st.success(f"Estimated Probability of Default: **{probability:.2%}**")