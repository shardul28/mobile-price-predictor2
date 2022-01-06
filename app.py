import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))

st.title('Mobile Price Prediction')
original_title = '<h1 style="color:White; font-size: 20px;">Created by Shardul Tambe</h1>'
st.markdown(original_title, unsafe_allow_html=True)
st.sidebar.header('Mobile Data')
#image = Image.open('bb.jpg')
#st.image(image, '')

# FUNCTION
def user_report():
  battery_power = st.sidebar.slider('battery_power', 0,7000, 1 )
  blue = st.sidebar.slider('blue', 0,1, 1 )
  clock_speed = st.sidebar.slider('clock_speed',0.0,4.0, 0.1 )
  dual_sim =  st.selectbox(
     'dual_sim support,Yes(1),No(0)',
     (0, 1))
  fc = st.sidebar.slider('Front Camera mega pixels', 0,100, 1 )#front camera megapixels
  fourgsupport = st.selectbox(
     '4G support,Yes(1),No(0)',
     (0, 1))
  #four_g = st.sidebar.slider('4G Support', 2000,2020, 2000)
  int_memory = st.sidebar.slider('Internal Memory in Gigabytes', 1,100, 1)
  m_dep= st.sidebar.slider('Mobile Depth in cm', 0.0,4.0, 0.1)#Mobile Depth in cm
  mobile_wt= st.sidebar.slider('Weight of mobile phone', 0,200, 1)
  n_cores= st.sidebar.slider('Number of cores of processor', 0,8,1)
  pc= st.sidebar.slider('Primary Camera mega pixels', 0,20,1)
  px_height= st.sidebar.slider('Pixel Resolution Height', 0,2000,1)
  px_width= st.sidebar.slider('Pixel Resolution Width', 0,2000,1)
  ram= st.sidebar.slider('Random Access Memory in Mega Bytes', 0,4000,1)
  sc_h= st.sidebar.slider('Screen Height of mobile in cm', 0,20,1)
  sc_w= st.sidebar.slider('Screen Width of mobile in cm', 0,20,1)
  talk_time= st.sidebar.slider('longest time that a single battery charge will last when you are aka talktime', 0,20,1)
  threegsupport = st.selectbox(
     '3G support,Yes(1),No(0)',
     (0, 1))
  touchscreen = st.selectbox(
     'Has touch screen or not,Yes(1),No(0)',
     (0, 1))
  wifi = st.selectbox(
     'Has wifi or not,Yes(1),No(0)',
     (0, 1))

  user_report_data = {
      'battery_power': battery_power,
      'blue':blue,
      'clock_speed':clock_speed,
      'dual_sim': dual_sim,
      'fc ':fc ,
      'fourgsupport':fourgsupport,
      'int_memory':int_memory,
      'm_dep':m_dep,
      'mobile_wt':mobile_wt,
      'n_cores':n_cores,
      'pc':pc,
      'px_height':px_height,
      'px_width':px_width,
      'ram':ram,
      'px_width':px_width,
      'sc_h':sc_h,
      'sc_w':sc_w,
      'talk_time':talk_time,
      'threegsupport':threegsupport,
      'touchscreen':touchscreen,
      'wifi':wifi
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Mobile Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Mobile price range')
#0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).

if salary==0:
    salaryrange="low cost"
elif  salary==1:
    salaryrange="medium cost"
elif  salary==2:
    salaryrange="high cost"
else:
    salaryrange="very high cost"

#st.subheader('The mobile price range is'+str(np.round(salary[0], 2)))
st.subheader('The mobile price range is '+str(salaryrange))
