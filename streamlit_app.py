import streamlit
streamlit.title('My Parents new Healthy dinner')

streamlit.header('🌭🌭🌭Breakfast Menu')
streamlit.text('🍍🍎🍓Omega 3 and some fruits')
streamlit.text('🍚Boiled Eggs')


streamlit.header('🍾Buit your own Breakfast Menu')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
