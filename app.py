import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import plotly.express as px

# Coding - Sentiment Analysis
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from langdetect import detect
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set page configuration
st.set_page_config(page_title="Generative AI", page_icon=":graduation_cap:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">Generative AI - House Plan Generator</h1>
        <br>
    </div>
    """,
    unsafe_allow_html=True,
)

# Navigation bar
selected_nav = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Project", "Contact Us"],
    icons=["house", "person-badge", "book", "flag"],
    default_index=0,
    orientation="horizontal",
)

# Assets
lottie_coding = "https://lottie.host/37ba51a6-3953-4bf7-a72b-09bd2a22ab3b/yHsfbMKPn1.json"

# Header Section
with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Welcome to the Home of Development Team</h2>
            <p>Analysis of Youtube Comments to provide Quality Videos to the User</p>
            <p><strong>Mentor:</strong> Prof. Dr. Deivamani M</p>
            <p><strong>Industry Expert:</strong> Mr. Muthumani M</p>
            <p>Visit our Github Page by clicking <a href="https://github.com/tksuren/Gan_3" target="_blank">here</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

# Content Section
if selected_nav == "Home":
    # Home content
    st_lottie(lottie_coding, height=300, key="coding")

elif selected_nav == "About Us":
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>About Us</b></h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Styling for the avatars and brief info
    avatar_style = """
    <style>
        img {
            border-radius: 50%;
            box-shadow: 0 0 15px 0 rgba(0, 0, 0, 0.3);
            margin: 10px auto 0;
            display: block;
        }
        .avatar-container {
            text-align: center;
            display: block;
            margin: auto;
            width: 100%;
        }
        .avatar-link {
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
            display: block;
        }
    </style>
"""

    st.markdown(avatar_style, unsafe_allow_html=True)

    # Dummy avatars and brief info
    col1, col2, col3 = st.columns(3)

    # Define the target URLs for each image
    url_surendar = "https://github.com/aakgna/Estate_plot_groups"
    url_praveen= "https://github.com/aakgna/Estate_plot_groups"
    url_deepan = "https://github.com/aakgna/Estate_plot_groups"

    # Use markdown and HTML to create the hyperlinks with styling
    with col1:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_surendar}'>Surendar K</a><p>tkbsurendar5@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "I would like to Contribute to the growth of a company by applying my technical skills. "
                "I have a strong passion for problem-solving and a strong desire to continually learn and adapt to emerging technologies."
            )

    with col2:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_praveen}'>Praveen</a><p>praveen.jobconnect@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "A dedicated and adaptable Master's in Computer Applications (MCA) student. "
                "I am enthusiastic about the opportunity to contribute my technical skills and passion for innovation. "
                "With a background in Physics and a strong foundation in programming, I bring a unique perspective to the table and am committed to continual learning and growth within the dynamic field of technology."
            )

    with col3:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_deepan}'>Deepan Raj</a><p>deepan@gmail.com</p></div>",
            unsafe_allow_html=True,
        )
        with st.expander("Expand to know more about me"):
            st.write(
                "I intend to be a part of an organization where I can constantly learn and develop my technical "
                "and management skills and make the best use of it for the growth of the organization. "
                "I look forward to establishing myself by adapting new technologies as well."
            )

    st.write("\n\n")

    st.markdown(
        """
        <div style="text-align: center;">
            <p>We, the students of the College of Engineering, Anna University, are currently pursuing Master of Computer Applications.
            Under the guidance of Dr. Deivamani M (Assistant Professor) and Mr. Muthumani M (Industry Expert) in our academic journey,
            we have collaboratively worked on enhancing Artificial Intelligence, focusing on the responsible identification and mitigation of bias utilizing it in recommendation systems.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif selected_nav == "Project":
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>Project</b></h2>
            <p>Youtube Sentiment Analysis Application</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Abstract
    st.subheader("**Abstract**")

    st.subheader("**Explanation Video**")
    st.video("https://www.youtube.com/watch?v=l8qB0fx2SOc")

    st.divider()

    st.subheader("**References**")

elif selected_nav == "Contact Us":
    # Contact Us content
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>Contact Us</b></h2>
            <p>For any inquiries, please contact us at the following email addresses</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <p><b>General Inquiries:</b> praveen.jobconnect@gmail.com</p>
            <p><b>Technical Support:</b> tkbsurendar5@gmail.com</p>
            <p><b>Project Related Queries:</b> deepanraj@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Add more email IDs as needed

# Add smooth scrolling to the selected section
st.markdown(
    f"""
    <style>
        a[name="{selected_nav.lower().replace(' ', '_')}"] {{
            visibility: hidden;
        }}
        #{selected_nav.lower().replace(' ', '_')} {{
            visibility: visible;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(f'<a name="{selected_nav.lower().replace(" ", "_")}"></a>', unsafe_allow_html=True)
