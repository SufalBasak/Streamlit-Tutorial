import streamlit as st

import pandas as pd
#st.write("Text Element")
#title
st.title("Streamlit Tutorial")

#header
st.header("This is a Header")

#subheader
st.subheader("This is a Subheader")

#title
st.text("Simple text in Streamlit")

#badge
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

#markdown
st.markdown("""
### Markdown Example
- Bullet point
- **Bold**
- *Italic*
""")

#caption
st.caption("© 2026 Sufal Basak")

st.write("--------------------------------------------------------")

st.subheader("Data Elements")


#data frame
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 95]
})

st.dataframe(df)

#Data Editor
st.data_editor(df)

#Table (Static)
st.table(df)
#Metric
st.metric(label="Temperature", value="28°C", delta="+2°C")
st.metric("Humidity", "65%", "-5%")
st.metric("CPU Usage", "72%", "+10%")
st.metric("RAM Usage", "6.5 GB", "+0.8 GB")

st.write("-----------------------------------------------------")
st.subheader("Chat Elements (AI-style UI)")

#chat input
user_msg = st.chat_input("Type your message")
if user_msg:
    st.write(user_msg)

#chat massage
with st.chat_message("user"):
    st.write("Hello Streamlit")

with st.chat_message("assistant"):
    st.write("Hi! How can I help?")
#status
with st.status("Processing..."):
    st.write("Loading data...")

#some fun with chat 
prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])
    
st.write('---------------------------------------------------')  

st.subheader("Chart")

#line chart 
st.write("Line chart")
st.line_chart(df["Marks"])

#bar Chart
st.write("bar Chart")
st.bar_chart(df["Marks"])

#Area Chart
st.write("Area Chart")
st.area_chart(df["Marks"])

#Scatter Chart
st.write("Scatter Chart")
st.scatter_chart(df)

#map  Chart
st.write("map  Chart")
map_df = pd.DataFrame({
    'lat': [22.57, 28.61],
    'lon': [88.36, 77.20]
})
st.map(map_df)









# python -m streamlit run app.py
