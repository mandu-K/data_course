import streamlit as st

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.text('Hello World. Streamlit text')
name = 'Mingyu Kim'
st.text('Hi, {}'.format(name))

st.markdown('## This is markdown')


st.success('성공적으로 저장하였습니다.')
st.warning('업로드 할 수 없는 파일 형식입니다.')
st.info('알려드립니다.')
st.error('This is an error')
st.exception('This is an exception')

st.write('Normal Text')
st.write('## This is a markdown text')
st.write(1+2)
st.write(dir(st))

st.help(range)




st.header('display json')
st.json({'data': 'name'})

st.header('display code')
st.code('''
def sayHello():
    print('Hello Streamlit')
''', language='python')



title = st.text_input('Movie title', 'Life of Brian')
st.write('Your first name is {}'.format(title))

first_name = st.text_input('Enter your first name', max_chars=10)
st.write(f'Your first name is {first_name}')

number = st.number_input('Insert a number', min_value=0, max_value=30)
st.write('The current number is', number)

st.image('image/streamlit.png')