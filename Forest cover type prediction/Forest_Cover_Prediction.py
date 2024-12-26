import streamlit as st
import numpy as np
from PIL import Image
import pickle


model = pickle.load(open('.venv/RFC.pkl', 'rb'))


st.set_page_config(page_title="Forest Cover Type Prediction", layout="wide")
st.title("🌲 Forest Cover Type Predictor")
st.markdown("""
This app predicts the **forest cover type** based on user-provided environmental values.

Please enter the necessary data below to predict the forest type. Each forest cover type is displayed with its name and an image.
""")

st.sidebar.header("Input Features")
user_input = st.sidebar.text_input(
    "Enter forest cover values (comma-separated):",
    help="Provide all necessary features as comma-separated numerical values.")



def predict(user_input):
    user_input = user_input.split(',')
    user_input = np.array([user_input], dtype=np.float64)
    result = model.predict(user_input)
    return int(result[0])



forest_cover_types = {
    1: {"name": "Spruce/Fir", "image": "img_1.jpg"},
    2: {"name": "Lodgepole Pine", "image": "img_2.png"},
    3: {"name": "Ponderosa Pine", "image": "img_3.png"},
    4: {"name": "Cuttonwood/Willow", "image": "img_4.jpg"},
    5: {"name": "Aspen", "image": "img_5.jpeg"},
    6: {"name": "Douglas Fir", "image": "img_6.png"},
    7: {"name": "Krummholz", "image": "img_7.png"},
}


if st.sidebar.button("Predict"):
    if not user_input:
        st.error("Please enter all required forest cover type values.")
    else:
        try:
            result = predict(user_input)


            forest_type = forest_cover_types.get(result)

            if forest_type:
                st.success(f"### 🏞️ Predicted Forest Cover Type: {forest_type['name']}")
                col1, col2 = st.columns([1, 2])

                with col1:
                    st.markdown(f"#### **Forest Name:** {forest_type['name']}")

                with col2:
                    image = Image.open(forest_type['image'])
                    st.image(image, use_column_width=True, caption=forest_type['name'])
            else:
                st.error("Prediction does not match any known forest cover type.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
