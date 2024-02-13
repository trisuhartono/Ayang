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

st.session_state.page_select = st.sidebar.radio('Pages', ['Page 1', 'Page 2', 'Page 3'])

if st.session_state.page_select == 'Page 1': 
    image = Image.open('poto.jpeg')
    new_size =  (1000,400)
    
# menyesuaikan ukuran gambar
    resized_image = image.resize(new_size)
    col1, col2, col3 = st.columns([1, 7, 1])
    with col1:
        st.write("")
    with col2:
        st.image(resized_image, caption='', use_column_width=True)
    with col3:
        st.write("")

    st.write('<center><h1>SELAMAT HARI VALENTINE AYANGKUUU❤❤❤</h1></center>', unsafe_allow_html=True)
    #st.write('''<center><h3>APLIKASI INI DIRANCANG SEBAGAI TUGAS AKHIR di SEKOLAH TINGGI ILMU KESEHATAN SEMARANG</h3></center>''', unsafe_allow_html=True)
  
    #st.write('')
    #st.write('')
    #st.write('''<center><h6>Tahun Akademik 2022/2023</h6></center>''', unsafe_allow_html=True)
    #st.write('''<center><h6>Oleh : TRI SUHARTONO</h6></center>''', unsafe_allow_html=True)

#st.set_page_config(page_title="trisuhartono klasifikasi pneumonia")

    
    next = st.button('Lanjut ay...')
    if next:
        st.session_state.page_select = 'Page 2'

        
if st.session_state.page_select == 'Page 2': 
    st.write('Kepada Yang Tercantik: Ayangkuuu Dek Anis Muzkiyah')
    st.write('Hal: kartu Ucapan')
    st.write('') 
    st.write('')
    st.write('Dengan penuh Cinta') 
    st.write('Dengan datangnya kartu ucapan ini, yang bertanda tangan dibawah ini') 
    st.write('Nama: Tri suhartono') 
    st.write('Jabatan : Calon suami Anis Muzkiyah') 
    st.write('Masa Jabatan : SELAMANYA') 
    st.write('') 
    st.write('Dengan ini mengucapkan selamat HARI VALENTINE 2024.') 
    st.write('Demikian Kartu ucapan ini saya buat dengan cinta seluah alam raya terkhusus bidadariku yang cantiiik, yang maniiisss, yang baiikkk, dan tak ada duanya') 
    st.write('') 
    st.write ('') 
    st.write ('Terdanda') 
    st.write('Mamas Ganteng') 

    
    next = st.button('Lanjut lagi ay...')
    if next:
        st.session_state.page_select = 'Page 3'
        
if st.session_state.page_select == 'Page 3': 
    temp = st.file_uploader("Uplod foto cantiknya dooong ayaangkuu 🥰🥰🥰")
    buffer = temp
    temp_file = NamedTemporaryFile(delete=False)
    if buffer:
        temp_file.write(buffer.getvalue())
        #st.write(image.load_img(temp_file.name))


    if buffer is None:
        st.text("yaaaah ko belum ada fotonya, coba lagi ya ayangkuuu😘😘")

    else:
   # img = image.load_img(temp_file.name, target_size=(50, 50),color_mode='grayscale')

        image = Image.open(temp)
        st.image(image,use_column_width=True)
        st.write('<center><h1>❤❤❤HAI AYAANGKUUUU CANTIIIKKKK❤❤❤</h1></center>', unsafe_allow_html=True) 
        st.write('<center><h3>Semangat kuliahe nggih ayaangkuuu❤❤❤, Mugi diparingi lancar sedoyo nggih cantiiiik❤❤❤</h3></center>', unsafe_allow_html=True) 
      
import pickle as pkle
import os.path

pages = ['Page1','Page2','Page3']if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(pages):
        next_clicked = 0 
else:
    next_clicked = 0 

if next:
    next_clicked = next_clicked+1
    if next_clicked == len(pages):
        next_clicked = 0 

choice = st.sidebar.radio("Pages",('Page1','Page2', 'Page3'), index=next_clicked)
pkle.dump(pages.index(choice), open('next.p', 'wb'))

if choice == 'Page1':
    st.title('Page 1')
elif choice == 'Page2':
    st.title('Page 2')
elif choice == 'Page3':
    st.title('Page 3')

next = st.button('Go to next page')
    



