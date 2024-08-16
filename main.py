import streamlit as st
from datetime import datetime

#function to display the current time

def display_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

#button for fun!
x = 0
def cookie_clicker():
  st.button("Eat your cookies", type="primary")
  if st.button("cookie clicker"):
    x+=1
    st.write(x)
  else:
    x = 0

#Sidebar for navigation

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

#Homepage

if page=="Home":
  st.title("Home")
  st.subheader("Welcome to my home page")

  #Display current time
  st.write(f"### Current time: {display_time()}")
  cookie_clicker()
#About page

elif page == "About":
  st.title("About")
  st.subheader("Hola! Made by Manit Gupta")













