import streamlit as st

import joblib
import time
from PIL import Image
import base64


gender_nv_model = open("model/anomalyModel.pkl","rb")
gender_clf = joblib.load(gender_nv_model)

def predict_gender(duration,src,dst):
  vec=[]
  vec.append(duration)
  vec.append(src)
  vec.append(dst)
  result = gender_clf.predict([vec])
  return result
      
def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)
  
def main():
  #st.title("Anomaly Detection")
  original_title = '<b><p style="font-family:Courier; color:white; font-size: 50px;">Anomaly Detection</p><b>'
  st.markdown(original_title, unsafe_allow_html=True)
  #html_temp = """
  #<div style="background-color:blue;padding:10px">
  #<h2 style="color:grey;text-align:center;">Streamlit App </h2>
  #</div>
  #"""
  #st.markdown(html_temp,unsafe_allow_html=True)
  with open("background.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
  st.markdown(
  f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
  unsafe_allow_html=True
  )
  tabs_font_css = """
	<style>
	div[class*="stTextArea"] label {
	  font-size: 30px;
	  color: red;
	  font-weight: bold;
	}

	div[class*="stTextInput"] label {
	  font-size: 30px;
	  color: blue;
	  font-weight: bold;
	}

	div[class*="stNumberInput"] label {
	  font-size: 35px;
	  color: white;
	  font-weight: bold;
	}

	</style>
	"""

  st.write(tabs_font_css, unsafe_allow_html=True)
  duration = st.number_input("Enter duration")
  duration=int(duration)
  src = st.number_input("Enter src")
  src=int(src)
  dst = st.number_input("Enter dst")
  dst=int(dst)
  if st.button("Predict"):
    result = predict_gender(duration,src,dst)
    if result[0] == 1:
      prediction = 'clean'
      img = 'good.png'
      color="green"
    else:
      color="red"
      result[0] == 1
      prediction = 'anomaly'
      img = 'mal.png'
    txt='duration: {} src: {} dst: {} was classified as {} result{}'.format(duration,src, dst, prediction,result)    
    htmlstr1=f"""<p style='background-color:{color};
                                           color:white;
                                           font-size:18px;
                                           border-radius:3px;
                                           line-height:60px;
                                           padding-left:17px;
                                           opacity:0.6'>
                                           {txt}</style>
                                           <br></p>""" 
    st.markdown(htmlstr1,unsafe_allow_html=True) 
    #st.success('duration: {} src: {} dst: {} was classified as {} result{}'.format(duration,src, dst, prediction,result))
    load_images(img)
main()
