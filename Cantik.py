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
with st.sidebar:
    selected = option_menu(
        menu_title = 'MENU',
        options = ['BERANDA', 'PNEUMONIA','TENTANG KAMI', 'MULAI KLASIFIKASI'],

    )
st.sidebar.success("PILIH MENU DI ATAS")
if selected == 'BERANDA':
    st.write(f'Anda sedang berada pada laman >> {selected}')
    #st.image('logo.png', width=200)
    image = Image.open('logo.png')
    new_size =  (1000,1400)
    
# menyesuaikan ukuran gambar
    resized_image = image.resize(new_size)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
         st.image(resized_image, caption='', use_column_width=True)
    with col3:
        st.write("")


    st.write('<center><h1>SELAMAT DATANG DI APLIKASI KLASIFIKASI PENYAKIT PNEUMONIA</h1></center>', unsafe_allow_html=True)
    st.write('''<center><h3>APLIKASI INI DIRANCANG SEBAGAI TUGAS AKHIR di SEKOLAH TINGGI ILMU KESEHATAN SEMARANG</h3></center>''', unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('''<center><h6>Tahun Akademik 2022/2023</h6></center>''', unsafe_allow_html=True)
    st.write('''<center><h6>Oleh : TRI SUHARTONO</h6></center>''', unsafe_allow_html=True)
"""
if selected == 'PNEUMONIA':
    st.write(f'Anda sedang berada pada laman >> {selected}')
    st.header('PENYAKIT PNEUMONIA')
    st.write('''Pneumonia adalah peradangan paru-paru yang disebabkan oleh infeksi.
    Pneumonia bisa menimbulkan gejala yang ringan hingga berat. Beberapa gejala yang
    umum dialami penderita pneumonia adalah batuk berdahak, demam, dan sesak napas.''')
    st.image('pne.jpg', width=500, caption='(www.alodokter.com)') 
    st.write('''Pneumonia juga dikenal dengan istilah paru-paru basah. Pada kondisi ini, infeksi 
    menyebabkan peradangan pada kantong-kantong udara (alveoli) di salah satu atau kedua
    paru-paru. Akibatnya, alveoli dipenuhi cairan atau nanah sehingga membuat penderitanya sulit bernapas.''')
    st.write('''Pneumonia bisa disebabkan oleh infeksi virus, bakteri, atau jamur. SARS-CoV-2 yang menyebabkan COVID-19 adalah
    salah satu jenis virus yang bisa menyebabkan pneumonia. Pneumonia terkadang juga bisa muncul beserta penyakit paru-paru lain, misalnya TB paru.''')
    st.write('''Pneumonia merupakan salah satu penyebab kematian tertinggi pada anak-anak di seluruh dunia. Data dari World Health Organization menyebutkan bahwa pada tahun 2019, sebanyak 740.180 anak-anak meninggal akibat pneumonia.''')
    st.subheader('Penyebab dan Gejala Pneumonia')
    st.write('''Pneumonia dapat disebabkan oleh infeksi bakteri, virus, dan jamur. Beberapa virus yang 
    umum menyebabkan pneumonia adalah virus influenza, respiratory syncytial virus (RSV), dan SARS-CoV-2. 
    Sementara jenis bakteri yang umum menyebabkan pneumonia adalah Streptococcus pneumonia.''')
    st.write('''Gejala pneumonia cukup bervariasi. Namun, umumnya pneumonia ditandai dengan batuk berdahak, demam, menggigil, sesak napas, nyeri dada ketika bernapas atau batuk, mual dan muntah, nafsu makan menghilang, serta tubuh yang mudah lelah.''')
    st.subheader('Pengobatan dan Pencegahan Penumonia')
    st.write('''Pengobatan pneumonia akan disesuaikan dengan penyebab dan tingkat keparahan yang dialami pasien. Pneumonia akibat infeksi bakteri akan ditangani dengan obat antibiotik.
    Dokter juga dapat memberikan obat pneumonia lain untuk meredakan gejala batuk, demam, atau nyeri.''')
    st.write('''Pneumonia dapat dicegah dengan beberapa cara, di antaranya menjalani vaksinasi, menjaga kebersihan diri, misalnya rajin mencuci tangan dan tidak menyentuh hidung atau mulut
    dengan tangan yang belum dicuci, dan menghindari kontak dengan orang yang sedang sakit''')
    st.write('ARTIKEL INI DIAMBIL DARI ALODOKTER, ANDA DAPAT MEMBUKA ARTIKEL INI DENGAN MEMBUKA LINK  https://www.alodokter.com/pneumonia')
if selected == 'TENTANG KAMI':
    st.write(f'anda sedang berada pada  >> {selected}')
    
    # membaca gambar dengan PIL dan menentukan ukuran yang diinginkan
    image = Image.open('tri.png')
    new_size = (1000,1400)
    # menyesuaikan ukuran gambar
    resized_image = image.resize(new_size)
    # membuat kolom dengan rasio 1:3
    col1, col2 = st.columns([1,2])
    # menempatkan gambar di kolom pertama
    with col1:
        st.image(resized_image, caption='', use_column_width=True)
        #st.image('tri.png', width=250)
    # menempatkan teks di kolom kedua
    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write("""
            '''NAMA    : Tri suhartono \n
            NIM     : 02320115 \n
            ALAMAT  : PEMALANG\n
            JABATAN : Peneliti 
        """)

if selected == 'MULAI KLASIFIKASI':
    st.write(f'anda sedang berada pada laman >> {selected}')
    st.title('KLASIFIKASI PENYAKIT PNEUMONIA')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    #@st.cache (allow_output_mutation=True)
    @st.cache_resource 
    def loading_model():
        cnn = tf.keras.models.load_model('modelta4.h5')
        return cnn

    cnn = loading_model()
    """
    temp = st.file_uploader("Upload Citra X-Ray")

    buffer = temp
    temp_file = NamedTemporaryFile(delete=False)
    if buffer:
        temp_file.write(buffer.getvalue())
        st.write(image.load_img(temp_file.name))


    if buffer is None:
        st.text("silakan coba lagi dan input citra X-Ray kembali.")

    else:
        img = image.load_img(temp_file.name, target_size=(500, 500),color_mode='grayscale')

  # Preprocessing the image
        """
        pimg = image.img_to_array(img)
        pimg = pimg/255
        pimg = np.expand_dims(pimg, axis=0)
#predict
        prediksi= cnn.predict(pimg)
        if prediksi>= 0.5:
             out = st.error('Anda  {:.2%} dinyatakan POSITIF PNEUMONIA'.format(prediksi[0][0])) #('Anda  {:.2%} dinyatakan POSITIF PNEUMONIA'.format(prediksi[0][0]))
    
        else:
             out = st.success('Anda {:.2%} dinyatakan BEBAS PNEUMONIA'.format(1-prediksi[0][0]))

        #st.success(out)
  """
        image = Image.open(temp)
        st.image(image,use_column_width=True)


