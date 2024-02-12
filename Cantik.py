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


image = Image.open('poto.jpeg')
new_size =  (1000,400)
    
# menyesuaikan ukuran gambar
resized_image = image.resize(new_size)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
     st.write("")
with col2:
     st.image(resized_image, caption='', use_column_width=True)
with col3:
     st.write("")

st.write('<center><h1>SELAMAT HARI VALENTINE AYANG KUUU</h1></center>', unsafe_allow_html=True)
    #st.write('''<center><h3>APLIKASI INI DIRANCANG SEBAGAI TUGAS AKHIR di SEKOLAH TINGGI ILMU KESEHATAN SEMARANG</h3></center>''', unsafe_allow_html=True)
    #st.write('')
    #st.write('')
    #st.write('')
    #st.write('')
    #st.write('')
    #st.write('''<center><h6>Tahun Akademik 2022/2023</h6></center>''', unsafe_allow_html=True)
    #st.write('''<center><h6>Oleh : TRI SUHARTONO</h6></center>''', unsafe_allow_html=True)

"""
#st.set_page_config(page_title="trisuhartono klasifikasi pneumonia")
temp = st.file_uploader("Uplod foto cantinya dooong ayaangkuu 🥰🥰🥰")

buffer = temp
temp_file = NamedTemporaryFile(delete=False)
if buffer:
     temp_file.write(buffer.getvalue())
     st.write(image.load_img(temp_file.name))


if buffer is None:
     st.text("yaaaah ko belum ada fotonya, coba lagi ya ayangkuuu😘😘")

else:
   # img = image.load_img(temp_file.name, target_size=(50, 50),color_mode='grayscale')

    image = Image.open(temp)
    st.image(image,use_column_width=True)
    st.write ('semangat cantikuuu') 
"""

