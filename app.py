import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Yahan Xie's Portfolio", layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('image/830635990.jpg')
     
st.title('Welcome to My Personal Website!')
st.header('Hello, I am Yahan Xie!:wave:')
st.markdown("""
    <style>
    .about_me_font {
        font-size: 28px; 
    }
    </style>
    <div class='about_me_font'>
        About me
    </div>
    """, unsafe_allow_html=True)

image = Image.open('image/IMG_1079 2.jpg')

original_width, original_height = image.size
new_width = 400
new_height = int(new_width * original_height / original_width)
resized_image = image.resize((new_width, new_height))
col1, col2, col3 = st.columns([1, 1, 1])

with col3:
    st.image(resized_image, caption='Yahan Xie')
with col1:
    st.markdown("""
    <style>
    .font_style {
        font-size:28px; 
    }
    </style>
    <div class='font_style'>
       "Create something useful & cool 🪄"
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <style>
    .font_style {
        font-size:28px; 
    }
    </style>
    <div class='font_style'>
        <📧 Email> xieyahan@uw.edu  <br>
        <☎️ TEL> 425-319-3137  <br>
        HCI researcher <br>
        UI/UX designer <br>
        <br>
        <📖 Education>
        Tsinghua University DESIGN  <br>
        University of  Washington MSTI 
    </div>
    """, unsafe_allow_html=True)