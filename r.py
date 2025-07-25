import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Ronaldo pictures", page_icon=":heart:", layout="wide")


#1. as sidebar menu
selected = option_menu(
        menu_title=None, # required
        options=["HOME", "IMAGES", "VIDEOS", "CONTACTS"],
        icons=["house", "images", "camera-video-fill", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal", 
    )
if selected == "HOME":
    st.title("Home of ronaldo pictures")
    st.subheader("Hi, I am saeed :wave: ")
    st.write("#")
    st.write("I am big ronaldo fan that has many many ronaldo pictures")
    st.write("[learn more>] https://facebook.com/groups/1995296401305423")
if selected == "IMAGES":
    st.title("IMAGES")
    st.subheader("images home")
    st.image("./images/1.jpg", width=500)
    st.write("---")
    st.image("./images/4.jpg", width=500)
    st.write("---")
    st.image("./images/5.jpg", width=500)
    st.write("---")
    st.image("./images/6.jpg", width=500)
    st.write("---")
    st.image("./images/22.jpg", width=500)
    st.write("---")
    st.image("./images/8.jpg", width=500)
    st.write("---")
    
if selected =="VIDEOS":
    st.title("videos")
    st.subheader("Home of ronaldo videos")
    st.write("Watch ronaldo pictures here")
if selected == "CONTACTS":
    st.title("Contacts us")
    st.write("##")
    st.subheader("Messeage me")

    contact_form="""
    <form action = "https://formsubmit.co/saeeddukku@email.com"method= "POST">
        <input type="hidden" name="_captcha" value="false"> 
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email"placeholder="your email"required>
        <textarea name="massege"placeholder="your massege here"required></textarea>
        <button type="submit">send</botton>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)