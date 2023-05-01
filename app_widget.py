import streamlit as st

name = 'Mingyu Kim'

st.header('Button')
if st.button('Submit', key=1):
    st.write('Name: {}'.format(name))

if st.button('Submit', key=2):
    st.write('Full Name: {}'.format(name))

st.header('Radio Button')
status = st.radio('What is your status',
                  ('Active', 'Inactive'))
if status == 'Active':
    st.success('You are active')
elif status == 'Inactive':
    st.warning('You are inactive')

st.header('Checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('You agreed')