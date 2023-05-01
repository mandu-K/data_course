import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is {}'.format(title))

first_name = st.text_input('Enter your first name', max_chars=10)
st.write('Your first name is {}'.format(first_name))

number = st.number_input('Insert a number', min_value=0, max_value=30)
st.write('The current number is ', number)