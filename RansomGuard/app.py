import streamlit as st
import pandas as pd
from predict import model


st.set_page_config(
    page_title="RansomGuard",
    page_icon="🛡️"
)


with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


st.markdown(
    '<div class="title">🛡️ RansomGuard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ransomware Detection and Early Threat Prevention System</div>',
    unsafe_allow_html=True
)

st.divider()


st.subheader("Upload Forensic Data")

uploaded_file = st.file_uploader(
    "Upload your feature CSV file",
    type=["csv"]
)


if uploaded_file is None:

    st.info("Please upload a CSV file to continue.")
    st.stop()


try:

    data = pd.read_csv(uploaded_file)

except Exception:

    st.error("Unable to read the uploaded CSV file.")
    st.stop()


required_features = model.feature_names_in_


missing_features = [
    feature
    for feature in required_features
    if feature not in data.columns
]


if missing_features:

    st.error("Invalid CSV file. Required features are missing.")
    st.write("Missing features:", missing_features)
    st.stop()


data = data[required_features]


data = data.apply(
    pd.to_numeric,
    errors="coerce"
)


if data.isnull().values.any():

    st.error("CSV contains invalid or missing values.")
    st.stop()


st.success(
    f"CSV validated successfully — {len(data)} samples, 55 features"
)


if st.button("🔍 Detect Threat"):

    predictions = model.predict(data)

    probabilities = model.predict_proba(data)


    ransomware_count = 0

    for prediction in predictions:

        if prediction == "Ransomware":

            ransomware_count += 1


    total_samples = len(predictions)


    if ransomware_count > 0:

        ransomware_class_index = (
            model.classes_.tolist().index("Ransomware")
        )


        ransomware_confidences = []


        for index, prediction in enumerate(predictions):

            if prediction == "Ransomware":

                confidence = (
                    probabilities[index][ransomware_class_index]
                    * 100
                )

                ransomware_confidences.append(confidence)


        average_confidence = (
            sum(ransomware_confidences)
            / len(ransomware_confidences)
        )


        if average_confidence >= 80:

            risk = "HIGH"

        else:

            risk = "MEDIUM"


        prediction_result = "RANSOMWARE"


    else:

        average_confidence = (
            probabilities.max(axis=1).mean()
            * 100
        )

        risk = "LOW"

        prediction_result = "BENIGN"


    st.divider()

    st.subheader("Detection Result")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Prediction</div>
                <div class="result-value">
                    {prediction_result}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Confidence</div>
                <div class="result-value">
                    {average_confidence:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Risk Level</div>
                <div class="result-value">
                    {risk}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    if risk == "HIGH":

        st.error(
            "⚠️ Potential ransomware activity detected!"
        )

        st.markdown(
            """
            <div class="response-box">

            <h4>🛡️ Recommended Response</h4>

            • Isolate the affected system<br>
            • Investigate suspicious activity<br>
            • Restrict affected resources<br>
            • Begin incident response<br>
            • Recover data from a safe backup

            </div>
            """,
            unsafe_allow_html=True
        )


    elif risk == "MEDIUM":

        st.warning(
            "⚠️ Suspicious activity detected. Further investigation is recommended."
        )


    else:

        st.success(
            "✅ No immediate ransomware threat detected."
        )