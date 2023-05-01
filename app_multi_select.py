import streamlit as st

my_lang = [
    'Python',
    'C',
    'C++',
    'C#',
    'Go',
    'Java'
]
choice = st.selectbox('Language', my_lang)
st.write('You selected {}'.format(choice))

multi_choice = st.multiselect('Multi select', my_lang)
