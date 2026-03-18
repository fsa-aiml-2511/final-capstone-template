"""
Capstone Web Application
========================
Integrates all 5 models into a single web interface using Streamlit.

Run locally:  streamlit run webapp/app.py
Deploy:       streamlit run webapp/app.py  (or deploy to Streamlit Community Cloud)
"""
import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Capstone Dashboard",
    page_icon="🔬",
    layout="wide",
)

st.title("AI Capstone Dashboard")
st.write("Select a model from the sidebar to make predictions.")

# Sidebar navigation
model_choice = st.sidebar.selectbox(
    "Choose a Model",
    [
        "Home",
        "Model 1: Traditional ML",
        "Model 2: Deep Learning",
        "Model 3: CNN (Image Classification)",
        "Model 4: NLP (Text Classification)",
        "Model 5: Innovation",
    ],
)

# ---------------------------------------------------------------------------
# Model pages — fill these in with your model loading and prediction logic
# ---------------------------------------------------------------------------

if model_choice == "Home":
    st.write("Welcome! Use the sidebar to navigate between models.")
    st.write("Each model page lets you input data and see predictions in real time.")

elif model_choice == "Model 1: Traditional ML":
    st.header("Model 1: Traditional ML")
    # TODO: Add input fields for your features
    # TODO: Load your saved model and run predictions
    # Example:
    # import joblib
    # model = joblib.load("models/model1_traditional_ml/saved_model/model.joblib")
    # if st.button("Predict"):
    #     prediction = model.predict(input_data)
    #     st.write(f"Prediction: {prediction}")
    st.info("Not yet implemented — load your model and add input fields here.")

elif model_choice == "Model 2: Deep Learning":
    st.header("Model 2: Deep Learning")
    # TODO: Load your DNN model and add prediction interface
    st.info("Not yet implemented — load your model and add input fields here.")

elif model_choice == "Model 3: CNN (Image Classification)":
    st.header("Model 3: CNN — Image Classification")
    # TODO: Add image upload and prediction
    # Example:
    # uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    # if uploaded_file is not None:
    #     image = Image.open(uploaded_file)
    #     st.image(image, caption="Uploaded Image", use_container_width=True)
    #     if st.button("Classify"):
    #         prediction = model.predict(image)
    #         st.write(f"Prediction: {prediction}")
    st.info("Not yet implemented — add image upload and classification here.")

elif model_choice == "Model 4: NLP (Text Classification)":
    st.header("Model 4: NLP — Text Classification")
    # TODO: Add text input and prediction
    # Example:
    # user_text = st.text_area("Enter text to classify:")
    # if st.button("Classify") and user_text:
    #     prediction = model.predict(user_text)
    #     st.write(f"Prediction: {prediction}")
    st.info("Not yet implemented — add text input and classification here.")

elif model_choice == "Model 5: Innovation":
    st.header("Model 5: Innovation")
    # TODO: Add your custom model interface
    st.info("Not yet implemented — add your innovation model interface here.")
