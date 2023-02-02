import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from language_tool_python import LanguageTool
import io

def grammar_check(text):
    # Initialize the grammar checker
    tool = LanguageTool('en-US')

    # Define the text to check
    # text = "I have went to the store."

    # Check grammar errors
    errors = tool.check(text)

    # Print the corrected text
    corrected_text = tool.correct(text)
    # print("Corrected text:", corrected_text)

    return corrected_text, len(errors)

st.write("# GramChecker")
st.write('_______________________')
st.write("""## How it works""")
st.write("GramChecker is a tool which helps to check and correct the English grammar." 
        " This tool check your grammar with the help of Artificial Intelligence.")

#image
image = Image.open('images/gram.jpg')
st.image(image)

txt = st.text_area('Enter your text')

if st.button('Check'):
    load_screen = 1
    while load_screen == 1:
        with st.spinner('Correcting grammar, please wait!'):
            corrected_text, errors = grammar_check(txt)
            # Corrected Text
            st.write("## Corrected Text")
            st.write(corrected_text)

            # Mentioning Error Found
            st.write("## Errors")
            st.write(errors)

            load_screen = 0
    st.snow()
else:
    pass