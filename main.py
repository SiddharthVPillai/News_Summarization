import streamlit as st
from prediction import PreprocessingPipeline, Model
from scraper import scrape
txt_cleaner = PreprocessingPipeline()

st.title("News Summarization")


option = st.sidebar.selectbox("Select method",("paragraph","url"))
model_name = st.sidebar.selectbox("Select model",("t5-base","bart-base"))
model = Model(model_name)

if option == "paragraph":
    txt = st.text_area(label='Enter paragraph for summarization')
elif option == "url":
    txt = txt = st.text_input(label='Enter url')

scraped_txt = scrape(txt) if option=="url" else txt
print(scraped_txt)
cleaned_txt = txt_cleaner.preprocess_pipeline(scraped_txt)
summary = model.predict(cleaned_txt)
st.write("## Generated Summary:")
st.write(summary)

