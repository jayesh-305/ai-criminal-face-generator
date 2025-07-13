import streamlit as st

st.title("🔍 Criminal Face Generator")
st.write("Enter suspect details:")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80)
face_shape = st.selectbox("Face Shape", ["Round", "Oval", "Square", "Heart"])
hair = st.selectbox("Hair Type", ["Short", "Medium", "Long", "Bald"])

if st.button("Generate Face"):
    st.image("generated_face.png", caption="Sample Suspect Face", width=300)
