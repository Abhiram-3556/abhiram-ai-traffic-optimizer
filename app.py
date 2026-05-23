import streamlit as st

st.set_page_config(page_title='AI Traffic Optimizer')

st.title('🚦 AI Traffic Flow Optimization')
st.write('Phase 1: Environment and webcam setup')

camera=st.camera_input('Capture traffic scene')

if camera:
    st.success('Camera connected successfully')
