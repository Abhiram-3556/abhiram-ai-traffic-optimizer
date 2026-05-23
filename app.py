import streamlit as st
import numpy as np
import cv2
from PIL import Image
from detector.detect import detect

st.set_page_config(page_title='AI Traffic Optimizer')

st.title('🚦 AI Traffic Flow Optimization')
st.subheader('Vehicle Detection Demo')

camera=st.camera_input('Capture traffic image')

if camera:
    image=Image.open(camera)
    frame=np.array(image)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    output,count=detect(frame)

    st.image(cv2.cvtColor(output,cv2.COLOR_BGR2RGB))
    st.metric('Detected Vehicles',count)
