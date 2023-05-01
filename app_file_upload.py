import streamlit as st
import pandas as pd
from PIL import Image

@st.cache

def load_image(img_file):
    return Image.open(img_file)

st.title('File Upload')
menu = ['Home', 'Dataset', 'DocumentFiled', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')
    img_file = st.file_uploader('Upload Images', type=['png', 'jpg', 'jpeg'])

    if img_file is not None:
        st.write(type(img_file))
        img_details = {'filename': img_file.name, 'filetype': img_file.type, 'filesize': img_file.size}
        st.write(img_details)
        st.image(load_image(img_file))

elif choice == 'Dataset':
    st.subheader('Dataset')
    data_file = st.file_uploader('Upload CSV', type=['csv'])

    if data_file is not None:
        st.write(type(data_file))

        file_details = {'filename': data_file.name, 'filetype': data_file.type, 'filesize': data_file.size}
        st.write(file_details)

        df = pd.read_csv(data_file)
        st.dataframe(df.describe())

elif choice == 'DocumentFiles':
    st.subheader('DocumentFiles')
    docs_file = st.file_uploader('Upload Document', type=['pdf', 'docs', 'txt'])

    if st.button('Process'):
        if docs_file is not None:
            file_details = {'filename': docs_file.name, 'filetype': docs_file.type, 'filesize': docs_file.size}
            st.write(file_details)
            if docs_file == 'text/plain':
                raw_text = docs_file.read()
                st.write(raw_text)