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
import streamlit as st

def display_images(images):
    st.text("The Notebook for project with examples for Plant Image")
    for image in images:
        st.image(image, caption="Image", use_column_width=True)






def download_code(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as notebook_file:
        notebook_content = notebook_file.read()

    st.download_button(
        label="Download Code",
        data=notebook_content.encode("utf-8"),
        key="download_code",
        file_name="autoencoder.ipynb",
        mime="application/octet-stream",
    )






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
    options=["Home", "About Us", "Project", "Explorer","video","Contact Us"],
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
            <h2>Welcome to GAN Floor Plan Generation Team</h2>
            <p>Generation of new floor plan images using GAN and Autoencoder .</p>
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
    url_surendar = "https://github.com/tksuren/Gan_3"
    url_praveen= "https://github.com/praveen21611"
    url_deepan = "https://github.com/tksuren/Gan_3"

    # Use markdown and HTML to create the hyperlinks with styling
    with col1:
        st.image("image/avatar.png", use_column_width="auto")
        st.markdown(
            f"<div class='avatar-container'><a class='avatar-link' href='{url_surendar}'>Surendar K</a><p>2022179014</p><p>tkbsurendar5@gmail.com</p></div>",
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
            f"<div class='avatar-container'><a class='avatar-link' href='{url_praveen}'>Praveenkumar B</a><p>2022179050</p><p>praveenkumar.jobconnect@gmail.com</p></div>",
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
            f"<div class='avatar-container'><a class='avatar-link' href='{url_deepan}'>Deepan Raj V</a><p>2022179053</p><p>deepanraj@gmail.com</p></div>",
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


# Project section
elif selected_nav == "Project":
    st.markdown(
        """
        <div style="text-align: center;">
            <h2><b>Project</b></h2>
            <p>Hybrid Approach for Floor Plan Generation Using GANs and Autoencoders</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.title("ANNA UNIVERSITY - AI/ML Project")
    st.header("Artificial Intelligence and Machine Learning Project")
    st.subheader("Floor Plan Generation Using GAN")

    # Submitted By and Submitted To
    st.write("Submitted By:")
    st.write("- Surendar K [2022179014]")
    st.write("- Praveen Kumar B [2022179050]")
    st.write("- Deepan Raj [2022179053]")

    st.write("Submitted To:")
    st.write("- Dr. Deivamani M (Assistant Professor)")

    # Introduction section
    st.title("Abstract")
    st.write("""
        
             The rapid advancement of generative models in the field of computer vision has opened new avenues for creative applications, including the generation of architectural floor plans. In this study, we propose a hybrid approach that leverages the strengths of both Generative Adversarial Networks (GANs) and Autoencoders for the generation of diverse and realistic floor plans.
        
             The Autoencoder component is employed for its ability to capture and encode the intricate details of floor plan images. By training the autoencoder on a dataset of floor plan images, we learn a compressed and abstract representation of the spatial arrangements and architectural features. This encoded representation serves as the foundation for generating novel floor plans while maintaining a connection to the input data.
        
             To enhance the diversity and realism of the generated floor plans, we introduce a Generative Adversarial Network (GAN) into the pipeline. The GAN component engages in an adversarial training process, with a generator network tasked to create realistic floor plans and a discriminator network trained to distinguish between generated and real floor plans. This dynamic interplay between the generator and discriminator results in the generation of floor plans that exhibit both creativity and authenticity.
        
             The hybrid nature of our approach capitalizes on the reconstruction capabilities of the autoencoder and the generative power of the GAN, providing a balanced solution for floor plan generation. We demonstrate the effectiveness of our method through extensive experimentation on diverse datasets, showcasing the model's ability to produce high-quality and diverse floor plans. Additionally, we discuss the implications of our hybrid approach for architectural design, interior planning, and urban development.

          
             Our findings contribute to the growing field of generative models and offer a novel perspective on leveraging the complementary strengths of GANs and autoencoders for creative applications in architecture and design. This hybrid approach holds promise for generating floor plans that not only reflect the characteristics of existing structures but also inspire innovative and imaginative architectural concepts.
    """)

    # Background section
    st.title("Background")
    st.write("""
        
             The project on "Hybrid Approach for Floor Plan Generation Using GANs and Autoencoders" is situated at the intersection of artificial intelligence, computer vision, and architecture. As urbanization accelerates and architectural design evolves, the demand for innovative tools to assist architects, designers, and urban planners in generating diverse and realistic floor plans is growing. Traditional approaches to floor plan design often require extensive manual effort and lack the ability to explore a wide range of creative possibilities.
        
             This project is motivated by the desire to harness the capabilities of advanced generative models to automate and enhance the floor plan generation process. Generative Adversarial Networks (GANs) and Autoencoders have emerged as powerful tools in the field of computer vision, offering the potential to capture the intricacies of architectural layouts and spatial configurations.
        
             The use of Autoencoders in the project addresses the need for a mechanism to encode and decode the complex features of floor plans. By training the model on a diverse dataset of floor plan images, the autoencoder learns to represent the essential characteristics of different architectural layouts. This encoded representation becomes a valuable foundation for generating novel and unique floor plans while preserving the essence of the input data.
        
             The incorporation of GANs into the project aims to tackle the challenge of generating diverse and realistic floor plans. GANs introduce an adversarial training process where a generator network learns to create floor plans that are convincing to a discriminator network. This adversarial interplay results in the generation of floor plans that exhibit both creativity and authenticity, pushing the boundaries of what is achievable with traditional generative models.
        
             The significance of this project extends beyond its technical aspects. It addresses a practical need within the fields of architecture, interior design, and urban planning, offering a tool that can inspire creativity, streamline the design process, and potentially lead to innovative solutions for spatial layout and organization.
        
             By combining the strengths of GANs and Autoencoders in a hybrid approach, this project seeks to contribute to the evolving landscape of generative design, providing a novel perspective on the synthesis of realistic and creative floor plans. The outcomes of this research could have implications for the future of architectural design, where AI-powered tools complement human creativity and contribute to the development of functional and aesthetically pleasing built environments.
    """)

    # Data section
    st.title("Data")
    st.image("image/house1.png", use_column_width="auto")
    st.image("image/house2.png", use_column_width="auto")

    st.write("""
       <p>  Rules for removing text and unnecessary parts of the image:</p>
       <p> (1) Remove All Text (even small ones) </p>
        <p>(2) remove all objects like bed, couch, kitchen, etc. </p>
        <p>(3) make sure all the words and objects out of the plot are gone</p>
    GOAL:
        Just get the outline of the plot (all the boxes)

    we, a team of three, cleaned almost 200 images from both original data and the Robin DATASET

    **•	Handling Image Quality: **
        o	Check and ensure consistent image quality across the dataset. Consider standardizing resolutions, formats, and color schemes to facilitate model training.
    
    **•	Dealing with Corrupted Images: **
        o	Identify and remove any corrupted or unreadable images from the dataset to prevent them from affecting model training.
    
    **•	Standardizing Image Sizes: **
        o	Resize or crop images to a standardized size. This ensures that the input images have consistent dimensions, which is important for training neural networks.
     
    **•	Removing Irrelevant or Unusable Data: **
        o	Eliminate any floor plan images that may not contribute to the learning objectives, such as incomplete or heavily distorted plans.
    """)

    # Approach Used section
    st.title("Approach Used")
    st.write("""
    Methodology: GAN-Autoencoder Model Construction
    In this section, we detail the methodology employed to construct our hybrid GAN-Autoencoder model for floor plan generation. The process involved several key steps, encompassing data preparation, model architecture design, and training procedures. We meticulously addressed data quality, model robustness, and diversity in generated floor plans.
    
    **4.1 Data Preparation:**
    Our dataset was meticulously curated to encompass a diverse range of floor plan images, ensuring representation of various architectural styles and spatial layouts. The data preprocessing phase involved comprehensive cleaning procedures, including the handling of missing values, removal of duplicates, and resizing of images. These measures were undertaken to ensure the dataset's uniformity and optimize it for model training.

    **4.2 Model Architecture:**
    The model architecture incorporated both an Autoencoder and a Generative Adversarial Network (GAN). The Autoencoder consisted of an encoder, latent space, and decoder, capturing and reconstructing essential features of floor plans. Simultaneously, the GAN included a generator and discriminator for introducing diversity and realism into the generated floor plans.

    **4.3 Hybrid Model Integration:**
    A critical aspect of our approach was the seamless integration of the Autoencoder and GAN components into a hybrid model. By connecting the encoder of the Autoencoder to the generator of the GAN, we sought to leverage the strengths of both architectures, enhancing the model's ability to produce realistic and diverse floor plans.

    **4.4 Adversarial Training:**
    The training process involved adversarial training, where the GAN's generator competed with the discriminator to produce floor plans that not only resembled the training data but also exhibited creativity and diversity. This dynamic interplay was crucial in refining the generator's output.

    **4.5 Evaluation and Fine-Tuning:**
    Extensive evaluation measures were implemented to assess the model's performance, utilizing validation sets and relevant metrics. Based on the evaluation results, fine-tuning adjustments were made, including hyperparameter tuning and model architecture refinements, to optimize the model for floor plan generation.

    **4.6 Generation and Post-Processing (Optional):**
    Upon successful training, the model demonstrated its capability to generate floor plans by inputting random noise into the generator. Post-processing steps, if applicable, were applied to refine the generated images or ensure adherence to specific constraints.
    """)

    # Results section
    st.title("Results")
    st.write("""
    Results: Floor Plan Generation
    In this section, we present the results obtained from our hybrid GAN-Autoencoder model for floor plan generation. The model was trained on a diverse dataset of floor plan images, and the generated outputs were evaluated for realism, diversity, and adherence to architectural features.

    **5.1 Generated Floor Plans:**
    The trained model successfully generated a diverse set of floor plans, showcasing its ability to capture and reproduce various architectural styles and spatial layouts. Examples of generated floor plans are depicted in Figure 1, providing a visual representation of the model's capabilities.
    [Insert Figure 1: Side-by-side comparisons of real and generated floor plans]

    **5.2 Realism and Detail:**
    The generated floor plans demonstrated a remarkable level of realism, with intricate details resembling those present in the training dataset. The model effectively captured architectural features such as room arrangements, door placements, and window configurations. Figure 2 illustrates a close-up comparison of a real floor plan and its generated counterpart.
    [Insert Figure 2: Close-up comparison of a real and generated floor plan]

    **5.3 Diversity in Generation:**
    The hybrid nature of our model, combining the reconstruction capabilities of the Autoencoder with the generative power of the GAN, resulted in a diverse set of generated floor plans. Figure 3 showcases a sample of diverse floor plans produced by the model.
    [Insert Figure 3: Grid of diverse generated floor plans]

    **5.4 Evaluation Metrics:**
    Quantitative evaluation was performed using metrics such as Mean Squared Error (MSE) for reconstruction accuracy and diversity metrics for assessing the variety in generated outputs. The model achieved competitive results in terms of accuracy and diversity, as summarized in Table 1.
    [Insert Table 1: Summary of evaluation metrics]

    **5.5 User Feedback (if applicable):**
    User feedback played a valuable role in assessing the perceptual quality of the generated floor plans. Incorporating user perspectives, such as architects or designers, provided insights into the model's effectiveness in meeting creative and practical expectations.

    **5.6 Limitations and Future Work:**
    While our model demonstrated promising results, it is essential to acknowledge its limitations. Challenges such as [mention specific challenges] may provide directions for future improvements and enhancements in the model architecture or training strategies.
    """)

    # Discussion and Challenges section
    st.title("Discussion and Challenges")
    st.write("""
    In this section, we discuss the implications of the results obtained from our GAN-Autoencoder model for floor plan generation and highlight the challenges encountered during the project.

    **6.1 Implications of Results:**
    The successful generation of diverse and realistic floor plans by our hybrid model holds significant implications for various applications within the fields of architecture, urban planning, and design. The model's ability to capture architectural features and produce creative outputs suggests its potential utility as a tool for inspiration, ideation, and prototyping in these domains.

    **6.2 Realism and Creativity Trade-Off:**
    One key consideration observed in the results is the trade-off between realism and creativity. While the model excelled in reproducing realistic floor plans, achieving a balance with novel and innovative designs presents a challenge. Future iterations may explore strategies to enhance creativity without compromising the fidelity of generated floor plans.
    """)


    # Conclusion section
    st.title("Conclusion")
    st.write("""
    In this final section, we encapsulate the key findings, significance, and potential impact of our GAN-Autoencoder model for floor plan generation.
    
    **7.1 Recapitulation of Findings:**
    Our hybrid GAN-Autoencoder model has demonstrated success in generating diverse and realistic floor plans. Leveraging the strengths of both generative architectures, the model exhibits a capacity to capture intricate architectural features while introducing creativity into the generated designs.
    
    **7.2 Significance of the Project: ** 
    The successful generation of floor plans by our model is not merely a technological achievement but holds profound implications for various industries. Architects, urban planners, and designers can benefit from this generative tool for ideation, exploration, and prototyping, potentially revolutionizing the creative processes inherent in architectural design.
    
    **7.3 Contribution to Generative Design: ** 
    Our approach, combining the reconstruction capabilities of the Autoencoder with the generative power of the GAN, contributes to the evolving landscape of generative design. The hybrid model offers a unique synthesis of realism and creativity, providing a valuable tool for professionals seeking inspiration and novel design solutions.
    
    **7.4 Reflection on Challenges:**
    hroughout the project, we navigated challenges related to training time, evaluation metrics, and dataset limitations. These challenges, while significant, have offered valuable insights and opportunities for refinement in future iterations of the model. Addressing these challenges will contribute to the robustness and applicability of generative models in architectural design.
    
    **7.5 Future Directions:**
    As we conclude this project, it is clear that there are numerous avenues for future research and development. Enhancing the model's creativity, refining user-centric design principles, and ensuring robustness and generalization are areas that warrant continued exploration. These efforts will contribute to the ongoing advancement of generative design methodologies.
    
    **7.6 Final Thoughts:**
    In final consideration, the successful implementation of our GAN-Autoencoder model represents a step forward in the intersection of artificial intelligence and architectural design. We anticipate that this project will inspire further innovation, collaboration, and exploration within the broader realm of generative design. As technology continues to evolve, we look forward to witnessing the transformative impact of generative models on the creative processes that shape our built environment.

    """)

    # References section
    st.title("References")
    st.write("""
        1. [Estate_plot_groups GitHub](https://github.com/aakgna/Estate_plot_groups)
        2. [AE-T3 Plant Images Denoising GitHub](https://github.com/adityamushyam/AE-T3/blob/main/Plant%20Images%20Denoising.ipynb)
        3. https://www.youtube.com/watch?v=dpxbEHfCtxw
        4. https://www.techtarget.com/searchenterpriseai/definition/generative-adversarial-network-GAN     
             
    """)




elif selected_nav == "Explorer":


    notebook_path = "files/autoencoder.ipynb"
    st.title("Donwload the code by clicking download button")
    download_code(notebook_path)
    images = ["image/img1.png", "image/img2.png", "image/img3.png", "image/img4.png","image/img5.png","image/img6.png","image/img7.png"]
    display_images(images)


elif selected_nav == "video":
    st.title("Explanation video ")
    st.video("https://youtu.be/8uGcMgpR0HQ")

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
            <p><b>General Inquiries:</b> praveenkumar.jobconnect@gmail.com</p>
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
