import streamlit
import pandas
streamlit.title('Healthy Diner Menu')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Oatmeal')
streamlit.text('🥗 Kale Smoothie')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.text('🐔 Eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
