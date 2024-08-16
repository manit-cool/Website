import streamlit as st
from datetime import datetime

#function to display the current time

def display_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

#Sidebar for navigation

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home, "About"])

#Homepage

if page=="Home":
  st.title("Home")
  st.subheader("Welcome to my home page")

  #Display current time
  st.write(f"### Current time: {display_time()}")

#About page

elif page == "About":
  st.title("About")
  st.subheader("Hola! Made by Manit Gupta")













