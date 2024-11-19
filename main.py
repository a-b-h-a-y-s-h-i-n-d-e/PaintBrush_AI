from model import inference

import streamlit as st 
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Paintbrush AI",
                   page_icon="./assets/favicon.png", layout="centered")

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- Small Header part ---------

title = '<p style="text-align:center; font-size:50px; color:#f4d03f;"> Paintbrush AI 🖌️</p>'
st.markdown(title, unsafe_allow_html=True)

info = """<b> What is PaintBrush AI ? </b> &nbsp; It uses Neural style transfer technique which takes Content 
image and style image as input and create Digital art !! <br> <b> What is Neural style Transfer ?? </b> &nbsp;
Neural style transfer (NST) is a computer vision technique that uses deep learning to combine the style of one image with 
the content of another
"""
st.markdown(info, unsafe_allow_html=True)

# Demo Image
st.image(image="./assets/demo.png")
st.markdown("<br>", unsafe_allow_html=True)




# -------- Left Sidebar -> give some sample images to use

with st.sidebar:

    st.image(image="./assets/giphy.gif")
    st.markdown("</br>", unsafe_allow_html=True)
    
    st.markdown('You can use below sample images to try out')

    # example images
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content1.jpg")
    with col2:
        st.image(image="./assets/style1.jpg")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content2.jpg")
    with col2:
        st.image(image="./assets/style2.jpg")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content3.jpg")
    with col2:
        st.image(image="./assets/style3.jpg")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content4.jpg")
    with col2:
        st.image(image="./assets/style4.jpg")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content5.jpg")
    with col2:
        st.image(image="./assets/style5.jpg")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content6.jpg")
    with col2:
        st.image(image="./assets/style6.jpg")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image="./assets/content7.jpg")
    with col2:
        st.image(image="./assets/style7.jpg")
    





# -------- Body Part--------

# input boxes
col1, col2 = st.columns(2)
content_image = None
style_image = None

with col1:
    content_image = st.file_uploader(
        "Content Image"
    )
with col2:
    style_image = st.file_uploader(
        "Style Image"
    )

if content_image is not None and style_image is not None:
    
    with st.spinner("This may take nearly 20-30 seconds!!"):

        output_image = inference(content_image, style_image)

        col1, col2 = st.columns(2)
        with col1:
            st.image(output_image)
        
        with col2:
            st.markdown("</br>", unsafe_allow_html=True)
            st.markdown(
                "<b> You can also download the image <b>", unsafe_allow_html=True
            )
            buffered = BytesIO()
            output_image.save(buffered, format="JPEG")
            st.download_button(
                label="Download image",
                data=buffered.getvalue(),
                file_name="output.png",
                mime="image/png")


            