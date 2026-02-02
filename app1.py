import streamlit as st
import pandas as pd
import numpy as np

#adding tittle
st.title("Day:1 Streamlit Learning")

#adding simple text
st.write('Here is a simple text')

# user input 

number = st.slider("pick a number", 0 ,100, 10)

# print the text of number 
st.write(f'you selecter: {number}')

#add button

if st.button('Greeting'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

     #add radio button with option
     genre = st.radio(
          "What's your favourite movie genre",
          ('comedy','Drama','Documentary')
     )

     #print the text of genre
     st.write(f'You Selected: {genre}')

     #add a dropdown list

    #  option = st.selectbox(
    #       'How would you like to be contacted?',
    #       ('Email','Home Phone', 'Mobile Phone')
    #  )

# add a dropdown option on the left slider
option = st.sidebar.selectbox(
          'How would you like to be contacted?',
          ('Email','Home Phone', 'Mobile Phone')
     )

#add your whatsapp number
st.sidebar.text_input("Enter whatsapp number")


#add a file uploder

uploaded_file = st.sidebar.file_uploader("choose a csv file", type="csv")

#create a line plot

st.title("📈 Line Plot Example")

# # Create sample data
data = pd.DataFrame({
    "Day": range(1, 11),
    "Sales": np.random.randint(10, 100, 10)
})

st.write("### Sales over Days")
st.line_chart(data.set_index("Day")) 





#footer
st.markdown(
    "© 2026 **Sufal Basak** | Built with ❤️ using Streamlit",
    unsafe_allow_html=True
)



