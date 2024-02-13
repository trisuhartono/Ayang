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
with st.sidebar:
    selected = option_menu(
        menu_title = 'MENU',
        options = ['BERANDA', 'UNDANGAN', 'UPLOAD DONG', 'WITH MY LOVE'],

    )
st.sidebar.success("PILIH MENU DI ATAS")
if selected == 'BERANDA':
    st.write('Haloo ayaangkuu 🥰🥰🥰')
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

    
if selected == 'UNDANGAN':
    st.write('undungan nih buat ayaang❤❤')
    st.write ('') 
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
if selected == 'UPLOAD DONG':
    st.write('yaaa, halaman terkhir nih ay🤭')
    st.write ('') 
    temp = st.file_uploader("Uplod foto cantiknya dooong ayaangkuu 🥰🥰🥰")
    buffer = temp
    temp_file = NamedTemporaryFile(delete=False)
    if buffer:
        temp_file.write(buffer.getvalue())
        #st.write(image.load_img(temp_file.name))


    if buffer is None:
        st.text("yaaaah ko belum ada fotonya, coba lagi ya ayangkuuu😘😘")

    else:
        image = Image.open(temp)
        st.image(image,use_column_width=True)
        st.write('<center><h1>❤❤❤HAI AYAANGKUUUU CANTIIIKKKK❤❤❤</h1></center>', unsafe_allow_html=True) 
        st.write('<center><h3>Semangat kuliahe nggih ayaangkuuu❤❤❤, Mugi diparingi lancar sedoyo nggih cantiiiik❤❤❤</h3></center>', unsafe_allow_html=True) 
      
if selected == 'WITH MY LOVE':
    st.write('Haloo ayaangkuu 🥰🥰🥰')
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('1.jpg') 
    with col2:
        st.image('2.jpg') 
        
     
    
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
        st.image('ht.png') 
    with col3:
        st.write("")

    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('3.jpg') 
    with col2:
        st.image('4.jpg') 
    





