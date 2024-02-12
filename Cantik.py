import streamlit as st 
import pandas as pd 
from streamlit_option_menu import option_menu

from tempfile import NamedTemporaryFile
import numpy as np
from PIL import Image 
import tensorflow as tf
from tensorflow.keras.models import load_model
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image 
from termcolor import colored

st.set_page_config(page_title="trisuhartono klasifikasi pneumonia")
temp = st.file_uploader(st.title("Uplod foto cantinya dooong ayaangkuu 🥰🥰🥰")

buffer = temp
temp_file = NamedTemporaryFile(delete=False)
if buffer:
     temp_file.write(buffer.getvalue())
     st.write(image.load_img(temp_file.name))


if buffer is None:
     st.text("silakan coba lagi dan input citra X-Ray kembali.")

else:
    img = image.load_img(temp_file.name, target_size=(50, 50),color_mode='grayscale')

  
    image = Image.open(temp)
    st.image(image,use_column_width=True)
    st.write ('semangat cantikuuu') 


