import streamlit as st

st.title("AskCrawler - The :blue[Smart] :brain: WebScrapper :magic_wand:")

st.subheader("Search data on your favorite site: ")

input_url = 'https://www.dummmy.com'
submit = False

with st.form('url_form'):
    input_url = st.text_input(label="URL", placeholder="Enter the URL", label_visibility="hidden")
    submit = st.form_submit_button("Search")

if submit:
    st.write(input_url)



st.write("Scraping data....")