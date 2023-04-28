"""
This Streamlit web app provides personalized book recommendations based on the user's input. The user can choose to get recommendations with or without considering book categories.

Usage:
    Run the script with Streamlit to start the web app:
    ```
    streamlit run app.py
    ```

Functions:
    main(): The main function that handles the user interface and interaction.
    make_input_box(country_dict, language_fullname_dict, category_dict, selected_item): Creates the input box UI elements for user input and returns the corresponding values.

Dependencies:
    - streamlit
    - numpy
    - requests
    - PIL
    - src (local package)
        - book_recommend_info
        - info_data_load

Author:
    BoostCamp AI Tech 5th RecSys
    GitHub: https://github.com/BrotherGyu
    Email: brothergyu98@gmail.com
"""

import streamlit as st
import numpy as np
import requests

from PIL import Image

from src import book_recommend_info
from src import info_data_load


def main():
    # SETTING PAGE CONFIG TO WIDE MODE
    st.set_page_config(layout="wide")
    st.header('Please enter your information')
    st.markdown("---")

    ## sidebar 
    st.sidebar.title('Book Recommend')
    st.sidebar.markdown("---")
    selected_item = st.sidebar.radio('Select', ('Use Category', 'Not Use Category'))

    country_dict, language_dict, language_fullname_dict, category_dict, idx2info = info_data_load()

    if selected_item == 'Use Category':
        age_process, country, language, category, books_number = make_input_box(country_dict, language_fullname_dict, category_dict, selected_item)
        
        if st.button('Recommend Books'):
            age_inp = age_process
            country_inp = country_dict[country]
            language_inp = language_dict[language]
            use_category_inp = True
            category_inp = category_dict[category]
            predict_li = book_recommend_info(age_inp, country_inp,language_inp,use_category_inp, category_inp)
            arr = np.array(predict_li)
            idxs = np.argsort(-arr)[:books_number]
            st.markdown("---")
            for idx in list(idxs):
                url = idx2info[idx][3]
                # Send an HTTP GET request to the URL
                img = request_img(url)
                col1, col2 = st.columns(2)
                col1.image(img, width=100)
                col2.write("Book Title - {}".format(idx2info[idx][0]))
                col2.write("Book Author - {}".format(idx2info[idx][1]))
                col2.write("Year of Publication - {}".format(idx2info[idx][2]))
                st.markdown("---")

    elif selected_item == 'Not Use Category':
        age_process, country, language, books_number = make_input_box(country_dict, language_fullname_dict, category_dict, selected_item)
        
        if st.button('Recommend Books'):
            age_inp = age_process
            country_inp = country_dict[country]
            language_inp = language_dict[language]
            use_category_inp = False
            category_inp = None
            predict_li = book_recommend_info(age_inp, country_inp,language_inp,use_category_inp, category_inp)
            arr = np.array(predict_li)
            idxs = np.argsort(-arr)[:books_number]
            st.markdown("---")
            for idx in list(idxs):
                url = idx2info[idx][3]
                # Send an HTTP GET request to the URL
                img = request_img(url)
                col1, col2 = st.columns(2)
                col1.image(img, width=100)
                col2.write("Book Title - {}".format(idx2info[idx][0]))
                col2.write("Book Author - {}".format(idx2info[idx][1]))
                col2.write("Year of Publication - {}".format(idx2info[idx][2]))
                st.markdown("---")


    st.sidebar.markdown("---")
    st.sidebar.subheader("Contact Us")
    st.sidebar.write("BoostCamp AI Tech 5th RecSys")
    st.sidebar.write("GitHub: https://github.com/BrotherGyu")
    st.sidebar.write("Email: brothergyu98@gmail.com")


# Creates the input box UI elements for user input and returns the corresponding values
def make_input_box(country_dict, language_fullname_dict, category_dict, selected_item):
    age = st.number_input('Age [5 ~ 100]',min_value=5, max_value=100)
    age_process = min(int(age)//10 , 6)

    country = st.selectbox('Country', country_dict.keys())
    language = st.selectbox('Language', language_fullname_dict.values())

    ## Convert language values to visibility
    values_list = list(language_fullname_dict.values())
    language = list(language_fullname_dict.keys())[values_list.index(language)]

    if selected_item == 'Use Category':
        category = st.selectbox('Category', category_dict.keys())
        st.sidebar.markdown("---")
        st.write('[age: {}, country: {}, language: {}, category: {}]'.format(age, country, language_fullname_dict[language], category))
    else:
        st.sidebar.markdown("---")
        st.write('[age: {}, country: {}, language: {}]'.format(age, country, language_fullname_dict[language]))

    st.markdown("---")
    books_number = st.number_input('Number of books to be recommended [10 ~ 100]',min_value=10, max_value=100)

    if selected_item == 'Use Category':
        return age_process, country, language, category, books_number
    else:
        return age_process, country, language, books_number


# Send an HTTP GET request to the URL
def request_img(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    img = np.asarray(Image.open(requests.get(url, stream=True, headers = header).raw))
    return img


if __name__=='__main__':
    main()
    print('done')