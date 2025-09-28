import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from utils import get_funny_caption
import textwrap
import random
import requests
from io import BytesIO

st.set_page_config(page_title="Pro Meme Generator", layout="centered")

st.markdown(
    """<style>
    .stApp { background-color: #1e1e2f; color: #e0e0e0; }
    .css-18e3th9 h1 { color: #ffcc00; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #2a2a3d; color: #e0e0e0; }
    .stFileUploader>div>div>input { background-color: #2a2a3d; color: #e0e0e0; }
    .stButton>button { background-color: #ffcc00; color: #1e1e2f; font-weight: bold; }
    .stButton>button:hover { background-color: #ffaa00; color: #fff; }
    .stImage>div>img { border: 2px solid #ffcc00; border-radius: 10px; }
    </style>""", unsafe_allow_html=True
)

st.title("😂 Pro Meme Generator")
st.markdown("Upload an image or enter an image URL, generate a caption, and download your meme!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image_url = st.text_input("Or enter an image URL (jpg/png)")
user_caption = st.text_input("Enter your caption (or leave blank for random)")

def load_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        st.error("Failed to load image from URL.")
        return None

def draw_pro_caption(img, caption, font_path=None):
    draw = ImageDraw.Draw(img)
    width, height = img.size

    font_size = random.randint(25, 40)
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    caption = caption.upper()
    wrapped_text = textwrap.fill(caption, width=30)
    lines = wrapped_text.split('\n')
    total_height = sum([draw.textsize(line, font=font)[1] for line in lines])
    y_text = height - total_height - 10

    for line in lines:
        text_width, text_height = draw.textsize(line, font=font)
        x_text = (width - text_width) / 2
        draw.text((x_text, y_text), line, font=font, fill="white",
                  stroke_width=2, stroke_fill="black")
        y_text += text_height
    return img

img = None
if uploaded_file:
    img = Image.open(uploaded_file)
elif image_url:
    img = load_image_from_url(image_url)

if img:
    caption = user_caption if user_caption else get_funny_caption()
    img = draw_pro_caption(img, caption)
    st.image(img, caption="Here’s your meme!", use_column_width=True)

    img.save("meme.png")
    with open("meme.png", "rb") as file:
        st.download_button("Download Meme", file, "meme.png")