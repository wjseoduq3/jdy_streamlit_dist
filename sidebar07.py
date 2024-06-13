import streamlit as st
from PIL import Image



st.sidebar.title('사이드바')
st.sidebar.header('텍스트입력')
user_id = st.sidebar.text_input('ID 입력', value='streamlit',max_chars=15)
user_pw = st.sidebar.text_input('PW 입력', value='1234',type='password')

st.sidebar.header('셀렉트박스')
sel_opt=['진주 궈걸이를 한 소녀','별이 빛나튼 밤','절규','월하정인']
user_opt=st.sidebar.selectbox('좋아하는 작품은?',sel_opt)
st.sidebar.write('선택한 작품은:', user_opt)

# 메인화면
st.title('스트림릿의 사이드바')
# folder =r'D:/JDY_folder/vs_ws/data/'
image_files=['Vermeer.png','Gogh.png','Munch.png','ShinYoonbok.png']

sel_img_index = sel_opt.index(user_opt)

# 선택한 항목에 맞는 이미지 파일 지정
img_file = image_files[sel_img_index]
# img_local = Image.open(folder+img_file)
img_local = Image.open(folder+img_file)
st.image(img_local,caption=user_opt)