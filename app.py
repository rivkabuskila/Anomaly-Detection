import streamlit as st

import joblib
import time
from PIL import Image


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
  st.title("Anomaly Detection")
  #html_temp = """
  #<div style="background-color:blue;padding:10px">
  #<h2 style="color:grey;text-align:center;">Streamlit App </h2>
  #</div>
  #"""
  #st.markdown(html_temp,unsafe_allow_html=True)
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
    else:
      result[0] == 1
      prediction = 'mal'
      img = 'mal.png'
    
    st.success('duration: {} src: {} dst: {} was classified as {} result{}'.format(duration,src, dst, prediction,result))
    load_images(img)
main()
