import streamlit as st

st.set_page_config(page_title="Study Ninja - Lets You Focus 🥷", page_icon="🥷", layout="wide")
st.header("Notes :scroll:")

import streamlit as st
import base64

def pdf_to_base64(pdf_file):
    # Convert the PDF file to base64 encoding
    return base64.b64encode(pdf_file).decode()



if uploaded_file is not None:
    # Convert the uploaded file to base64
    pdf_base64 = pdf_to_base64(uploaded_file.read())
    
    # Create an HTML iframe to display the PDF inline
    pdf_embed = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500" type="application/pdf"></iframe>'
    
    # Use components to render the iframe in the Streamlit app
    st.markdown(pdf_embed, unsafe_allow_html=True)
